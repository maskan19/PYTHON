import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
import numpy as np
from tensorflow.keras.models import load_model

form_class = uic.loadUiType("myomok20.ui")[0]
model = load_model('20210320_172325.h5')

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbreset.clicked.connect(self.myreset)   
        
        self.arr2D = np.zeros((20,20))
        
        print(self.arr2D)
        self.arr2pb = []
        self.flag_wb = True
        self.flag_ing = True
        
        
        for i in range(1,21):
            line = []
            for j in range(1,21):
                pb = QPushButton(self)
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(40 * j, 40 * i, 40, 40))
                pb.clicked.connect(self.myclick)
                pb.setToolTip("{},{}".format(i-1,j-1))
                line.append(pb)
            self.arr2pb.append(line)
            
        
        self.myrender()
    def myreset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
                
        self.flag_wb = True
        self.flag_ing = True
        self.myrender()
    def myclick(self):
        if not self.flag_ing: 
            return
        
        tool = self.sender().toolTip()
        toolarr = tool.split(",")
        i = int(toolarr[0])
        j = int(toolarr[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        int_wb = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            int_wb = 1
        else:
            self.arr2D[i][j] = 2
            int_wb = 2
        
        self.myrender()
        
        up = self.getUP(i, j, int_wb)
        dw = self.getDW(i, j, int_wb)
        ri = self.getRI(i, j, int_wb)
        le = self.getLE(i, j, int_wb)
        
        ul = self.getUL(i, j, int_wb)
        ur = self.getUR(i, j, int_wb)
        dl = self.getDL(i, j, int_wb)
        dr = self.getDR(i, j, int_wb)
        
        result1 = up + dw + 1
        result2 = ri + le + 1
        result3 = ul + dr + 1
        result4 = dl + ur + 1
        
        print("up + dw",result1)
        print("ri + le",result2)
        print("ul + dr",result3)
        print("dl + ur",result4)
        
        if result1 == 5 or result2 == 5 or result3 == 5 or result4 == 5:
            if self.flag_wb:
                QtWidgets.QMessageBox.about(self, '게임끝', "백돌이 이겼습니다.")
            else:
                QtWidgets.QMessageBox.about(self, '게임끝', "흑돌이 이겼습니다.")
            self.flag_ing = False
            return
                 
        self.flag_wb = not self.flag_wb
        
        #컴
        input = np.array(self.arr2D)
        input[(input != 1) & (input != 0)] = -1
        input[(input == 1) & (input != 0)] = 1
        input = np.expand_dims(input, axis=(0, -1)).astype(np.float32)
        output = model.predict(input)
        output = output.reshape((20,20))
        
        for i in range(20):
            for j in range(20): 
                if self.arr2D[i][j]>0:
                    output[i][j] = 0
        
        com_i, com_j = np.unravel_index(np.argmax(output), output.shape)
        
        print(output)
        print(np.argmax(output))
        
        int_wb = 0
        if self.flag_wb:
            self.arr2D[com_i][com_j] = 1
            int_wb = 1
        else:
            self.arr2D[com_i][com_j] = 2
            int_wb = 2
            
        self.myrender()
        
        up = self.getUP(com_i, com_j, int_wb)
        dw = self.getDW(com_i, com_j, int_wb)
        ri = self.getRI(com_i, com_j, int_wb)
        le = self.getLE(com_i, com_j, int_wb)
        
        ul = self.getUL(com_i, com_j, int_wb)
        ur = self.getUR(com_i, com_j, int_wb)
        dl = self.getDL(com_i, com_j, int_wb)
        dr = self.getDR(com_i, com_j, int_wb)
        
        result1 = up + dw + 1
        result2 = ri + le + 1
        result3 = ul + dr + 1
        result4 = dl + ur + 1
        
        if result1 == 5 or result2 == 5 or result3 == 5 or result4 == 5:
            if self.flag_wb:
                QtWidgets.QMessageBox.about(self, '게임끝', "백돌이 이겼습니다.")
            else:
                QtWidgets.QMessageBox.about(self, '게임끝', "흑돌이 이겼습니다.")
            self.flag_ing = False
        
        self.flag_wb = not self.flag_wb
            
    def getDR(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                i+=1
                j+=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt 
    
    def getDL(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                i+=1
                j-=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt  
     
    def getUR(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                i-=1
                j+=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt  
     
    def getUL(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                i-=1
                j-=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt 
    
    def getLE(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                j-=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt 
        
    def getRI(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                j+=1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt    
    
    def getUP(self, i, j, int_wb):
        cnt = 0
       
        while True:
            i-=1
            if i < 0:
                return cnt
            if int_wb == self.arr2D[i][j]:
                cnt+=1
            else:
                return cnt   
        
    def getDW(self, i, j, int_wb):
        cnt = 0
        try:
            while True:
                i+=1
                # if i > 9:
                if i < 0:
                    return cnt
                if int_wb == self.arr2D[i][j]:
                    cnt+=1
                else:
                    return cnt   
        except:
            return cnt
        
    def myrender(self):
        # print(self.arr2D)
        for i in range(20):
            for j in range(20):
                # self.arr2pb[i][j].setIcon(QtGui.QIcon(str(self.arr2D[i][j])+'.png'))
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