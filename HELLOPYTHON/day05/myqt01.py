import sys

from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from anaconda_navigator.utils.launch import console

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("myomok.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0,  0, 0, 0, 0, 0]
            ]
        self.arr2pb = []
        self.turn = 0
        
        for i in range(10):
            line = []
            for j in range(10):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon("0.png"))
                pb.setIconSize(QtCore.QSize(40, 40))
                pb.setGeometry(QtCore.QRect(40 * j, 40 * i, 40, 40))
                # pb.setToolTip(str(i)+","+str(j))
                pb.setToolTip("{},{}".format(i, j))
                pb.clicked.connect(self.myclick)
                line.append(pb)
            self.arr2pb.append(line)
        self.myrender()
             
    def myrender(self):
         for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon("0.png"))
                elif self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon("1.png"))
                else:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon("2.png"))

        # self.arr2pb[0][0].setIcon(QtGui.QIcon("1.png"))
        # self.pb.setIcon(QtGui.QIcon("1.png"))
    def myclick(self):
        att = self.sender().toolTip().split(",")
        if self.arr2D[int(att[0])][int(att[1])] > 0:
            return
        if self.turn % 2 == 0:
            self.arr2D[int(att[0])][int(att[1])] = 1
        else:
            self.arr2D[int(att[0])][int(att[1])] = 2
        self.myrender()
        self.turn += 1

if __name__ == "__main__":
    
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    # WindowClass의 인스턴스 생성
    myWindow = MyWindow() 

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
