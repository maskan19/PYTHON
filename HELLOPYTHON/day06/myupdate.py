import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="python",
    database="python"
)

mycursor = mydb.cursor()

sql = "UPDATE sample SET col03 = '123' WHERE col02 = '1'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "개의 행이 수정되었습니다.")