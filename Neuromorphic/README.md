### frame_reconstruct.py
•	frame_reconstruct.py is an algorithm to integrate neuromorphic events over user defined timescales into a series of *.tif images to achieve varied temporal sampling. The input to this function is a neuromorphic events data file with *.aedat4file extension.  
•	The following variables are the inputs to the algorithm: <br/>
&emsp;o	**data_dir**: Enter the directory where the neuromorphic data is stored in the .aedat4file format.<br/>
&emsp;o	**out_dir**: Enter the directory where the tiff images must be saved.<br/>
&emsp;o	**step_size**: Enter the timescale or window over which the accumulation or integration of event polarities must occur for each frame, thus defining the frame rate. This value should be entered in units of microseconds.<br/>
&emsp;o	**rows, cols**: Enter the size of the image in terms of number of rows of pixels(rows), and coloumns of pixels(cols).<br/>
<p align="center">![Picture1](https://user-images.githubusercontent.com/108917651/177950771-5a7c4ffd-827b-411d-be20-6b288fc40b7e.png)<p/>
<p align="center">Fig 1: Snippet of input variables<p/>

•	The code reads the *.aedat4file from the data_dir directory and generates frames by integrating the polarities over a defined timescale(step_size) for every pixel. The polarities are colour coded as green for positive polarity or ON process and red for negative polarity or OFF process. That is, for every positive polarity or ON process, the pixel value for that pixel will increase by one in the green channel, and for every negative polarity or OFF process, the pixel value of that pixel will increase by one in the red channel. This process is repeated for the duration of step_size or timescale, thereby producing an *.tif image frame of either 8-bit depth or 16 -bit(uint8 or uint16 respectively as shown in figure below) depth as defined by the user that is saved in the out_dir directory.
<p align="center">![image](https://user-images.githubusercontent.com/108917651/177950237-4a48b095-0d8c-4562-a569-a1b5fd65f7db.png)<p/> 
<p align="center">Fig 2: Snippet of choosing bit depth<p/>

### Using the given data
•	Enter the file named 100ms-300mW-NM.aedat4 to the input data directory variable data_dir
•	Enter step size as 100000
•	Enter rows, cols and 260, 346
•	Enter the desired output directory for out_dir variable
•	The result should be a string of 212 *.tif images when stacked together should resemble the given file ON-OFF-100ms-300mW.tif
•	On cropping out frames that see no particles, we are left with frames 3 to 197, and should resemble the given file ON-OFF-100ms-300mW-cropped.tif
•	Alternate frames can be stacked together to create identical copies of files ON.tif and OFF.tif that can be further used to localise the particles in during the ON processes and OFF processes independently.
