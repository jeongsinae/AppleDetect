import numpy as np
from mean_average_precision import MetricBuilder
import os
import json

x_list=[]
y_list=[]
width_list=[]
height_list=[]
gt_lists=[]

with open('C:/Users/aaa/Desktop/9th Apple/1~10/via_project_8Sep2021_12h24m_json.json', 'r') as f:

    json_data = json.load(f)
    file_name=list(json_data.keys())
    print(file_name)
    
    for i in range(12):
        print(file_name[i])
        name=file_name[i]
        for k in json_data[name]["regions"]: 
            x=k['shape_attributes']['x']
            #print(x)
            x_list.append(x)
        for k in json_data[name]["regions"]: 
            y=k['shape_attributes']['y']
            #print(y)
            y_list.append(y)
        for k in json_data[name]["regions"]: 
            y=k['shape_attributes']['width']
            #print(y)
            width_list.append(y)
        for k in json_data[name]["regions"]: 
            y=k['shape_attributes']['height']
            #print(y)
            height_list.append(y)


def gt_point(x1, y1, x2, y2):
    array = []
    for j in range(1):
        array.append(x1)
        array.append(y1)
        array.append(x2)
        array.append(y2)
        array.append(0)
        array.append(0)
        array.append(0)

    return array


def preds_point(x1, y1, x2, y2, confi):
    array = []
    for j in range(1):
        array.append(x1)
        array.append(y1)
        array.append(x2)
        array.append(y2)
        array.append(0)
        array.append(confi)

    return array


if __name__ == '__main__':
        
    topk='top5'
    
    pred_lists = []
    pred_path = f"C:/Users/aaa/Documents/GitHub/MinneApple/Locations/TopK/yolo-k/onlyapple-yolok/{topk}/"
    pred_list = os.listdir(pred_path)

    for line in pred_list:

        with open(pred_path + line, 'r') as fout:
            data = fout.readlines()

        for i in range(len(data)):  # data=k개수
            data[i] = data[i].split()
            preds = preds_point(int(data[i][2]), int(data[i][3]), int(data[i][4]), int(data[i][5]), float(data[i][1]))
            pred_lists.append(preds)
    pred_lists = np.array(pred_lists)
    print("pred: ",pred_lists)
    
    
    for i in range(len(x_list)):
        gt=gt_point(x_list[i],y_list[i],width_list[i],height_list[i])
        gt_lists.append(gt)
        
    gt_lists = np.array(gt_lists)
    print("gt: ",gt_lists)

    '''    
    # [xmin, ymin, xmax, ymax, class_id, difficult, crowd]
    gt = np.array([
        [526, 601, 555, 635, 0, 0, 0],
        [114, 651, 146, 683, 0, 0, 0],
        [285, 421, 316, 449, 0, 0, 0],
        [55, 552 ,89, 584, 0, 0, 0],
        [494, 748, 518, 770, 0, 0, 0]
    ])
    
    # [xmin, ymin, xmax, ymax, class_id, confidence]
    preds = np.array([
        [526, 600, 558, 634, 0, 0.735840 ],
        [112, 650, 147, 684, 0, 0.712402 ],
        [286, 422, 318, 450, 0, 0.606445 ],
        [53, 550, 92, 586, 0, 0.597168 ],
        [494, 746, 518, 772, 0, 0.565430 ]
    ])
    '''
    # print list of available metrics
    print(MetricBuilder.get_metrics_list())

    # create metric_fn
    metric_fn = MetricBuilder.build_evaluation_metric("map_2d", async_mode=True, num_classes=1)

    # add some samples to evaluation
    # for i in range(10):
    metric_fn.add(pred_lists, gt_lists)

    # compute PASCAL VOC metric
    print(f"VOC PASCAL mAP: {metric_fn.value(iou_thresholds=0.5, recall_thresholds=np.arange(0., 1.1, 0.1))['mAP']}")

    # compute PASCAL VOC metric at the all points
    print(f"VOC PASCAL mAP in all points: {metric_fn.value(iou_thresholds=0.5)['mAP']}")

    # compute metric COCO metric
    print(
        f"COCO mAP: {metric_fn.value(iou_thresholds=np.arange(0.5, 1.0, 0.05), recall_thresholds=np.arange(0., 1.01, 0.01), mpolicy='soft')['mAP']}")


    fout.close()

