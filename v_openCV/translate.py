import cv2
import numpy as np

img = cv2.imread("../v_openCV/imgs/photo.jpg")
rows, cols = img.shape[0:2]
# print(rows)
# print(cols)
# print(img)
# print(np.shape(img)) -> (1080, 1440, 3) -> 1080은 y축, 1440은 x축, 3은 BGR을 나타냄

dx, dy = 200, 100  # 픽셀 단위

mtrx = np.float32([[1, 0, dx], 
                   [0, 1, dy]])

dst = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy))

dst2 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, \
                                cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))

dst3 = cv2.warpAffine(img, mtrx, (cols+dx, rows+dy), None, \
                                cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('original', img)
cv2.imshow('trans',dst)
cv2.imshow('BORDER_CONSTATNT', dst2)
cv2.imshow('BORDER_FEFLECT', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()