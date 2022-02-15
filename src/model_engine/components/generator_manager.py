import pandas as pd
from random import randrange
from PIL import Image
from components import Generator
import matplotlib.pyplot as plt
from datetime import datetime


class GeneratorManager:
    def __init__(self, image_map_dimensions, results_size, generated_images_path):
        self.generator = Generator()
        self.image_map_dimensions = image_map_dimensions
        self.results_size = results_size
        self.image_map_data = None
        self.generated_images_path = generated_images_path

    def generate_image_random(self):
        image_map_data = []
        image_map_dimensions = self.image_map_dimensions * self.image_map_dimensions
        for i in range(image_map_dimensions):
            image, latent_code = self.generator.generate_image_random(randrange(1000))
            image_map_data.append({'id': 'pos_' + str(i), 'image': image, 'latent_vector': latent_code})

        self.image_map_data = pd.DataFrame(image_map_data)
        Image.fromarray(image[0]).resize((self.results_size, self.results_size))

    def plot_image_map(self):
        fig = plt.figure(figsize=(self.image_map_dimensions * 4.6, self.image_map_dimensions * 4.6))
        ax = [
            plt.subplot(self.image_map_dimensions, self.image_map_dimensions, i + 1)
            for i in range(self.image_map_dimensions * self.image_map_dimensions)
        ]

        i = 0
        for a in ax:
            a.imshow(
                Image.fromarray(self.image_map_data['image'][i][0]).resize((self.results_size, self.results_size)),
                interpolation='nearest',
            )
            a.set_xticklabels([])
            a.axes.get_xaxis().set_visible(False)
            a.set_yticklabels([])
            a.axes.get_yaxis().set_visible(False)

            i = i + 1

        fig.subplots_adjust(wspace=0, hspace=0)
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.savefig(
            '{}handbags-fakes-{}.png'.format(self.generated_images_path, str(datetime.utcnow())),
            bbox_inches='tight',
            pad_inches=0,
        )

    def load(self):
        self.generate_image_random()
        self.plot_image_map()
        return self.image_map_data

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
