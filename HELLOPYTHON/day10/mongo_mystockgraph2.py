import pymongo

def getPrices(s_name):
    arr = []
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    rows = db.stock.find({'s_name' : s_name})
    # records = dict((record['_id'], record) for record in rows)
    first_price = rows[0]['s_price']
    print("2")
    for x in rows: 
        print(x)
        print(int(x['s_price'])/int(first_price))
        arr.append(int(x['s_price'])/int(first_price))
    return arr
if __name__ == '__main__':
    getPrices('삼성전자')
