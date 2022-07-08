import deeptracknew
### Define image properties

from numpy.random import randint, uniform, normal, choice
from math import pi

particle_number = 4
first_particle_range = 10
other_particle_range = 25
particle_distance = 10


def get_image_parameters():
    (particles_center_x, particles_center_y) = deeptracknew.particle_positions(particle_number, first_particle_range, other_particle_range, particle_distance)
    image_parameters = {}

    image_parameters['Particle Center X List'] = particles_center_x
    image_parameters['Particle Center Y List'] = particles_center_y
    image_parameters['Particle Radius List'] = uniform(1, 3, particle_number)
    image_parameters['Particle Bessel Orders List'] = [[1, ], 
                                                       [1, ],
                                                       [1, ], 
                                                       [1, ]]
    image_parameters['Particle Intensities List'] = [[uniform(0.5, 0.7, 1), ], 
                                                     [uniform(0.5, 0.7, 1), ],
                                                     [uniform(0.5, 0.7, 1), ], 
                                                     [uniform(0.5, 0.7, 1), ]]
    image_parameters['Image Half-Size'] = 25
    image_parameters['Image Background Level'] = uniform(0,.2)
    image_parameters['Signal to Noise Ratio'] = uniform(8,10)
    image_parameters['Gradient Intensity'] = uniform(0, 0.1)
    image_parameters['Gradient Direction'] = uniform(-0.2, 0.2)#-pi to pi usually
    image_parameters['Ellipsoid Orientation'] = uniform(-pi, pi, particle_number)
    image_parameters['Ellipticity'] = uniform(1,1.3)

    return image_parameters


image_parameters_function = lambda : get_image_parameters()

### Define image generator
image_generator = lambda : deeptracknew.get_image_generator(image_parameters_function)

### Show some examples of generated images
number_of_images_to_show = 10

for image_number, image, image_parameters in image_generator():
    if image_number>=number_of_images_to_show:
        break
    
    deeptracknew.plot_sample_image(image, image_parameters)
### Load the pretrained network
saved_network_file_name = 'neuromorph_psf_new Network 2020-07-25-172716 C-16-32-64 D-32-32 training-8x5001-32x4001-128x2501-512x1001-1024x101.h5'
network = deeptracknew.load(saved_network_file_name)
#%%
##testing
number_of_predictions_to_show = 25
for image_number, image, image_parameters in image_generator():
    if image_number>=number_of_predictions_to_show:
        break
    predicted_position = deeptracknew.predict(network, image)
    deeptracknew.plot_prediction(image, image_parameters, predicted_position)