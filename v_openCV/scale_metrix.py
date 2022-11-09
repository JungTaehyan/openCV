# 행렬을 이용한 이미지 확대 및 축소 (scale_matrix.py)

import cv2
import numpy as np

img = cv2.imread('../img/photo.jpg')
height, width = img.shape[:2]


# 변환 행렬 사용
# # 축소
# m_small = np.float32([[0.5, 0, 0],
#                        [0, 0.5,0]])  
# # 2배 확대
# m_big = np.float32([[2, 0, 0],
#                      [0, 2, 0]])  

# # 보간법 X
# dst1 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)))
# dst2 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)))

# # 보간법 O
# dst3 = cv2.warpAffine(img, m_small, (int(height*0.5), int(width*0.5)), \
#                         None, cv2.INTER_AREA)
# dst4 = cv2.warpAffine(img, m_big, (int(height*2), int(width*2)), \
#                         None, cv2.INTER_CUBIC)


#  변환 행렬 사용 X
# 크기 지정으로 축소
#dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)),None, 0, 0, cv2.INTER_AREA)
dst1 = cv2.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv2.INTER_AREA)

# 배율 지정으로 확대
dst2 = cv2.resize(img, None,  None, 2, 2, cv2.INTER_CUBIC)

# 결과 출력
cv2.imshow("original", img)
cv2.imshow("small", dst1)
cv2.imshow("big", dst2)
# cv2.imshow("small INTER_AREA", dst3)
# cv2.imshow("big INTER_CUBIC", dst4)
cv2.waitKey(0)
cv2.destroyAllWindows()