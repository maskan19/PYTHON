import pymysql
# anaconda prompt에서 conda install pymysql해야 임포트할 수 있음

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')

# statement
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()

# ==== select example ====
sql = "select col01, col02, col03 from sample"
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)
conn.close()