import deeptracknew
### Define image properties

from numpy.random import randint, uniform, normal, choice
from math import pi

particle_number = 4
first_particle_range = 10
other_particle_range = 25
particle_distance = 10


def get_image_parameters_optimized():
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
    image_parameters['Image Background Level'] = uniform(0,.1)
    image_parameters['Signal to Noise Ratio'] = uniform(2, 4)
    image_parameters['Gradient Intensity'] = uniform(0, 0.1)
    image_parameters['Gradient Direction'] = uniform(-0.2, 0.2)#-pi to pi usually
    image_parameters['Ellipsoid Orientation'] = uniform(-pi, pi, particle_number)
    image_parameters['Ellipticity'] = uniform(1,1.3)

    return image_parameters


image_parameters_function = lambda : get_image_parameters_optimized()

### Define image generator
image_generator = lambda : deeptracknew.get_image_generator(image_parameters_function)

### Show some examples of generated images
number_of_images_to_show = 10

for image_number, image, image_parameters in image_generator():
    if image_number>=number_of_images_to_show:
        break
    
    deeptracknew.plot_sample_image(image, image_parameters)
#%%
#%%
### Define parameters of the deep learning network
input_shape = (51, 51, 1) # Change to determine the shape of the input image [x-pixels by 
conv_layers_dimensions = (16, 32, 64) # Change to determine the number and size of convolutional 
dense_layers_dimensions = (32, 32) # Change to determine the numebr and size of dense layers
### Create deep learning network
network = deeptracknew.create_deep_learning_network(input_shape, conv_layers_dimensions, dense_layers_dimensions)### Print deep learning network summary
network.summary()
#%%
### Define parameters of the training
sample_sizes = (8, 32, 128, 512, 1024)
iteration_numbers = (5000, 4000, 2500, 1000, 500)
verbose = 1
### Training
training_history = deeptracknew.train_deep_learning_network(network, image_generator, sample_sizes,  iteration_numbers, verbose)
#%%
##testing
number_of_predictions_to_show = 100
for image_number, image, image_parameters in image_generator():
    if image_number>=number_of_predictions_to_show:
        break
    predicted_position = deeptracknew.predict(network, image)
    deeptracknew.plot_prediction(image, image_parameters, predicted_position)
#%%
    ### Prepare file name
from datetime import datetime as time
save_file_name = 'neuromorph_psf_QD Network ' + time.now().strftime('%Y-%m-%d-%H%M%S')
save_file_name += ' C'
for conv_layer_dimension in conv_layers_dimensions:
    save_file_name += '-' + str(conv_layer_dimension)
save_file_name += ' D'
for dense_layer_dimension in dense_layers_dimensions:
    save_file_name += '-' + str(dense_layer_dimension)
save_file_name += ' training'
for sample_size, iteration_number in zip(sample_sizes, iteration_numbers):
    save_file_name += '-' + str(sample_size) + 'x' + str(iteration_number)  
save_file_name += '.h5'
### Save deep learning model
import os
if not os.path.exists(save_file_name):
    network.save(save_file_name)
    print('Saved deep learning network as:')
    print(save_file_name)