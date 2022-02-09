from lib.stylegan2 import pretrained_networks
from lib.stylegan2 import dnnlib
from lib.stylegan2.dnnlib import tflib
from server_config import generator_pickle
import numpy as np


class Generator:
    def __init__(self):
        self._G, self._D, self.Gs = pretrained_networks.load_networks(generator_pickle['handbags'])
        self.Gs_kwargs = dnnlib.EasyDict()
        self.noise_vars = [var for name, var in self.Gs.components.synthesis.vars.items() if name.startswith('noise')]
        self.Gs_kwargs.output_transform = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        self.Gs_kwargs.randomize_noise = False
        return self.Gs, self.noise_vars, self.Gs_kwargs

    # Generate images given a random seed (Integer)
    def generate_image_random(self, rand_seed):
        rnd = np.random.RandomState(rand_seed)
        z = rnd.randn(1, *self.Gs.input_shape[1:])
        tflib.set_vars({var: rnd.randn(*var.shape.as_list()) for var in self.noise_vars})
        images = self.Gs.run(z, None, **self.Gs_kwargs)
        return images, z

    # Generate images given a latent code ( vector of size [1, 512] )
    def generate_image_from_z(self, z):
        images = self.Gs.run(z, None, **self.Gs_kwargs)
        return images