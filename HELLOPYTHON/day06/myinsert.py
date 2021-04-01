import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="python",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO sample (col01, col02, col03) VALUES (%s, %s, %s)"

val = ('어쩌고', '저쩌고', '얍')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "개의 행이 삽입되었습니다.")
