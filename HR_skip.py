import os
import shutil
import numpy as np

orig_folder_path = '/nas-ctm01/datasets/public/Avenue/dataset/gt/test_frame_mask/'
destination_folder_path = '/nas-ctm01/datasets/public/Avenue/dataset/gt/test_frame_mask_hr/'

if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

for filename in os.listdir(orig_folder_path):
    source_file = os.path.join(orig_folder_path, filename)
    destination_file = os.path.join(destination_folder_path, filename)

    shutil.copy2(source_file, destination_file)


video_list = ["01", "02", "03", "06", "16"]

for video in video_list:
    data = np.load(orig_folder_path + '01_{}.npy'.format(video))

    hr_skip = [(1, x) for x in range(75, 121)] + [(1, x) for x in range(390, 437)] + [(1, x) for x in range(864, 911)] + \
            [(1, x) for x in range(931, 1001)] + [(2, x) for x in range(272, 320)] + [(2, x) for x in range(723, 764)] + \
            [(3, x) for x in range(293, 341)] + [(6, x) for x in range(561, 625)] + [(6, x) for x in range(814, 1007)] + \
            [(16, x) for x in range(728, 740)]


    for i in range(len(data)):
        if data[i] == 1 and (int(video[1:]), i) in hr_skip:
            data[i] = 0

    np.save(destination_folder_path + '01_{}.npy'.format(video), data)
