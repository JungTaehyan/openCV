import cv2


save_file = "../v_openCV/imgs/test1.jpg"
cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('cam', frame)
            if cv2.waitKey(1) != -1:
                cv2.imwrite(save_file, frame)
                break
        else:
            print('no frame')
            break
else:
    print('no camera')
cap.release()
cv2.destroyAllWindows()