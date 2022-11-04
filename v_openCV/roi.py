import cv2
import numpy as np

img = cv2.imread("../v_openCV/imgs/dog.jpg")
# 좌표는 윗줄을 기준으로 적용됨!!
x = 600; y = 520; w = 50; h = 50
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,0,255))
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()