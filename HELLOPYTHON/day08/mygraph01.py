import pymysql
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()
print("ddd")
# ==== select example ====
sql = "select * from stock where s_code=155660"
curs.execute(sql)
X=[]#종목코드 00
Y=[]#날짜 03
Z=[]#가격 02
# 데이타 Fetch
datas = curs.fetchall()
for data in datas:
    X.append(data[0])
    Y.append(data[3])
    Z.append(data[2])
    # print(Y)
    
print(Z)
print(X)
print(Y)




##1종목꺾은선
# import matplotlib.pyplot as plt
#
# plt.plot(Y, Z)
# plt.xlabel('in_date')
# plt.ylabel('s_price')
# plt.show()






# %matplotlib inline
from matplotlib.collections import PolyCollection
from matplotlib.colors import ColorConverter, colorConverter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d

style.use('seaborn-talk')

fig = plt.figure()
ax = fig.gca(projection='3d')

def cc(arg):
    return colorConverter.to_rgba(arg, alpha=0.6)

xs = np.arange(0,10,0.4)
verts = []
zs = [0.0,1.0,2.0,3.0]
for z in zs:
    ys = np.random.rand(len(xs))
    ys[0], ys[-1] = 0,0
    verts.append(list(zip(xs, ys)))

poly = PolyCollection(verts, facecolors=[cc('r'), cc('g'), cc('b'), cc('y')])
poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=zs, zdir='y')
ax.set_xlabel('in_date')
ax.set_xlim3d(0,10)
ax.set_ylabel('s_code')
ax.set_ylim3d(-1,4)
ax.set_zlabel('s_price')
ax.set_zlim3d(0,1)
plt.show()








#
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# a = np.arange(0, 60000, 0.2)
#
# plt.plot(a, Z, 'bo')
# # plt.plot(a, 4, color='#e35f62', marker='*', linewidth=1)
# # plt.plot(a, a**3, color='springgreen', marker='^', markersize=9)
# plt.xticks(np.arange(0, 10, 0.4), labels=Y)
# plt.yticks(np.arange(1, 6))
#
# plt.show()
#









from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as dates
import datetime, random
import matplotlib.ticker as ticker

def random_date():
    date = datetime.date(2021, 1, 1)
    while 1:
        date += datetime.timedelta(days=20)
        yield (date)
        
def format_date(x, pos=None):
    return dates.num2date(Y).strftime('%Y%m%d.%H%M') #use FuncFormatter to format dates
    
r_d = random_date()
some_dates = [dates.date2num(next(r_d)) for i in range(0,20)]

fig = plt.figure(figsize=(10, 10))
ax = Axes3D(fig,rect=[0,0.1,1,1]) #make room for date labels

for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
    xs = np.array(some_dates)
    ys = np.random.rand(20)
    ax.bar(xs, ys, zs=z, zdir='y', color=c, alpha=0.8,width=8)
    
ax.w_xaxis.set_major_locator(ticker.FixedLocator(some_dates)) # I want all the dates on my xaxis
ax.w_xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
for tl in ax.w_xaxis.get_ticklabels(): # re-create what autofmt_xdate but with w_xaxis
    tl.set_ha('right')
    tl.set_rotation(30)     
    
ax.set_ylabel('Series')
ax.set_zlabel('Amount')

plt.show()






# import matplotlib as mpl
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np                #  뭔가 많이 import 시켰다. 그냥 그른가부다 하고 넘어가자.
# import matplotlib.pyplot as plt   #  여러분이 코딩을 할땐 그냥 복붙하여 사용하면 된다.
# # import 어쩌고 as 저쩌고 라는 코드는 from 어쩌고 import 와 비슷하다. 다만 코드를 칠때마다 "저쩌고.어쩌고 안의 기능"이라고 해야 코드가 작동한다.
# # 바로 아래코드도 보면 mpl.rcParams[~~~] 이라고 써있다. rcParams 를 바로 쓰지 않는다.
# # mpl.rcParams['legend.fontsize'] = 10            # 그냥 오른쪽 위에 뜨는 글자크기 설정이다.
#
# fig = plt.figure()                                # 이건 꼭 입력해야한다.
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)    # 각도의 범위는 -4파이 에서 +4파이
# z = np.linspace(-2, 2, 100)                        # z는 -2부터 2까지 올라간다.
# # r = z**2 + 1                                    # z값이 변함에 따라 반지름이 바뀔 것이다. 
# x =  np.sin(theta)                            # 나선구조를 만들기 위해 x는 sin함수
# y =  np.cos(theta)                            # 나선구조를 만들기 위해 y는 cos함수
# ax.plot(x, y, z, label='parametric curve')        # 위에서 정의한 x,y,z 가지고 그래프그린거다.
# ax.legend()                                        # 오른쪽 위에 나오는 글자 코드다. 이거 없애면 글자 사라진다. 없애도 좋다.
#
# plt.show()