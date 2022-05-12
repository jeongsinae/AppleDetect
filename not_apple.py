# -*- coding: utf-8 -*-
import cv2
import torch
from PIL import Image
import glob
import numpy as np
import os
import pandas as pd

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5l')

'''
# Images
img1 = Image.open('C:/MinneApple/detection.tar/detection/train/images/*')  # PIL image
#img2 = cv2.imread('C:/MinneApple/detection/detection/test/images/dataset1_front_61.png')[:, :, ::-1]  # OpenCV image (BGR to RGB)
imgs = [img1]  # batch of images
'''

ROOT_PATH = 'C:/Users/aaa/Desktop/9th Apple/img'

for fname in os.listdir(ROOT_PATH):
    # Inference
    images = np.array(Image.open(os.path.join(ROOT_PATH, fname)))
    results = model(images,size=1280)  # includes NMS
    
    # Results
    #results.print()  
    #results.show()  # or .show()
    
    results.xyxy[0]  # img1 predictions (tensor)
    df=results.pandas().xyxy[0]  # img1 predictions (pandas)
    
    for i in range(len(df)):

        x1=round(df.xmin).astype(int)
        y1=round(df.ymin).astype(int)
        x2=round(df.xmax).astype(int)
        y2=round(df.ymax).astype(int)
        name=df.name
        confi=df.confidence
        
    
        SAVE_FILE = 'C:/Users/aaa/Desktop/9th Apple/yolov5l-1280.txt'
        with open(SAVE_FILE, 'a') as f:
            f.write(f'{fname} {name[i]} {confi[i]:.6f} {x1.values[i]} {y1.values[i]} {x2.values[i]} {y2.values[i]}\n')

        
