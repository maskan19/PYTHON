import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음


def getPrices(s_name):
# MySQL Connection 연결
    conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
    
    # statement
    # curs = conn.cursor(pymysql.cursors.DictCursor)
    curs = conn.cursor()
    # ==== select example ====
    sql = "select * from stock where s_name='" + s_name + "'"
    curs.execute(sql)
    # code_155660 = []  # 종목코드 00
    # date_155660 = []  # 날짜 03
    price = []  # 가격 02
    datas = curs.fetchall()
    for data in datas:
        # code_155660.append(data[0])
        # date_155660.append(data[3])
        price.append(data[2])
    return price


# print(getPrices('메리츠금융지주'))
    
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

a = np.zeros(39, dtype=int)
b = a + 1
c = b + 1
y = range(39)

ax.plot(a, y, getPrices('덴티움'), label='DENTIUM')
ax.plot(a+1, y, getPrices('삼양사'), label='SAMYANGSA')
ax.plot(a+2, y, getPrices('한진칼'), label='HANGINCAL')
ax.plot(a+3, y, getPrices('NHN'), label='NHN')
ax.plot(a+4, y, getPrices('더블유게임즈'), label='WGAMES')
ax.legend()

plt.show()
