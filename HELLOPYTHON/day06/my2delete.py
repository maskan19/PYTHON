import pymysql
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

# ==== update OR delete example ====

sql = "delete from sample where col01=%s"
cnt = curs.execute(sql, 2)
print(cnt)
conn.commit()
conn.colse()