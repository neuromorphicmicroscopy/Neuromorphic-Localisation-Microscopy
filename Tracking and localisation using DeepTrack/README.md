### deeptracknew.py
•	deeptrack.py(https://github.com/softmatterlab/DeepTrack) is a python based deep learning algorithm developed by Helgadottir et al., 2019. deeptracknew.py incorporates a few minor modifications to the original deeptrack.py code as required for analysis of images generated from neuromorphic data. The following pipelines and codes have been created using functions defined by DeepTrack. The following link and paper have a more detailed overview of DeepTrack:
  o	https://github.com/softmatterlab/DeepTrack <br/>
  o	Helgadottir, S., Argun, A. & Volpe, G. Digital video microscopy enhanced by deep learning. Optica6, 506-513, doi:10.1364/OPTICA.6.000506 (2019). <br/>

### beadtracksim.py
•	beadtracksim.py is an algorithm that uses DeepTrack's image_generator function to simulate images of varying image parameters, create and train a neural network of user defined sizes, and to test the trained neural network on simulated particles. Each of these processes are carried out in separate cells as follows:
•	The first cell is used to generate simulation images of particles. The image parameters for generating simulated particles are defined by DeepTrack's function get_image_parameters that has been modified to suite the required simulations. The algorithm generates simulated particle images using the Bessel function from user defined distributions for image parameters like particle radii, particle intensity, Bessel function order, background level, signal to noise ratio, ellipticity of the particle, and gradients, all in terms of pixel values. The algorithm also allows for multiple particles to be simulated in a single image, and define the size of the image generated( in pixels).
•	The second cell is used to define the architecture of the neural network as follows: <br/>
  &emsp;o	**input_shape**: Enter the shape of the input data to the neural network. <br/>
  &emsp;o	**conv_layers_dimensions**: Enter the number and size of the convolutional layers required in the network. <br/>
  &emsp;o	**dense_layers_dimensions**: Enter the number and size of the dense layers needed in the network. <br/>
  &emsp;o	create_deep_learning_network is a DeepTrack function that is used to create a convoluted neural network of given dimensions and architecture. <br/>
•	The third cell is used to train the neural network that was created by user defined parameters. The inputs in this cell are: <br/>
  &emsp;o	**sample_sizes**: Enter the size of the batch of images to be generated. <br/>
  &emsp;o	**iteration_numbers**: Enter the number of iterations each batch has to go through. <br/>
  &emsp;o	train_deep__learning_network is a DeepTrack function that uses image_generator and training parameters to train the neural network created. <br/>
•	The fourth cell uses the image_generator function to generate simulated function to test the trained neural network for its accuracy. <br/>
•	The final cell is used to save the trained neural network. <br/>

### snrseries.py
•	snrseries.py is an algorithm that uses DeepTrack's image_generator function to simulate images of varying image parameters. The parameters are defined by DeepTrack's function get_image_parameters that has been modified to suite the required simulations. The algorithm generates simulated particle images using the Bessel function from user defined distributions for image parameters like particle radii, particle intensity, Bessel function order, background level, signal to noise ratio, ellipticity of the particle, and gradients, all in terms of pixel values. The algorithm also allows for multiple particles to be simulated in a single image, and define the size of the image. A trained neural network can be loaded and used to predict the centroids of simulated particles to test the prediction respect to changing signal to noise ratio. This code can also be edited to train the neural network using the simulated particle images.

### beadtrack.py
•	beadtrack.py is a pipeline using functions from DeepTrack to load experimental images/videos of particles, and have a trained neural network predict the centroids of all the particles in the input data. The pipeline has been divided into cells defining different steps. 
•	The first cell is used to preprocess and upload the experimental data either in form of image or video, and define the scanning box parameters using the variables:<br/>
  &emsp;o	video_file_name: Enter the name of the image or video file with the extension.<br/>
  &emsp;o	box_half_size: Enter the size of the scanning box window that scans each frame.<br/>
  &emsp;o	box_scanning_size: Enter the step size for the scanning window.<br/>
  &emsp;o	frame_enhance and frame_normalise: Enter values to optimise and adjust pixel values for preprocessing.<br/>
•	The second cell is used to load a pre-trained convoluted neural network:<br/>
  &emsp;o	saved_network_file_name: Enter the name of the trained neural network.<br/>
  o	network: Used to load the neural network for localisation.<br/>
•	The third cell uses DeepTrack's track_video function to track particles by scanning each frame of the video by the predefined scanning box or window.<br/>
•	The fourth cell defines filter parameters to average multiple localisations of the same particle(particle_maximum_interdistance), and radial threshold to localise a particle for a scanning box(particle_radial_distance_threshold).<br/>
•	The fifth cell uses DeepTrack's plot_scanning_boxes function to display particular scanning boxes and the localisation in each case. The scanning boxes to be displayed are defined by the variables frames_to_be_shown, rows_to_be_shown, and columns_to_be_shown.<br/>
•	The sixth cell uses DeepTrack's show_tracked_frames function to display entire frames and all the localisation in each case. The frames to be displayed are defined by the variables number_frames_to_be_shown, and frame.<br/>


### References
•	Helgadottir, S., Argun, A. & Volpe, G. Digital video microscopy enhanced by deep learning. Optica6, 506-513, doi:10.1364/OPTICA.6.000506 (2019).

