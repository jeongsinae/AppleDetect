import numpy as np
import cv2, os

img_path = "C:/MinneApple/detection/detection/test/images"
save_path = "C:/MinneApple/gt_yolo_box" # option
gt_path = "C:/MinneApple/mAP-master/mAP-master/input"
yolo_path = "C:/Users/aaa/Documents/GitHub/MinneApple/Locations/for_get_AP_yx/yolov5x-1028"

# color
blue = (255,0,0) # yolov5l
green = (0,255,0) # gt
red = (0,0,255) # predict rcnn

img_list = os.listdir(img_path)
predict_list = os.listdir(yolo_path) # option


# rcnn-predict bounding box
for i in range(len(img_list)):
    img_name = img_path+'/'+img_list[i]
    save_name = save_path+'/'+img_list[i]

    origin_img = cv2.imread(img_name, cv2.IMREAD_COLOR)
    save_img = cv2.imwrite(save_name,origin_img) # 이미지 복사

    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    pred_file_name = predict_list[i]
    loc = open(yolo_path+'/'+pred_file_name,"r") #option
    lines = loc.readlines()
    k=1
    for line in lines:
        img = cv2.imread(save_name, cv2.IMREAD_COLOR)
        l = line.split(' ')
        name=l[0]
        confidence=l[1]
        ymin = int(l[3])
        xmin = int(l[2])
        ymax = int(l[5])
        xmax = int(l[4])
        image = cv2.rectangle(np.array(img), (ymin, xmin), (ymax, xmax), blue, 3)
        image = cv2.putText(image,confidence,(ymin-10, xmin-10),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        image = cv2.putText(image,name,(ymin-10, xmin-30),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        image = cv2.putText(image,str(k),(ymin-20, xmin-20),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        k+=1
        cv2.imwrite(save_name,image)
        cv2.waitKey(0)
