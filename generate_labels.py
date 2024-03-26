import os
import glob
import csv

"""
Given a list of ships_data files, generates the class labels based on how the images are named
"""

DATA_DIR = "/home/daleas@ads.iu.edu/Pytorch-VAE/ship_data/"

# CLASS_MAP={0:'background',
#            1: 'RW',
#            2: 'VW',
#            3: 'RW_patch_VW_bg',
#            4: 'VW_patch_RW_bg',
#            5: 'noise_RW_bg',
#            6: 'noise_VW_bg'
#            }

# Get list of all *.pngs in the directory

img_list = glob.glob(os.path.join(DATA_DIR, "*.png"))
labels_out = []

with open(os.path.join(DATA_DIR, 'labels.csv'), 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=',', escapechar=' ')

    for item in img_list:
        img_name = os.path.split(item)[-1]
        bp = 0
        
        if img_name[:3] == 'set' and img_name[-5] == 'n':
            class_id ='6'
        elif img_name[:3] == 'set' and img_name[-5] == 'p':
            class_id ='4'
        elif img_name[:3] == 'set':
            class_id ='2'
        elif img_name[-5] == 'n':
            class_id ='5'
        elif img_name[-5] == 'p':
            class_id ='3'
        else:
            class_id ='1'

        wr.writerow([img_name,class_id])

print('Done')
