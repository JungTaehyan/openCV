import cv2

video_file = "../v_openCV/videos/dog.mp4" # 영상 파일 경로

cap = cv2.VideoCapture(video_file) # 영상 캡쳐 객체
if cap.isOpened(): # 영상 객체 초기화, 주로 True/Fals로 반환됨.
    while True:
        ret, img = cap.read() # 다음 프레임을 읽는 무한루프
        if ret:
            cv2.imshow(video_file, img) # 화면에 표시
            cv2.waitKey(25) # 25ms 지연 (40fps으로 가정)
        else: #다음 프레임을 읽을 수 없을때
            break
else:
    print("can't open video.") # 캡쳐 객체 초기화 실패
cap.release() #캡쳐 자원 반납
cv2.destroyAllWindows()