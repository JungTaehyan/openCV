import cv2

video_file = "../v_openCV/videos/dog.mp4" # 영상 파일 경로

cap = cv2.VideoCapture(video_file) # 영상 캡쳐 객체 비디오의 레퍼런스 정보가 저장됨
# cap에는 참조 첫번째 프레임이 들어간다기 보다 참조 라인이 들어간다고 생각해야 함.
if cap.isOpened(): # 영상 객체 초기화, 주로 True/Fals로 반환됨.
    while True:
        ret, img = cap.read() # 다음 프레임을 읽는 무한루프
        if ret:
            img_1 = cv2.flip(img, 0)
            # 상하 반전(1 -> 좌우 대칭, 0 -> 상하 대칭, -1 -> 상하 좌우 대칭)
            cv2.imshow(video_file, img_1) # 화면에 표시
            cv2.waitKey(25) # 25ms(밀리세컨즈) 지연 (40fps으로 가정) 키 입력을 기다리는 대기함수
            # cv2.waitKey() -> 매개변수로 넘긴 시간 안에 키를 입력하면 소스의 다음줄로 이동.
            # 만약 지정 시간 안에 키를 입력하지 않으면 넘어가게 되어있음
            # 0:무한 대기, -1: 키가 눌리지 않을때, 아스키코드로 확인 가능
            # 예시 : if cv2.waitKey() == ord('q'): # q를 누르면 종료
            # cv2.waitKeyEX() : 특수키 사용
        else: #다음 프레임을 읽을 수 없을때
            break
else:
    print("can't open video.") # 캡쳐 객체 초기화 실패
cap.release() #캡쳐 자원 반납
cv2.destroyAllWindows()

# 비디오가 상하 반전이 되어 재생되는 문제 발견
