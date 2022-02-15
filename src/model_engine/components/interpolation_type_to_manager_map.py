from enums import InterpolationType
from components import InterpolationManager


INTERPOLATION_TYPE_TO_MANAGER_MAP = {
    InterpolationType.LINEAR: InterpolationManager().linear_interpolate,
    InterpolationType.ADD_CONSTANT: InterpolationManager().constant_interpolate,
}
