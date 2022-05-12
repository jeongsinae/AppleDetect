import numpy as np
from mean_average_precision import MetricBuilder
import os


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
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    topk='top5'
    gt_lists = []
    gt_path = f"C:/Users/aaa/Documents/GitHub/MinneApple/Locations/for_get_AP_yx/ground-truth/"
    gt_list = os.listdir(gt_path)

    for line in gt_list:

        with open(gt_path + line, 'r') as fin:
            data = fin.readlines()

        for i in range(len(data)):
            data[i] = data[i].split()
            gt = gt_point(int(data[i][1]), int(data[i][2]), int(data[i][3]), int(data[i][4]))
            gt_lists.append(gt)
    gt_lists = np.array(gt_lists)

    pred_lists = []
    pred_path = f"C:/Users/aaa/Documents/GitHub/MinneApple/Locations/TopK/rcnn-k/pred-rcnnk/{topk}/"
    pred_list = os.listdir(pred_path)

    for line in pred_list:

        with open(pred_path + line, 'r') as fout:
            data = fout.readlines()

        for i in range(len(data)):  # data=k개수
            data[i] = data[i].split()
            preds = preds_point(int(data[i][2]), int(data[i][3]), int(data[i][4]), int(data[i][5]), float(data[i][1]))
            pred_lists.append(preds)
    pred_lists = np.array(pred_lists)

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

    fin.close()
    fout.close()
