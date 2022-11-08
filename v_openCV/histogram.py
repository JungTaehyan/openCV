import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../v_openCV/imgs/dog.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

print("hist.shape: ", hist.shape)
print("hist.sum(): ", hist.sum(), "img.shape: ", img.shape)
plt.show()