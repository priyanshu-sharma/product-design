from extensions.utils import Singleton

class GeneratorRegistry(metaclass=Singleton):
    def __init__(self):
        super(GeneratorRegistry, self).__init__()
        self._handbag_generator = None

    @property
    def handbag_generator(self):
        from components.generator import Generator
        if self._handbag_generator is None:
            self._handbag_generator = Generator()
        return self._handbag_generator

registry = GeneratorRegistry()

from components import registry as handbag_generator_registry
from components.generator_manager import GeneratorManager
from components.interpolation_manager import InterpolationManager
from components.interpolation_type_to_manager_map import INTERPOLATION_TYPE_TO_MANAGER_MAP