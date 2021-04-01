import pymysql
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

# ==== insert example ====
sql = "insert into sample(col01,col02,col03) values (%s, %s, %s)"
curs.execute(sql, ('김가나', '일본', '서울'))
cnt = curs.execute(sql, ('김다라', '칡소', '서울'))
conn.commit()
print(cnt)