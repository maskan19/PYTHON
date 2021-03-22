import pymongo
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.python
users = db.sample
doc = {'_id':'myid','firstname':'Terry','lastname':'Cho'}
users.insert_one(doc)

#다른 표현법
from pymongo import MongoClient 
import pandas as pd 
my_client = MongoClient("mongodb://localhost:27017/") 
# print(my_client.list_database_names()) 
mydb = my_client['python'] 
mycol = mydb['sample'] 
x = mycol.insert_one({"col1":"01", "col2":"02", "col3":"03"}) 
print(x.inserted_id)

