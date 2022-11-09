# 행렬을 이용한 이미지 확대 및 축소 (scale_matrix.py)

import cv2
import numpy as np

img = cv2.imread('../img/photo.jpg')
height, width = img.shape[:2]

# 축소
m_small = np.float32([[0.5, 0, 0],
                       [0, 0.5,0]])  
# 2배 확대
m_big = np.float32([[2, 0, 0],
                     [0, 2, 0]])  

# 보간법 X
dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
dst2 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)))

# 보간법 O
dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)), \
                        None, cv2.INTER_AREA)
dst4 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)), \
                        None, cv2.INTER_CUBIC)

# 보간법

# 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
cv2.imshow("small INTER_AREA", dst3)
cv2.imshow("big INTER_CUBIC", dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()