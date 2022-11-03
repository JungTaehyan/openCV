import cv2

cap = cv2.VideoCapture(0) # 0번 캠에 연결
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('cam', img)
            if cv2.waitKey(1) != -1:
                break
        
        else:
            print('no frame')
            break
else:
    print("no")

cap.release()
cv2.destroyAllWindows