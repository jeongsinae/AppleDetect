import cv2 as cv
import numpy as np
import glob


images=glob.glob('C:/MinneApple/detection/detection/train/masks/*.png')

image_list=[]

for i in images:
    im=cv.imread(i)
    image_list.append(im)

point=[]
    
    
for i in range(len(image_list)):
    #print(image_list[i])
    img_gray = cv.cvtColor(image_list[i], cv.COLOR_BGR2GRAY)
    ret, img_binary = cv.threshold(img_gray, 0, 255, 0)
    contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    print(images[i])
    
    inner_point=[]
    for j in range(4):
        inner_point.append(0)
    point.append(inner_point)
    
    for cnt in contours:

        cv.drawContours(image_list[i],[cnt],0,(255,0,0),3)
        
        x, y, w, h = cv.boundingRect(cnt)
        print(x,y,w,h)
        
        point.append([x,y,w,h])
        
        cv.rectangle(image_list[i], (x, y), (x + w, y + h), (0, 255, 0), 2)
        
print(point)
