# AppleDetection    
자동 사과 수확을 위한 딥러닝 기반 사과 검출기의 정밀도 벤치마킹    

## Dataset 
다운로드 링크 : <https://conservancy.umn.edu/handle/11299/206575>    
+ 레이블링 된 670장 (720*1280)    
+ train : 420, test : 134, val : 134    
+ red, green

<img src="https://user-images.githubusercontent.com/49273782/168086053-09ae8960-634c-4a4c-a906-a3a41845923f.png" width="60%" height="40%"></img>
#### 기존 사과 검출 연구    

+ ResNet50을 적용한 faster R-CNN, mask R-CNN   

|Method|Backbone|AP @ IoU=.50:.05:.95|AP @ IoU=.50|
|---|---|---|---|
|Faster RCNN|ResNet50|0.438 |0.775|
|Mask RCNN|ResNet50|0.433|0.763|


## 모델 학습   
MS COCO 데이터 셋(자전거, 개, 사과 등 80여종)으로 이미 학습된 모델로 전이 학습   
+ Faster RCNN
+ YoloV5l

<img src="https://user-images.githubusercontent.com/49273782/168085824-91edbe52-0544-41fa-bee3-4b3b8c2ddcc4.png" width="60%" height="40%"></img>    

YoloV5에는 s,m,l,x 4가지 버전, s부터 x순으로 무겁고 mAP가 높은 모델   
YoloV5s와 YoloV5m은 빠르지만 사과를 찾는 갯수가 적었고 YoloV5x는 너무 느렸기에 적절한 YoloV5l 사용   

+ epoch = 300
+ batch size = 16
+ image size = 640*640


## 모델에 따른 사과 검출 결과

<img src="https://user-images.githubusercontent.com/49273782/168086106-4a91cb46-fd06-456c-9f3b-4bb27bd26b9b.png" width="40%" height="80%"></img>    
<img src="https://user-images.githubusercontent.com/49273782/168086258-9b2a1226-0b07-4fd3-8433-dd2767a9152e.png" width="40%" height="40%"></img>   



+ green : ground truth
+ red : predict

#### 모델에 따른 검출 성능 비교
|Method|Pecision|Recall|F1-Score|
|---|---|---|---|
| Faster RCNN  | 0.937 |  0.48 |  0.634 |
| YoloV5l |  0.872  | 0.57  |  0.689 |

#### 모델에 따른 AP 비교
| Method | AP @ IoU=.50:.05:.95 | AP @ IoU=.50  | AP @ IoU=.70  |
|---|---|---|---|
| Faster RCNN  | 0.389 |  0.79 |  0.482 |
| YoloV5l |  0.407  | 0.822  |  0.52 |

## 정밀도 향상 실험
+ epoch = 300
+ batch size = 16
+ image size = 1280*1280

로봇은 사과를 한 번에 한 개씩 따기 때문에 재현율보다 정밀도가 중요   
YOLOv5l 모델의 정밀도를 높이기 위한 추가 실험을 진행   

#### 임계치에 따른 검출 성능 비교
| Confidence | Precision @ IoU=.50 | Recall @ IoU=.50  | AP @ IoU=.50  |
|---|---|---|---|
| 85 | 1.000 |  0.504 |  1.000 |
| 80 |  0.998  | 0.499  |  0.996 |
| 70 |  0.992  | 0.494  |  0.964 |
| 60 |  0.983  | 0.487  |  0.912 |
| 50 |  0.976  | 0.48  |  0.876 |
| 0(전체) |  0.959  | 0.515  |  0.874 |

#### 임계치에 따른 수확 가능 사과 개수
| Confidence | Apple Sum | Tree Sum  | Avg  |
|---|---|---|---|
| 85 | 136 |  52 |  2.615 |
| 80 |  1430  | 134 |  10.6716 |
| 70 |  3688  | 134 |  27.5223 |
| 60 |  4852  | 134 |  36.2089 |
| 50 |  5431  | 134 |  40.5298 |
| 0(전체) |  5726  | 134 |  42.7313 |

## 결과 및 고찰
1. 사과 검출기를 수확 로봇에 적용시키려면 모델의 정밀도가 높아야함
2. 모델이 사과라고 예측하였지만 예측한 결과가 실제로는 사과가 아니라면 문제
3. 실제 사과를 얼마나 많이 찾는지에 대한 재현율보다 모델이 예측한 결과가 얼마나 정확한지에 대한 정밀도 지표가 더 중요
4. 현장에서 빠르른 검출을 위해 모델의 속도가 빨라야 함
5. 정밀도를 높이기 위해 모델이 해당 물체가 사과라고 예측을 했더라도 신뢰도가 임계치를 넘지 않으면 해당 결과를 사과라고 판단하지 않음
6. 해당 연구의 후속 연구로 MinneApple 데이터 셋 이외의 데이터에 적용하는 일이 있음
