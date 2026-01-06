
import sys

from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
import faceDetect
import faceFilter
class GUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.pb1.clicked.connect(self.open_image)
        self.ui.pb3.clicked.connect(self.startFace)
        self.ui.pb4.clicked.connect(self.startEyes)
        self.ui.pb5.clicked.connect(self.startFilter)

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
        self.detect = faceDetect.FaceDetect(self.image_path,choice)
        self.detect.signal_success_process.connect(self.showOutput_detect)
        self.detect.start()
        
    def startFilter(self):
        self.input_1=self.ui.le2.text()
        self.input_2=self.ui.le3.text()
        self.input_3=self.ui.le4.text()
        self.input_4=self.ui.le5.text()
        self.input_5=self.ui.le6.text()
        self.input_6=self.ui.le7.text()
        self.input_7=self.ui.le8.text()
        self.input_8=self.ui.le9.text()
        self.input_9=self.ui.le10.text()
        self.filter=faceFilter.FaceFilter(self.image_path,self.input_1,
self.input_2,self.input_3,self.input_4,self.input_5,
self.input_6,self.input_7,self.input_8,self.input_9)
        self.filter.signal_success_process.connect(self.showOutput_filter)
        self.filter.start()

    def showOutput_detect(self):
        my_pixmap = QPixmap("output.jpg")
        self.ui.label.setPixmap(my_pixmap)
        
    def showOutput_filter(self):
        my_pixmap = QPixmap("output_filter.jpg")
        self.ui.label.setPixmap(my_pixmap)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window= GUI()

    sys.exit(app.exec())
