import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myqt06.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        dan = int(self.le.text())
        result = str(dan)+" * 1 = " + str(dan*1)
        result = str(dan)+" * 2 = " + str(dan*2)
        result = str(dan)+" * 3 = " + str(dan*3)
        result = str(dan)+" * 4 = " + str(dan*4)
        result = str(dan)+" * 5 = " + str(dan*5)
        result = str(dan)+" * 6 = " + str(dan*6)
        result = str(dan)+" * 7 = " + str(dan*7)
        result = str(dan)+" * 8 = " + str(dan*8)
        result = str(dan)+" * 9 = " + str(dan*9)
        self.te.setText(result)


if __name__ == "__main__":
    
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    # WindowClass의 인스턴스 생성
    myWindow = MyWindow() 

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
