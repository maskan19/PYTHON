from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    list = ['가', '나', '다']
    return render_template("post.html", list=list)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="80" , debug=True)
    