import requests
from bs4 import BeautifulSoup
import pymysql
import datetime
import time
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

# ==== insert example ====

sql = "insert into stock(s_code,s_name,s_price, in_date) values (%s, %s, %s, %s)"
for i in range(10): 
    now = datetime.datetime.now().strftime('%Y%m%d.%H%M')
    response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    
    for info in soup.select('.tbody'):
            s_name = info.dt.text
            s_code = info.dd['id'][len(info.dd['id']) - 6:]
            s_price = info.dd.span.text.replace(",", "")
            curs.execute(sql, (s_code, s_name, s_price, now))
    print(i, '세트 입력')
    time.sleep(61)
    conn.commit() 

conn.close()