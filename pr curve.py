import numpy as np
import matplotlib.pyplot as plt

y_true = np.array([1,1,1,1,1,1,1,1,1,1,1])
y_scores = np.array([1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0 ])

def get_recall(y_true,y_scores,threshold):
    predict_positive_num = len(y_scores[y_scores >= threshold])
    tp = len( [x for x in y_true[:predict_positive_num] if x == 1] )
    ground_truth  = len(y_true[y_true==1])
    recall = tp / ground_truth
    return recall

def get_precision(y_true,y_scores,threshold):
    predict_positive_num = len(y_scores[y_scores >= threshold])
    tp = len( [x for x in y_true[:predict_positive_num] if x == 1] )
    fp = len( [x for x in y_true[:predict_positive_num] if x == 0] )
    precision = tp / (tp + fp) 
    return precision 

def recall_precision_plot(y_true, y_scores):
    recall, precision = [] , []

    for _ in y_scores: # y_scores 를 thresholds 처럼 사용했음
        recall.append(get_recall(y_true, y_scores, _ ))
        precision.append(get_precision(y_true,y_scores,_))

    fig = plt.figure(figsize=(9, 6))

    #3d container
    ax = plt.axes(projection = '3d')
    #3d scatter plot
    ax.plot3D(recall, y_scores, precision)
    ax.scatter3D(recall,y_scores,precision)
    #give labels
    ax.set_xlabel('Recall')
    ax.set_ylabel('Thresholds')
    ax.set_zlabel('Precision')
    ax.set_title('Precision-Recall Curve 3D')  
    plt.show()
    
    fig = plt.figure(figsize = (9,6))
    plt.plot(recall, precision)
    plt.scatter(recall,precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve 2D')
    plt.show()
    
recall_precision_plot(y_true,y_scores)