import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

# def getPrices(s_name):
conn = pymysql.connect(host='localhost', user='root', password='python', db='_stock_old', charset='utf8')
curs = conn.cursor()
sql = "select * from stock_sync_0121  ORDER BY in_time"
curs.execute(sql)
# code_155660 = []  # 종목코드 00
# date_155660 = []  # 날짜 03
# price = []  # 가격 02
datas = curs.fetchall()
conn.close()
# for data in datas:
    # # code_155660.append(data[0])
    # # date_155660.append(data[3])
    # price.append(data[2]/datas[0][2])
# return datas
# 2224 893
print(len(datas))#2225
# print(getPrices('메리츠금융지주'))
print(len(datas[0])-2)#893
# print(datas[2224][893])
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.zeros(len(datas), dtype=int)
y = range(len(datas))
z=[]
for i in range(30):
    temp=[]
    origin= datas[0][i]
    for data in datas:
        # origin = 1
        # if datas[0][j]!=0:
        temp.append(data[i]/origin)
        # print(datas[i][j])
    ax.plot(x+i, y, temp, label=i)

ax.legend()
plt.show()
print("done")



#
#
#
# ax.plot(a, y, getPrices('덴티움'), label='DENTIUM')
# ax.plot(a+1, y, getPrices('삼양사'), label='SAMYANGSA')
# ax.plot(a+2, y, getPrices('한진칼'), label='HANGINCAL')
# ax.plot(a+3, y, getPrices('NHN'), label='NHN')
# ax.plot(a+4, y, getPrices('더블유게임즈'), label='WGAMES')
# ax.legend()
#
# plt.show()
