import aedat
from glob import glob
from pdb import set_trace as ps
import numpy as np
import os
import cv2
from tqdm import tqdm

step_size = 100000 # Window size for accumulation of events
rows, cols = 260, 346   # Defines image size in terms of pixels
data_dir = r"C:\Users\Darshana\Desktop\Data - Revision\NM\20220113\moving beads" # Location of data directory with aedat files
out_dir = 'C:\\Users\\Darshana\\Desktop\\Data - Revision\\NM\\20220113\\' # Location of where to save the generated frames

files = os.listdir(data_dir)
for file in tqdm(files):
	decoder = aedat.Decoder(os.path.join(data_dir, file))
	save_dir = os.path.join(out_dir, file.split('.')[0])
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)
	data = []
	for packet in decoder:
		if 'events' in packet:
			data.append(packet['events'])
	data = np.concatenate(data)
	start_time = data[0][0]
	last_time = data[-1][0]
	co = 0
	while start_time < last_time:
		end_time = start_time + step_size
		event_count_image = np.zeros((rows, cols, 3), dtype=np.float32)
		for i in range(len(data)):
			if data[i][0] > end_time:
				break
			if data[i][3] > 0:
				event_count_image[data[i][2], data[i][1], 2] += 1
			else:
				event_count_image[data[i][2], data[i][1], 0] += 1
		event_count_image = event_count_image * 65535 / max(np.max(event_count_image), 1e-6)
		cv2.imwrite(os.path.join(save_dir, '{:010d}'.format(co) + '.tif'), event_count_image.astype(np.uint16))
		data = data[i:]
		co += 1
		start_time = end_time


