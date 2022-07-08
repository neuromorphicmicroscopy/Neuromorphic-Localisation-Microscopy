#%%
import deeptracknew
import numpy as np
import cv2
### Define the video file to be tracked
video_file_name = 'nmtrackedon1.tif'
### Define the number of frames to be tracked
number_frames_to_be_tracked =5
### Define the size of the box to be scanned over the frames
box_half_size = 15
### Define the scanning step over the frame
box_scanning_step = 3
### Preprocess the images
frame_normalize = 0
frame_enhance = 5
#%%
### Load the pretrained network
saved_network_file_name = 'neuromorph_psf_new Network 2020-07-25-172716 C-16-32-64 D-32-32 training-8x5001-32x4001-128x2501-512x1001-1024x101.h5'
network = deeptracknew.load(saved_network_file_name)

#%%
### Track the video`
(number_tracked_frames, frames, predicted_positions_wrt_frame, predicted_positions_wrt_box, boxes_all)=deeptracknew.track_video(
    video_file_name,
    network,
    number_frames_to_be_tracked=2,
    box_half_size=25,
    box_scanning_step=3,
    frame_normalize=0,
    frame_enhance=3)
number_frames_to_be_shown=2
#number_frames_to_be_tracked, frames, predicted_positions_wrt_frame, predicted_positions_wrt_box, boxes_all

    # Release the video


    
#%%
### Define minimum radial distance from the center of the scanning boxes
import matplotlib 
particle_radial_distance_threshold =2
### Define the minumum distance between predicted scanning points for them belonging to 
particle_maximum_interdistance =4
#%%
### Define frames, rows and columns of the samples to be shown
frames_to_be_shown = range(1)
rows_to_be_shown = range(15,20)
columns_to_be_shown = range(5,10)
### Show boxes
deeptracknew.plot_tracked_scanning_boxes(
frames_to_be_shown,
rows_to_be_shown,
columns_to_be_shown,
boxes_all,
predicted_positions_wrt_box)

 #%%

#%%
### Define frames, rows and columns of the samples to be shown
(particle_positions, particle_centroids)=deeptracknew.show_tracked_frames(
particle_radial_distance_threshold,
particle_maximum_interdistance,
number_frames_to_be_shown,
frames,
predicted_positions_wrt_frame)

#%%
import centroidlogfn
centroidlogfn.log_centroids(particle_centroids, number_frames_to_be_shown)
#%%
#import projectionplot
#projectionplot.plot_in_new_image(particle_centroids, number_frames_to_be_shown)
##%%
#import scatter_plotfn
#scatter_plotfn.scatter_plot(particle_centroids, number_frames_to_be_shown)

#%%
import limitarrays
(xupper,xlower,yupper,ylower)=limitarrays.get_array()

import centroidlogfn
#(x_up_lim,x_low_lim,y_up_lim,y_low_lim)=centroidlogfn.get_limits(1,2,particle_centroids)
centroidlogfn.log_single_centroids(particle_centroids, number_frames_to_be_shown,xupper,xlower,yupper,ylower)