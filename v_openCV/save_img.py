import cv2

img_file = "../v_openCV/imgs/dog.jpg"
save_file = "../v_openCV/imgs/gray_dog.jpg" # 경로와 파일명을 미리 지정

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) # 파일로 저장함
cv2.waitKey()
cv2.destroyAllWindows()
