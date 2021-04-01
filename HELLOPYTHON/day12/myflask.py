from flask import Flask, render_template
from day12.mydao import MyEmpDao
from flask.globals import request
from flask.json import jsonify

app = Flask(__name__)

@app.route('/emp')
def index():
    list = MyEmpDao().getEmp()
    return render_template("emp.html", list = list)

@app.route('/ins.ajax', methods=['POST'])
def ins_ajax():
    data = request.get_json()
    print(data)
    sabun = data['sabun']
    name = data['name']
    dept = data['dept']
    mobile = data['mobile']
    cnt = MyEmpDao().insEmp(sabun, name, dept, mobile)
    result= "fail"
    if cnt==1:
        result = "success"

    return jsonify(result = result)

@app.route('/upd.ajax', methods=['POST'])
def upd_ajax():
    data = request.get_json()
    print(data)
    sabun = data['sabun']
    name = data['name']
    dept = data['dept']
    mobile = data['mobile']
    cnt = MyEmpDao().updEmp(sabun, name, dept, mobile)
    result= "fail"
    if cnt==1:
        result = "success"

    return jsonify(result = result)

@app.route('/del.ajax', methods=['POST'])
def del_ajax():
    data = request.get_json()
    print(data)
    sabun = data['sabun']
    name = data['name']
    dept = data['dept']
    mobile = data['mobile']
    cnt = MyEmpDao().delEmp(sabun)
    result= "fail"
    if cnt==1:
        result = "success"

    return jsonify(result = result)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port="80" , debug=True)
    