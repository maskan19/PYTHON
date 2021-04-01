import pymongo
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np                
import matplotlib.pyplot as plt   



connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
rows = list(db.stock.find())
records = dict((record['_id'], record) for record in rows)
# for x in rows: 
    # print(len(x))
print(len(records))
print(records.keys())

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.zeros(len(records), dtype=int)
y = range(len(records))
z=[]
for i in records:
    temp=[]
    origin= records[0][i]
    for data in records:
        temp.append(records[records.keys()]/origin)
    ax.plot(x+i, y, temp, label=i)

ax.legend()
plt.show()
print("done")