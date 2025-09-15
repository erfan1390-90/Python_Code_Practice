
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class Calculatur(QWidget):
    def __init__(self):
        super(Calculatur).__init__()
        loader=QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.pb1.clicked.connect(self.sum)
        self.ui.pb4.clicked.connect(self.num1)
        self.ui.pb5.clicked.connect(self.num2)
        self.ui.pb6.clicked.connect(self.num3)
        self.ui.pb7.clicked.connect(self.num4)
        self.ui.pb8.clicked.connect(self.num5)
        self.ui.pb9.clicked.connect(self.num6)
        self.ui.pb10.clicked.connect(self.num7)
        self.ui.pb11.clicked.connect(self.num8)
        self.ui.pb12.clicked.connect(self.num9)
        self.ui.pb13.clicked.connect(self.num0)
        self.ui.pb3.clicked.connect(self.equal)
        self.ui.pb2.clicked.connect(self.sub)
        self.ui.pb14.clicked.connect(self.mul)
        self.ui.pb15.clicked.connect(self.div)
        self.ui.pb16.clicked.connect(self.clear)
        self.ui.pb17.clicked.connect(self.tawan)
        self.a=[]
        self.c=[]
        self.n=""
    def clear(self):
        self.n = ""
        self.a = []
        self.ui.tb1.clear()

    def num1(self):
        self.n+="1"
        self.ui.tb1.clear()
        self.ui.tb1.setText(self.n)
    def num3(self):
        self.n+="3"
        self.ui.tb1.setText(self.n)
    def num4(self):
        self.n+="4"
        self.ui.tb1.setText(self.n)
    def num0(self):
        self.n+="0"
        self.ui.tb1.setText(self.n)
    def num5(self):
        self.n+="5"
        self.ui.tb1.setText(self.n)
    def num6(self):
        self.n+="6"
        self.ui.tb1.setText(self.n)
    def num7(self):
        self.n+="7"
        self.ui.tb1.setText(self.n)
    def num8(self):
        self.n+="8"
        self.ui.tb1.setText(self.n)
    def num9(self):
        self.n+="9"
        self.ui.tb1.setText(self.n)
    def num2(self):
        self.n+="2"
        self.ui.tb1.setText(self.n)
    def mul(self):
        self.op="*"
        self.a.append(int(self.n))
        self.a.append("*")
        self.ui.tb1.setText("*")
        self.n=""

        self.ui.tb1.setText("*")
    def div(self):
        self.op="/"
        self.a.append(int(self.n))
        self.a.append("/")
        self.ui.tb1.setText("/")
        self.n=""
    def sum(self):
        self.op="+"
        self.a.append(int(self.n))
        self.a.append("+")
        self.ui.tb1.setText("+")
        self.n=""
        
    def equal(self):
        self.ui.tb1.clear()
         

        self.a.append(int(self.n))
        result = self.a[0]

        for i in range(1, len(self.a), 2):
            if self.a[i] == "+":
                result += self.a[i + 1]
            elif self.a[i] == "-":
                result -= self.a[i + 1]
            elif self.a[i] == "*":
                result *= self.a[i + 1]
            elif self.a[i] == "/":
                result /= self.a[i + 1]
            elif self.a[i] == "**":
                result = result**self.a[i + 1]
        self.ui.tb1.setText(str(result))
        self.n = str(result)
        self.n = ""
        self.a = []

    def sub(self):
        self.op="-"
        self.a.append(int(self.n))
        self.a.append("-")
        self.ui.tb1.setText("-")
        self.n=""
    def tawan(self):
        self.op="**"
        self.a.append(int(self.n))
        self.a.append("**")
        self.ui.tb1.setText("**")
        self.n=""
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculatur()
    
    sys.exit(app.exec())
