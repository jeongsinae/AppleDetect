import cv2 
import numpy as np 

img = cv2.imread('C:/users/aaa/Desktop/mask/1.png') # 이미지 불러오기 
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 이미지 그레이 전환 

ret, thresh = cv2.threshold(imgray, 0, 255, 0) # 흑과 백으로 임계(threshold) 분할 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # contour(외곽선)를 찾아냄.(연속된 좌표점) 

cv2.drawContours(img, contours, -1, (0, 255, 0), 1) # contour(외곽선)을 그림, 초록색(0 255 0), 두께 2로 
cnt = contours[0] # cnt변수에 Contour[0]에 있는 2차원 연속된 좌표를 넣음. 

# 윤곽(convex)정보 휙득 
hull = cv2.convexHull(cnt, returnPoints=False) 

defects = cv2.convexityDefects(cnt, hull) 

print(cnt.shape)

'''
for i in range(defects.shape[0]): 
    s, e, f, d = defects[i, 0] 
    print(s,e,f,d)
    start = tuple(cnt[s][0]) 
    end = tuple(cnt[e][0]) 
    #far = tuple(cnt[f][0]) # 바깥 최 외곽선을 이은 line 표시 (파랑색) 
    #cv2.line(img, start, end, [255, 0, 0], 2) # 내부의 꼭지점에 좌표점 표시 (빨간색) 
    #cv2.circle(img, far, 5, [0, 0, 255], -1) 
'''


cv2.imshow('img', img) 

cv2.waitKey(0) 
cv2.destroyAllWindows()

