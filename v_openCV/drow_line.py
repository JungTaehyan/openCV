import cv2
import numpy as np
img =cv2.imread('../v_openCV/imgs/whight.jpg')
path = "../v_openCV/imgs/test_line.jpg"
# cv2.line(img, start, end, color(BRG), thickness(픽셀단위, -1은 전체 색칠), line Type)
# cv2.rectangle(img, start, end, color, thickness, lineType)
# cv2.polylines(img, pts, isClosed, color, thickness, lineType)
# cv2.circle(img, center, radius(반지름), color, thickness, lineType) 
# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness, lineType)

# 선 그리기
cv2.line(img, (50, 50), (150, 150), (255,0,0))
cv2.line(img, (100, 350), (400, 400), (0,0,255), 20, cv2.LINE_4)
cv2.line(img, (100, 450), (400, 500), (0,0,255), 20, cv2.LINE_AA)

# 사각형 그리기
cv2.rectangle(img, (100, 50), (300, 150), (0, 0, 250), -1)
cv2.rectangle(img, (100, 50), (300, 150), (0, 250, 0), 10, cv2.LINE_8)

# 다각형 그리기
# numpy array로 좌표 생성(2원 배열을 활용해야 하기 때문)
pts1 = np.array([[450,450], [550, 550], [500, 540], [600, 640]], dtype=np.int32) # 번개모양
pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32) # 삼각형

cv2.polylines(img, [pts1], False, (255, 0, 0))# 좌표에 맞게 선그리기
cv2.polylines(img, [pts2], True, (100, 100, 100))# 좌표에 맞게 선그리기

# 원, 타원 그리기
cv2.circle(img, (400, 150), 50, (0,0,255), -1)
cv2.ellipse(img, (400, 425), (50, 75), 45, 181, 360, (255,0,0)) 

if img is not None:
    cv2.imshow("line", img)
    cv2.waitKey()
    # cv2.imwrite(path, img)
    cv2.destroyAllWindows()
else:
    print("no imgs")


# 사진을 저장했을 때 선이 그려진 사진으로 저장됨.