from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)           

@app.route('/', methods=['GET'])
def get():
    a = request.args.get('a',' no a here')
    # return 'get flask'  + a
    return render_template("  post.html", variable=a)

@app.route('/', methods=['POST'])
def post():
     a = request.form["a"," no a here"]
     return 'post flask!' + a

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="80" , debug=True)
    