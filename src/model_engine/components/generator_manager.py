import pandas as pd
from random import randrange
from PIL import Image
from components import Generator
import matplotlib.pyplot as plt
from datetime import datetime
from services import registry as service_registry
import pandas as pd


class GeneratorManager:
    def __init__(self, image_map_dimensions, results_size, generated_images_path):
        self.generator = Generator()
        self.image_map_dimensions = image_map_dimensions
        self.results_size = results_size
        self.image_map_data = None
        self.generated_images_path = generated_images_path

    def generate_image_random(self):
        self.image_map_data = []
        image_map_dimensions = self.image_map_dimensions * self.image_map_dimensions
        for i in range(image_map_dimensions):
            image, latent_code = self.generator.generate_image_random(randrange(1000))
            self.image_map_data.append({'id': 'pos_' + str(i), 'image': image, 'latent_vector': latent_code, 'name': "image_{}_{}".format(datetime.now(), i)})

        # Image.fromarray(image[0]).resize((self.results_size, self.results_size))

    # def plot_image_map(self):
    #     fig = plt.figure(figsize=(self.image_map_dimensions * 4.6, self.image_map_dimensions * 4.6))
    #     ax = [
    #         plt.subplot(self.image_map_dimensions, self.image_map_dimensions, i + 1)
    #         for i in range(self.image_map_dimensions * self.image_map_dimensions)
    #     ]

    #     i = 0
    #     for a in ax:
    #         a.imshow(
    #             Image.fromarray(self.image_map_data['image'][i][0]).resize((self.results_size, self.results_size)),
    #             interpolation='nearest',
    #         )
    #         a.set_xticklabels([])
    #         a.axes.get_xaxis().set_visible(False)
    #         a.set_yticklabels([])
    #         a.axes.get_yaxis().set_visible(False)

    #         i = i + 1

    #     fig.subplots_adjust(wspace=0, hspace=0)
    #     plt.subplots_adjust(wspace=0, hspace=0)
    #     plt.savefig(
    #         '{}handbags-fakes-{}.png'.format(self.generated_images_path, str(datetime.utcnow())),
    #         bbox_inches='tight',
    #         pad_inches=0,
    #     )

    def plot_image_map(self, new_image_map):
        fig = plt.figure(figsize=(self.image_map_dimensions * 4.6, self.image_map_dimensions * 4.6))
        for i in range(0, len(new_image_map)):
            fig, ax = plt.subplots()
            ax.imshow(Image.fromarray(new_image_map['image'][i][0]).resize((self.results_size, self.results_size)), interpolation='nearest')
            ax.set_xticklabels([])
            ax.axes.get_xaxis().set_visible(False)
            ax.set_yticklabels([])
            ax.axes.get_yaxis().set_visible(False)
            # plt.show()
            plt.savefig(self.generated_images_path + '/{}.png'.format(new_image_map['name'][i]),bbox_inches = 'tight',pad_inches=0)
            plt.close()

    def load(self):
        self.generate_image_random()
        new_image_map = pd.DataFrame(self.image_map_data)
        self.plot_image_map(new_image_map)
        payload = {
            'product_type': 'ACCESSORIES',
            'product_name': 'Handbags',
            'product_meta': {},
        }
        product_detail_list = []
        for image_data in self.image_map_data:
            product_payload = {
                'name': image_data['name'],
                'type': 'HANDBAGS',
                'url': '/content/product-design/src/model_engine/media/handbag/images/{}'.format(image_data['name']),
                'meta': image_data['latent_vector'].tolist()
            }
            product_detail_list.append(product_payload)
        payload['product_details'] = product_detail_list
        product_design_service = service_registry.product_design_client
        return product_design_service.create_handbag_details(payload)

    def generate_image_from_z(self, z):
        images = self.generator.generate_image_from_z(z)
        return images

    def get_interpolated_vector(self, latent_vectors, proportions):
        return sum([vector * proportion for vector, proportion in zip(latent_vectors, proportions)])

    def get_image_and_associated_latent_code(self, proportion_list):
        vector_list = [
            self.image_map_data['latent_vector'][randrange(self.image_map_dimensions * self.image_map_dimensions)]
            for i in range(4)
        ]
        latent_code = self.get_interpolated_vector(vector_list, proportion_list)
        image = Image.fromarray(self.generate_image_from_z(latent_code)[0]).resize(
            (self.results_size, self.results_size)
        )
        return image, latent_code
