import os
import glob
import cv2

DATA_DIR = "/home/daleas@ads.iu.edu/Pytorch-VAE/ship_data/"
img_list = glob.glob(os.path.join(DATA_DIR, "*.png"))
labels_out = []

for item in img_list:
    im = cv2.imread(item)

    print(os.path.split(item)[-1], im.shape)
