import numpy as np
from collections import namedtuple
import cv2
import glob

import numpy as np



# boxA -> boxGT, botB -> boxPRED
#@njit
def intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    # compute the area of intersection rectangle

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    # compute the area of both the prediction and ground-truth
    # rectangles

    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area

    iou = interArea / float(boxAArea + boxBArea - interArea)
    # return the intersection over union value

    return iou


# images = glob.glob('./minneapple/test/masks/*.png')

# gt = []
# image = glob.glob('./minneapple/test/masks/*.png')

gt_file = open("C:/MinneApple/gt.txt", 'r')
gt_lines = gt_file.readlines()

pred_file = open("C:/MinneApple/yolov5s-yx.txt", 'r')
pred_lines = pred_file.readlines()


#@njit
def solve():
    iou_sum = 0
    cnt = 0
    for gt_line in gt_lines:
        max_iou = -1e9

        boxGT_check = gt_line.rstrip('\n').split(',')[:1]

        boxGT = gt_line.rstrip('\n').split(',')[1:]
        boxGT = list(map(int, boxGT))

        for pred_line in pred_lines:
            boxPRED_check = pred_line.split(' ')[:1]

            if boxGT_check == boxPRED_check:
                boxPRED = pred_line.split(' ')[3:]
                boxPRED = list(map(int, boxPRED))
                IOU = intersection_over_union(np.array(boxGT), np.array(boxPRED))
                if IOU > 0.5:  # 겹치는 부분이 50% 이상
                    max_iou = max(max_iou, IOU)
                    # print("boxGT: ", boxGT)
                    # print("boxPRED: ", boxPRED)
                    # print("iou: ", intersection_over_union(np.array(boxGT), np.array(boxPRED)))
                    # iou_sum = iou_sum + intersection_over_union(boxGT, boxPRED)
            else:
                break

            # print("Cimplete")
        iou_sum += max_iou
        cnt = cnt + 1
        print(f'IOU of {boxGT_check} => {max_iou}')

    print(iou_sum / cnt)


solve()
