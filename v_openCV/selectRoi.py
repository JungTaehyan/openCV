# selectROI로 관심영역 지정 및 표시, 저장 (roi_select_img.py)
'''
ret = cv2.selectROI(win_name, img, showCrossHair=True, fromCenter=False)

win_name: 관심영역을 표시할 창의 이름
img: 관심영역을 표시할 이미지
showCrossHair: 선택 영역 중심에 십자 모양 표시 여부
fromCenter: 마우스 시작 지점을 영역의 중심으로 지정
ret: 선택한 영역의 좌표와 크기 (x, y, w, h); 선택을 취소하면 모두 0으로 지정됨
'''

import cv2
import numpy as np

img = cv2.imread('../v_openCV/imgs/dog.jpg')

x,y,w,h	= cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped', 0, 0) # 새창을 화면 좌측 상단에 이동
    cv2.imwrite('./imgs/cropped2.jpg', roi)   # ROI 영역만 파일로 저장

cv2.waitKey(0)
cv2.destroyAllWindows()