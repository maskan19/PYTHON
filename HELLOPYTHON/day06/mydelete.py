import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="python",
    database="python"
)

mycursor = mydb.cursor()

sql = "DELETE FROM sample WHERE col01 = '1'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "개의 행이 삭제되었습니다.")