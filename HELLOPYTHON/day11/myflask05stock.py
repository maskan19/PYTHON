from flask import Flask, render_template
import pymysql
from flask.globals import request
# from day10.mongo_select import list


def stockList():
    conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "select * from stock"
    curs.execute(sql)
    rows = curs.fetchall()
    set = []
    for row in rows:
        if row[1] not in set:
            set.append(row[1])
    conn.close()
    return set



def readStock(s_name):
    conn = pymysql.connect(host='localhost', user='root', password='python', db='python', charset='utf8')
    curs = conn.cursor()
    sql = "select * from stock where s_name = '" + s_name+"'"
    curs.execute(sql)
    rows = curs.fetchall()
    conn.close()
    print(rows)
    return rows
# print(rows)



app = Flask(__name__)

@app.route('/stock')
def index():
    s_name = request.args.get("s_name", "이마트")
    rows = readStock(s_name)
    set = stockList()
    return render_template("stock.html", list=rows, set=set)
    # return render_template("stock.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8888" , debug=True)
    
    
    
    
    