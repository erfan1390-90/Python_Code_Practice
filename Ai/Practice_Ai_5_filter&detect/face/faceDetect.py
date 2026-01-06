
from PySide6.QtCore import QThread,Signal
import cv2
class FaceDetect(QThread):
    signal_success_process = Signal()

    def __init__(self, image_path,choice):
        super().__init__()
        self.img_path = image_path
        self.choice=choice
    def run(self):
        if self.choice == "Face":
            haar_cascade = "haarcascade_frontalface_alt.xml"
        elif self.choice == "Eyes":
            haar_cascade = "haarcascade_eye.xml"
        face_detection = cv2.CascadeClassifier(haar_cascade)
        img = cv2.imread(self.img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(img_gray, 1.1)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imwrite("output.jpg", img)
        self.signal_success_process.emit()