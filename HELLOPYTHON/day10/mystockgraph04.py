from mpl_toolkits.mplot3d import Axes3D
import pymysql

import matplotlib as mpl
import matplotlib.pyplot as plt  
import numpy as np      


def getAllPrice():
    zs = []
    conn = pymysql.connect(host='localhost', user='root', password='python', db='_stock_old', charset='utf8') 
    
    cursor = conn.cursor() 
    
    sql = """
            SELECT *
            FROM stock_sync_0121
             """
    cursor.execute(sql) 
    rows = cursor.fetchall() 
    cnt10 = len(rows)
    cnt3 = len(rows[0]) - 1
    
    for i3 in range(cnt3): 
            line = []
            first_price = rows[0][i3]
            if first_price == 0:
                first_price = 1
            for j10 in range(cnt10):
                # else:
                    line.append(rows[j10][i3] / first_price)
            zs.append(line)
    conn.close() 
    
    return zs

if __name__ == "__main__":
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    zs = getAllPrice()
    x = np.zeros(len(zs[0]))
    y = range(len(zs[0]))
    
for i3 in range(len(zs)):
    ax.plot(x + i3, y, zs[i3])
   
ax.legend()
plt.show()
        
