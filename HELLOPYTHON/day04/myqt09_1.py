import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt09.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.numclick)
        self.pb2.clicked.connect(self.numclick)
        self.pb3.clicked.connect(self.numclick)
        self.pb4.clicked.connect(self.numclick)
        self.pb5.clicked.connect(self.numclick)
        self.pb6.clicked.connect(self.numclick)
        self.pb7.clicked.connect(self.numclick)
        self.pb8.clicked.connect(self.numclick)
        self.pb9.clicked.connect(self.numclick)
        self.pb0.clicked.connect(self.numclick)
        self.pbCall.clicked.connect(self.callclick)
        
    def numclick(self):
        print(self.sender().text())
        new = self.sender().text()
        old = self.le.text()
        self.le.setText(old + new)
        
    def callclick(self):
        QMessageBox.information(self, "Calling", self.le.text())

        
        

if __name__ == "__main__":
    
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    # WindowClass의 인스턴스 생성
    myWindow = MyWindow() 

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
