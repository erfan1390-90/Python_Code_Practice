from PySide6.QtCore import QThread,Signal
import cv2
import numpy as np
class FaceFilter(QThread):
    signal_success_process = Signal()
    def __init__(self,image_path,input_1,input_2,input_3,input_4,
input_5,input_6,input_7,input_8,input_9):
        super().__init__()
        self.image_path=image_path
        self.input_1=int(input_1)
        self.input_2=int(input_2)
        self.input_3=int(input_3)
        self.input_4=int(input_4)
        self.input_5=int(input_5)
        self.input_6=int(input_6)
        self.input_7=int(input_7)
        self.input_8=int(input_8)
        self.input_9=int(input_9)
    def run(self):
        img=cv2.imread(self.image_path)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        kernel=np.array([[self.input_1,self.input_2,self.input_3],
                        [self.input_4,self.input_5,self.input_6],
                        [self.input_7,self.input_8,self.input_9]])
        result=np.zeros(img.shape,dtype='uint8')

        for i in range(1,img.shape[0]-1):
            for j in range(1,img.shape[1]-1):
                small_img=img[i-1:i+2,j-1:j+2]

                out=np.multiply(small_img,kernel)
                result[i,j]=np.sum(out)
        cv2.imwrite("output_filter.jpg", result)
        self.signal_success_process.emit()