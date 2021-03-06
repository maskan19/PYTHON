import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt08.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        rsp = ["가위", "바위", "보"]
        com = random.randrange(0,3)
        if(com==0):
            self.le1.setText("가위")
        elif(com==1):
            self.le1.setText("바위")
        else:
            self.le1.setText("보")
            
        if(self.le1.text()==self.le2.text()):
                self.le3.setText("무승부")
        elif(rsp.index(self.le2.text())-com==1 or rsp.index(self.le2.text())-com==-2):
            self.le3.setText("승리")
        else:
            self.le3.setText("패배")


if __name__ == "__main__":
    
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    # WindowClass의 인스턴스 생성
    myWindow = MyWindow() 

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
