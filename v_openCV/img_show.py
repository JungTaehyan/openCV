import cv2

img_file = "../v_openCV/imgs/4star.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img) # 읽은 이미지를 화면에 표시 'IMG'는 화면 이름을 지칭
    cv2.waitKey() # 키가 입력될 때 까지 대기(무슨 키를 말하는건지?)
    cv2.destroyAllWindows() # 창 모두 닫기
else:
    print('No image file.')