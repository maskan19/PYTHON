from bs4 import BeautifulSoup
import datetime
import pymongo
import requests
import time

def insertStock(s_code, s_name, s_price, yyyymmdd_hhmm):
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    doc = {'s_code' : s_code,'s_name' : s_name,'s_price': s_price , 'in_date' : yyyymmdd_hhmm }
    stock.insert_one(doc)

for i in range(10): 
    print("i", i)
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    yyyymmdd_hhmm = datetime.datetime.now().strftime('%Y%m%d.%H%M') 
     
    for info in soup.select('.tbody'):
        s_name = info.dt.text
        s_price = info.dd.span.text.replace(",", "")
        s_code_txt = info.dd['id']
        s_code = s_code_txt[len(s_code_txt) - 6:len(s_code_txt)]        
        insertStock(s_name, s_price, s_code, yyyymmdd_hhmm)
    time.sleep(60)

