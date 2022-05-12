import numpy as np
from collections import namedtuple
import cv2
import glob
import os

path = 'C:/Users/aaa/Desktop/9th Apple/yolo/'
save_path='C:/Users/aaa/Desktop/9th Apple/d/'
file_list = os.listdir(path)

for pred_line in file_list:
    pred_file = open(path+pred_line, 'r')
    line = pred_file.readlines()
    new=""
    new_file = open(save_path+pred_line, 'w')

    for i in line:
        if(str(i).find('apple')):
            line=i.replace(i,"")
    print(line)

    l=line.split(' ')
    new_file.write(str(l))

new_file.close()
pred_file.close()





'''
import numpy as np
from collections import namedtuple
import cv2
import glob
import os

path = "C:/MinneApple/mAP-master/mAP-master/input/detection-results/"
save_path="C:/MinneApple/yolov5x_1280_top15/"
file_list = os.listdir(path)


for pred_line in file_list:
    
    pred_file = open(path+pred_line, 'r')
    line = pred_file.readlines()
    new=""
    

    for i in line:
        if(str(i).find('apple')):
            line=i.replace(i, "6")
            
    name = str(pred_line).rstrip('\n').split(' ')
    name=' '.join(name)


    with open(save_path+pred_line , 'a') as f:
        f.write(f'{pred_file}\n')
     
pred_file.close()
f.close()
'''