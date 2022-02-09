class InterpolationManager():
    def __init__(self):
        pass

    def linear_interpolate(self, interpolation_dict):
        latent_code_1 = interpolation_dict['latent_code_1']
        latent_code_2 = interpolation_dict['latent_code_2']
        alpha = interpolation_dict['alpha']
        return latent_code_1 * (1 - alpha) + latent_code_2 * alpha
    
    def constant_interpolate(self, interpolation_dict):
        latent_code_1 = interpolation_dict['latent_code_1']
        latent_code_2 = interpolation_dict['latent_code_2']
        alpha = interpolation_dict['alpha']
        constant = interpolation_dict['constant']
        return ((latent_code_1 * (1 - alpha) + latent_code_2 * alpha) + constant)
