import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from astropy.units import fl

form_class = uic.loadUiType("myomok19.ui")[0]

class MyWindow(QMainWindow, form_class):
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
        self.arr2D=[
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]

            ]
        self.arr2pb = []
        self.flag_wb = True
        self.flag_ing = True

        
        for i in range(19):
            line = []
            for j in range(19):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(40*j , 40*i, 40, 40))
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{},{}".format(i,j))
                line.append(pb)
            self.arr2pb.append(line)
        
        self.myrender()
        
    def myreset(self):
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j]=0

        self.flag_wb = True
        self.flag_ing = True  
        self.seq=0
        self.myrender()
        
        
    def myclick(self):
        if not self.flag_ing:
            return
        
        str = self.sender().toolTip()
        arr = str.split(",")
        i = int(arr[0])
        j = int(arr[1])
        print(i, "좌표",j)
        print(self.arr2D[i][j])
        
        
        if self.arr2D[i][j] > 0:
            return
        
        int_wb = 0
        if self.flag_wb : 
            print('if');  
            self.arr2D[i][j] = 1
            print(self.arr2D[i][j])
            int_wb = 1
        else :
            self.arr2D[i][j] = 2  
            int_wb = 2
        self.myrender()
        
        up = self.getUP(i,j,int_wb)
        dw = self.getDW(i,j,int_wb)
        ri = self.getRI(i,j,int_wb)
        le = self.getLE(i,j,int_wb)
        
        ul = self.getUL(i,j,int_wb)
        ur = self.getUR(i,j,int_wb)
        dl = self.getDL(i,j,int_wb)
        dr = self.getDR(i,j,int_wb)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self, "omok", "흑돌이 이겼습니다.")
            self.flag_ing = False    
            return
        
        self.flag_wb = not self.flag_wb
        
        com_i = self.arr_ij[self.seq][0]
        com_j = self.arr_ij[self.seq][1]
        
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
        
        ul = self.getUL(com_i,com_j,int_wb)
        ur = self.getUR(com_i,com_j,int_wb)
        dl = self.getDL(com_i,com_j,int_wb)
        dr = self.getDR(com_i,com_j,int_wb)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "omok", "백돌이 이겼습니다.")
            else :
                QtWidgets.QMessageBox.about(self, "omok", "흑돌이 이겼습니다.")
            self.flag_ing = False    
        
        self.flag_wb = not self.flag_wb
        
        self.seq +=1
        
        
    def getDR(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDL(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUR(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            j += 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt 
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
                return cnt
        
        
    def getUL(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            j -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt 
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
                return cnt
        
        
    def getLE(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                j -= 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt        
        
    def getRI(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                j += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt                
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt        
        
        
    def getDW(self,i,j,int_wb):    
        cnt = 0
        try:  
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 :
                    return cnt
                if self.arr2D[i][j] == int_wb:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    
    def getUP(self,i,j,int_wb):    
        cnt = 0
        while True :
            i -= 1
            if i < 0 :
                return cnt
            if j < 0 :
                return cnt
            if self.arr2D[i][j] == int_wb:
                cnt += 1
            else:
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

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    