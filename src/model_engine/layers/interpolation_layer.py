from storage_backend import registry as storage_registry
from layers import BaseLayer
from tqdm import tqdm
import numpy as np
from PIL import Image
from extensions.utils import get_concat_h
from random import randrange

class InterpolationLayer(BaseLayer):
    NAME = "interpolation"
    PREFIX = "i"

    SUPPORTED_STORAGE_BACKENDS = ["redis"]

    def __init__(self):
        super().__init__()
        self.redis_store = storage_registry.redis
        self.layer_prefixes = self.redis_store.add_layer(self.NAME, self.PREFIX)
        self.image_map_dimensions, self.results_size, self.output_gifs_path, self.results_size, self.fps, self.image_map_data, self.generator, self.generator_manager, self.num_interps = None
        self.proportion_list_1 = [0.15, 0.15, 0.35, 0.35]
        self.proportion_list_2 = [0.25, 0.25, 0.25, 0.25]

    def _update_redis(self, image_id, availability):
        key = f"{self.PREFIX}_{image_id}"
        record = {"key": key, "value": availability}
        client = storage_registry.redis
        client.upsert(self.NAME, record)

    def update(self, image_id, availablity, storage_backend="redis"):
        if storage_backend not in self.SUPPORTED_STORAGE_BACKENDS:
            raise NotImplementedError()
        _update = getattr(self, f"_update_{storage_backend}")
        _update(image_id, availablity)

    def _fetch_redis(self, key, field):
        client = storage_registry.redis
        return client.get_value(key, self.NAME, field)

    def fetch(self, key, storage_backend="redis", field=None):
        if storage_backend not in self.SUPPORTED_STORAGE_BACKENDS:
            raise NotImplementedError()
        _fetch = getattr(self, f"_fetch_{storage_backend}")
        _fetch(key, field)

    def get_interpolated_vector(self, latent_vectors, proportions):
        return sum([vector*proportion for vector, proportion in zip(latent_vectors, proportions)])

    def interpolate(self, interpolation_type, interpolation_dict):
        from components import INTERPOLATION_TYPE_TO_MANAGER_MAP
        if interpolation_type in INTERPOLATION_TYPE_TO_MANAGER_MAP.keys():
            return INTERPOLATION_TYPE_TO_MANAGER_MAP[interpolation_type](interpolation_dict)
        else:
            raise NotImplementedError
    
    def make_latent_interp_animation(self, interpolation_dict, interpolation_type):
        step_size = 1.0/self.num_interps
        all_imgs = []
        amounts = np.arange(0, 1, step_size)
        
        for alpha in tqdm(amounts):
            interpolation_dict['alpha'] = alpha
            interpolated_latent_code = self.interpolate(interpolation_type, interpolation_dict)
            images = self.generator_manager.generate_image_from_z(interpolated_latent_code)
            interp_latent_image = Image.fromarray(images[0]).resize((self.results_size, self.results_size))
            image_1 = interpolation_dict['image_1']
            image_2 = interpolation_dict['image_2']
            frame = get_concat_h(image_1, interp_latent_image)
            frame = get_concat_h(frame, image_2)
            all_imgs.append(frame)

        save_name = '{}/latent_space_traversal.gif'.format(self.output_gifs_path)
        all_imgs[0].save(save_name, save_all=True, append_images=all_imgs[1:], duration=1000/self.fps, loop=0)
        return save_name

    def transform(self, interpolation_type):
        image_1, latent_code_1 = self.generator_manager.get_image_and_associated_latent_code(self.proportion_list_1)
        image_2, latent_code_2 = self.generator_manager.get_image_and_associated_latent_code(self.proportion_list_2)
        interpolation_dict = {
            'image_1': image_1,
            'latent_code_1': latent_code_1,
            'image_2': image_2,
            'latent_code_2': latent_code_2,
        }
        return self.make_latent_interp_animation(interpolation_dict, interpolation_type)
    
    def _fetch_config(self, config):
        self.image_map_dimensions = config['generator']['image_map_dimensions']
        self.results_size = config['generator']['results_size']
        self.generated_images_path = config['media']['images']
        self.output_gifs_path = config['media']['output_gifs']

    def refresh(self, product_type):
        from components import GeneratorManager
        from api.actions import ACCESSORIES_TYPE_TO_CONFIG_MAP

        config = ACCESSORIES_TYPE_TO_CONFIG_MAP[product_type]
        self._fetch_config(config)
        self.generator_manager = GeneratorManager(self.image_map_dimensions, self.results_size, self.generated_images_path)
        self.generator = self.generator
        return {"status": "done"}