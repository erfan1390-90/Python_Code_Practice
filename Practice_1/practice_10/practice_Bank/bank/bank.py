
import sqlite3

connection=sqlite3.connect("bank.db")
my_curser=connection.cursor()

connection_2=sqlite3.connect("account.db")
my_curser_a=connection_2.cursor()

import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader


class Bank(QWidget):
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.pb2.clicked.connect(loan.show)
        self.ui.pb1.clicked.connect(loan.search)
        self.ui.pb3.clicked.connect(loan.loan_status)
        self.ui.pb4.clicked.connect(loan.loan_status_false)
        self.ui.pb6.clicked.connect(loan.write)
        self.ui.pb8.clicked.connect(loan.updata)
        self.ui.pb7.clicked.connect(loan.delete)
        self.ui.pb5.clicked.connect(loan.buy)


class Account:
    def show(self):
        for data in my_curser_a.execute("SELECT * FROM account WHERE account_status=1"):
            print(data)
    def show_false(self):
        for data in my_curser_a.execute("SELECT * FROM account WHERE account_status=0"):
            print(data)
    def money_transfer(self):
        self.account=int(input("enter account number: "))
        self.account_1=int(input("enter account(transfer) number: "))
        self.money=int(input("enter money: "))
        for data in my_curser_a.execute(f"SELECT * FROM account WHERE account_status=1 AND account_number={self.account} AND money>={self.money}"):
            for data in my_curser_a.execute(f"SELECT * FROM account WHERE account_status=1 AND account_number={self.account_1}"):
                my_curser_a.execute(f"UPDATE account SET money=money-{self.money} WHERE account_number={self.account}")
                my_curser_a.execute(f"UPDATE account SET money=money+{self.money}  WHERE account_number={self.account_1}")
                connection_2.commit()
                #connection.commit()
                break
            else:
                 print("account number (transfer) not found")
                 break
        # else:
        #     print("account number not found")




class Loan():

         
    def show(self):
        for data in my_curser.execute("SELECT * FROM loans WHERE STATUS=1 OR STATUS=0"):
            print(data)
    def show_false(self):
        for data in my_curser.execute("SELECT * FROM loans WHERE STATUS=0"):
            print(data)
    def search(self):
        self.id=int(widget.ui.le1.text())
        for data_s in my_curser.execute(f"SELECT * FROM loans WHERE ID={self.id} AND (STATUS=1 OR STATUS=0) "):
            widget.ui.le3_2.setText(str(data_s))
            break
        else:
            
            widget.ui.le3_2.setText(str(f"id {self.id} not found"))
            

    def loan_status(self):
        self.id=int(widget.ui.le1.text())
        my_curser.execute(f"UPDATE loans SET STATUS = 1 WHERE ID = '{(self.id)}'")
        connection.commit()

        if my_curser.rowcount>0:
                 widget.ui.le3_2.setText("ok")
        else:
                 widget.ui.le3_2.setText("not found")
    def loan_status_false(self):
        self.id=int(widget.ui.le1.text())
        my_curser.execute(f"UPDATE loans SET STATUS = 0 WHERE ID = '{(self.id)}'")
        connection.commit()

        if my_curser.rowcount>0:
                 widget.ui.le3_2.setText("ok")
        else:
                 widget.ui.le3_2.setText("not found")
    def write(self):
        self.id=int(widget.ui.le1.text())
        self.name=(widget.ui.le2.text())
        self.rcode=(widget.ui.le3.text())
        self.amount=int(widget.ui.le4.text())
        self.number=int(widget.ui.le5.text())
        self.year=int(widget.ui.le6.text())
        self.month=int(widget.ui.le7.text())
        self.day=int(widget.ui.le8.text())
        self.installment=int(widget.ui.le9.text())
        self.status=int(widget.ui.le10.text())
        my_curser.execute(f"INSERT INTO loans (ID,NAME,RCODE,AMOUNT,NUMBER,DATE_YEAR,DATE_MONTH,DATE_DAY,[LOAN INSTALLMENT],STATUS) \
        VALUES ({self.id},'{self.name}','{self.rcode}',{self.amount},{self.number},{self.year},{self.month},{self.day},{self.installment},{self.status})")
        connection.commit()
        widget.ui.le3_2.setText("ok")
    def updata(self):
        self.id=int(widget.ui.le1.text())
        self.name=(widget.ui.le2.text())
        self.rcode=(widget.ui.le3.text())
        self.amount=int(widget.ui.le4.text())
        self.number=int(widget.ui.le5.text())
        self.year=int(widget.ui.le6.text())
        self.month=int(widget.ui.le7.text())
        self.day=int(widget.ui.le8.text())
        self.installment=int(widget.ui.le9.text())
        self.status=int(widget.ui.le10.text())
        my_curser.execute(f"UPDATE loans SET ID={self.id},NAME='{self.name}',RCODE='{self.rcode}',AMOUNT={self.amount},NUMBER={self.number},DATE_YEAR={self.year},DATE_MONTH={self.month},DATE_DAY={self.day},[LOAN INSTALLMENT]={self.installment},STATUS={self.status} WHERE ID={self.id}")
        connection.commit()
        if my_curser.rowcount>0:
                 widget.ui.le3_2.setText("ok")
        else:
                 widget.ui.le3_2.setText("not found")
    def delete(self):
            self.id=int(widget.ui.le1.text())
            self.rcode=(widget.ui.le3.text())
            my_curser.execute(f"DELETE FROM loans WHERE ID='{self.id}' AND RCODE='{self.rcode}'")
            connection.commit()
            if my_curser.rowcount>0:
                 widget.ui.le3_2.setText("ok")
            else:
                 widget.ui.le3_2.setText("not found")
    def buy(self):
            self.id=int(widget.ui.le1.text())
            my_curser.execute(f"UPDATE loans SET STATUS = 0 WHERE ID = '{(self.id)}' AND AMOUNT=0")
            my_curser.execute(f"UPDATE loans SET AMOUNT = AMOUNT-1 WHERE ID = '{(self.id)}' AND STATUS=1")
            connection.commit()

            if my_curser.rowcount>0:
                 widget.ui.le3_2.setText("ok")
            else:
                 widget.ui.le3_2.setText("not found")
loan=Loan()
# loan.show()
account=Account()
# account.money_transfer()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Bank()
    widget.show()
    sys.exit(app.exec())
