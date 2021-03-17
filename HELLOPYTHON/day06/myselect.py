import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="python",
    database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sample")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)