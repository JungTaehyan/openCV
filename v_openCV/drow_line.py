import cv2

img =cv2.imread('../v_openCV/imgs/whight.jpg')
# cv2.line(img, start, end, color(BRG), thickness(픽셀단위), line Type)

cv2.line(img, (50, 50), (150, 150), (255,0,0))
cv2.line(img, (100, 350), (400, 400), (0,0,255), 20, cv2.LINE_4)
cv2.line(img, (100, 450), (400, 500), (0,0,255), 20, cv2.LINE_AA)
if img is not None:
    cv2.imshow("line", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("no imgs")