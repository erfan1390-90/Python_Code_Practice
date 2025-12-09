import cv2

haar_path = "haarcascade_frontalcatface.xml"
face_detector = cv2.CascadeClassifier(haar_path)

img = cv2.imread("test.webp")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_detector.detectMultiScale(gray_img, 1.1)
print(faces)
for i, (x, y, w, h) in enumerate(faces):
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    img_s = img[y:y+h, x:x+w]
    cv2.imwrite(f"HUMANS\\result_{i}.jpg", img_s)

cv2.imshow("face_detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
