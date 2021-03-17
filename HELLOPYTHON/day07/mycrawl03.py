import requests
from bs4 import BeautifulSoup
import pymysql
import datetime
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

# ==== insert example ====
sql = "insert into stock(s_code,s_name,s_price, in_date) values (%s, %s, %s, %s)"

# curs.execute(sql, ('김가나', '일본', '서울'))
# cnt = curs.execute(sql, ('김다라', '칡소', '서울'))
# print(cnt)

now = datetime.datetime.now().strftime('%Y%m%d:%H%M')
# print(now) 

# anacoda때문에 따로 설치할 필요가 없다
 
response = requests.get('https://www.sedaily.com/Stock/Quote/?mobile')
txt = response.text
soup = BeautifulSoup(txt, 'html.parser')

for info in soup.select('.tbody'):
        s_name = info.dt.text
        s_code = info.dd['id'][len(info.dd['id']) - 6:]
        s_price = info.dd.span.text.replace(",", "")
        curs.execute(sql, (s_code, s_name, s_price, now))
conn.commit()
