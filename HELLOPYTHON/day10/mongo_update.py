import pymongo
connection = pymongo.MongoClient("mongodb://localhost:27017/")
db = connection.python
users = db.sample

myquery = { "col02": "2" }
newvalues = { "$set": { "col03": "222" } }

x = users.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")