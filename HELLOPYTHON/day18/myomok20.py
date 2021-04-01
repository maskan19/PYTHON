import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from prompt_toolkit.contrib.telnet.protocol import SE
import numpy as np
from ursina import *
from day18.gomoku import Board, Gomoku
from tensorflow.keras.models import load_model

model = load_model('20201213_202430.h5')
                   
def getIJFromNeuro(arr):
    
    arr_n = np.zeros((20,20))
    
    for i in range(20):
        for j in range(20):
            if arr[i][j] ==1:
                arr_n[i][j]=1
            if arr[i][j]==2:
                arr_n[i][j]= -1
            
    arr_n = np.reshape(arr_n,(1,20,20,1))
    output = model.predict(arr_n).squeeze()
    output = output.reshape((20, 20))
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j               
form_class = uic.loadUiType("myomok20.ui")[0]


class MyWindow(QMainWindow, form_class): #다중 상속
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbreset.clicked.connect(self.myreset)
        
        self.arr_ij=[
                [0,0],
                [0,1],
                [0,2],
                [0,3],
                [0,4]
            ]
        self.seq = 0
        
        #파이썬 전역변수
       
        self.arr2D= np.zeros((20,20))
        self.arr2pb = []
        self.flag_wb = True #파이썬에서 boolean타입은 이런식으로 선언
        self.flag_ing = True
      
        for i in range(20):
            line = []
            for j in range(20):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(40*j, 40*i, 40, 40))
                pb.clicked.connect(self.myclick) # 버튼에 클릭 이벤트 걸어주기
                pb.setToolTip("{},{}".format(i,j))
                
                line.append(pb)
            self.arr2pb.append(line)
           
                
        self.myrender()
        
    def myreset(self):
        
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j]=0
       
        self.flag_wb = True #파이썬에서 boolean타입은 이런식으로 선언
        self.flag_ing = True    
        self.seq = 0
        self.myrender()
    
    def myclick(self):
        if not self.flag_ing :
            return
        
            
        str12 = self.sender().toolTip()
        print(str12)
        spstr = str12.split(",") #값이 배열로 저장
        
        i = int(spstr[0])
        j = int(spstr[1])
        
        if self.arr2D[i][j] > 0: # 돌이 놓여져 있으면 return하도록
            return 
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[i][j] = 1
            int_wb = 1
        else :
            self.arr2D[i][j] = 2
            int_wb = 2
        self.myrender()
        
        up = self.getUP(i,j,int_wb)
        dw = self.getDW(i,j,int_wb)
        ri = self.getRI(i,j,int_wb)
        le = self.getLE(i,j,int_wb)
        
        UL = self.getUL(i,j,int_wb)
        UR = self.getUR(i,j,int_wb)
        DL = self.getDL(i,j,int_wb)
        DR = self.getDR(i,j,int_wb)
        
        print("up", up)
        print("dw", dw)
        print("RI", ri)
        print("LE", le)
        
        print("UL", UL)
        print("UR", UR)
        print("DL", DL)
        print("DR", DR)
        
        
        d1 = int(up + dw) + 1
        d2 = int(ri + le) + 1
        d3 = int(UL + DR) + 1
        d4 = int(UR + DL) + 1
        
        if (d1 == 5) or (d2 == 5) or (d3 == 5) or (d4 == 5):
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self, "omok", "흑돌이 이겼습니다.")
            self.flag_ing = False
            return

        self.flag_wb = not self.flag_wb
        
        com_i,com_j = getIJFromNeuro(self.arr2D)
        
        int_wb = 0
        if self.flag_wb :
            self.arr2D[com_i][com_j] = 1
            int_wb = 1
        else :
            self.arr2D[com_i][com_j] = 2
            int_wb = 2
        self.myrender()
        
        up = self.getUP(com_i,com_j,int_wb)
        dw = self.getDW(com_i,com_j,int_wb)
        ri = self.getRI(com_i,com_j,int_wb)
        le = self.getLE(com_i,com_j,int_wb)
        
        UL = self.getUL(com_i,com_j,int_wb)
        UR = self.getUR(com_i,com_j,int_wb)
        DL = self.getDL(com_i,com_j,int_wb)
        DR = self.getDR(com_i,com_j,int_wb)
        
        d1 = int(up + dw) + 1
        d2 = int(ri + le) + 1
        d3 = int(UL + DR) + 1
        d4 = int(UR + DL) + 1
        
        if (d1 == 5) or (d2 == 5) or (d3 == 5) or (d4 == 5):
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self, "omok", "흑돌이 이겼습니다.")
            self.flag_ing = False
            
        self.flag_wb = not self.flag_wb
        
    def getUP(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                i -= 1;
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt 
            
    def getDW(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                i += 1;
                
                if i < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt    
            
            
    def getRI(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j += 1;
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt 
        
    def getLE(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j -= 1;
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
        
    def getUL(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j -= 1
                i -= 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
         
         
    def getUR(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j += 1
                i -= 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def getDL(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j -= 1
                i += 1
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
        
    def getDR(self,i,j,int_wb):
        cnt = 0    
        try :
            
            while True:
                j += 1;
                i += 1;
                
                if i < 0:
                    return cnt
                
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else :
                    return cnt
        except:
            return cnt
    

    
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.arr2pb[i][j].setIcon(QtGui.QIcon('2.png'))
    
    
       
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindow()
    MyWindow.show()
    app.exec_()
    