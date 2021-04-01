import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["python"]
mycol = mydb["sample"]

myquery = { "_id": "myid" }

# mycol.delete_one(myquery)
mycol.delete_many(myquery)