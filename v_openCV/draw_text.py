import cv2

# cv2.putText(img, text, org(위치 좌표), font, fontScale글꼴크기, color, thickness, lineType)

img = cv2.imread("../v_openCV/imgs/whight.jpg")

cv2.putText(img, "Happy", (300, 300), cv2.FONT_HERSHEY_PLAIN, 5, (150, 50, 30), 1)

if img is not None:
    cv2.imshow("text", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("no imgs")