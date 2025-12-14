
import sys

from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal
import cv2
from PySide6.QtCore import QThread,Signal
class FaceDetect(QThread):
    signal_success_process = Signal()

    def __init__(self, image_path,choice):
        super().__init__()
        self.img_path = image_path
        self.choice=choice
    def run(self):
        if self.choice == "Face":
            haar_cascade = "face\haarcascade_frontalface_alt.xml"
        elif self.choice == "Eyes":
            haar_cascade = "face\haarcascade_eye.xml"
        face_detection = cv2.CascadeClassifier(haar_cascade)
        img = cv2.imread(self.img_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(img_gray, 1.3
                                                )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imwrite("output.jpg", img)
        self.signal_success_process.emit()

    def startFaceDetection(self):
        self.face_detect=FaceDetect(self.img_path)
        self.face_detect.start()
        self.face_detect.signal_success_process.connect(self.showOutput)
    def showOutput(self):
        my_pixmap=QPixmap("output.jpg")
        self.ui.le.setPixmap(my_pixmap)
class Face_detection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("c:/Users/Erfan/Desktop/Pracctice_Ai_2/face/form.ui")
        self.ui.show()

        self.ui.pb1.clicked.connect(self.open_image)
        
        self.ui.pb3.clicked.connect(self.startFace)
        self.ui.pb4.clicked.connect(self.startEyes)

    def startFace(self):
        self.startFaceDetection("Face")

    def startEyes(self):
        self.startFaceDetection("Eyes")



    def open_image(self):
        image_path = QFileDialog.getOpenFileName(self, "open file name")
        self.image_path = image_path[0]
        self.ui.le.setText(self.image_path)   
        my_pixmap = QPixmap(self.image_path)
        self.ui.label.setPixmap(my_pixmap)    

    def startFaceDetection(self,choice):
        self.detect = FaceDetect(self.image_path,choice)
        self.detect.signal_success_process.connect(self.showOutput)
        self.detect.start()

    def showOutput(self):
        my_pixmap = QPixmap("output.jpg")
        self.ui.label.setPixmap(my_pixmap)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= Face_detection()

    sys.exit(app.exec())
