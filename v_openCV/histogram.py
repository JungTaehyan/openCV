import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread("../v_openCV/imgs/dog.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("../v_openCV/imgs/dog.jpg")
cv2.imshow('img', img)

# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist)

# print("hist.shape: ", hist.shape)
# print("hist.sum(): ", hist.sum(), "img.shape: ", img.shape)
# plt.show()

channels = cv2.split(img) # 색(B,G,R)을 따로 나누어줌, 색깔별로 나누어서 저장도 가능함
colors = ('b', 'g', 'r')
for (ch, color) in zip (channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
plt.show()