#조건 select
from pymongo import MongoClient 
my_client = MongoClient("mongodb://localhost:27017/") 
mydb = my_client['python'] 
mycol = mydb['sample'] 
list = mycol.find_one({"col01":"1"}) 
print(list)

#전체 select
from pymongo import MongoClient 
my_client = MongoClient("mongodb://localhost:27017/") 
mydb = my_client['python'] 
mycol = mydb['sample'] 
list = mycol.find() 
#.sort(조건)로 정렬 가능
for x in list: 
    print(x)
    
#전체 select
import pymongo
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
rows = db.sample.find()
for x in rows: 
    print(x)