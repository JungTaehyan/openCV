import cv2
import numpy as np
import matplotlib.pyplot as plt


'''
dst = cv2.normalize(src, dst, alpha, beta, type_flag)
src: 정규화 이전의 데이터
dst: 정규화 이후의 데이터
alpha: 정규화 구간 1
beta: 정규화 구간 2, 구간 정규화가 아닌 경우 사용 안 함
type_flag: 정규화 알고리즘 선택 플래그 상수
'''

img = cv2.imread("../v_openCV/imgs/dog.jpg", cv2.IMREAD_GRAYSCALE)

img_f = img.astype(np.float32)
img_norm = ((img_f - img_f.min()) * (255) / (img_f.max() - img_f.min()))
img_norm = img_norm.astype(np.uint8)

img_norm2 = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])
hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 255])
hist_norm2 = cv2.calcHist([img_norm2], [0], None, [256], [0, 255])

cv2.imshow('Before', img)
cv2.imshow('Manual', img_norm)
cv2.imshow('cv2.normalizw()', img_norm2)

hists = {'Before' : hist, 'Manual':hist_norm, 'cv2.normalize()':hist_norm2}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1,3,i+1)
    plt.title(k)
    plt.plot(v)
plt.show()