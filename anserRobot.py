import random
from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/ans',methods=['GET','POST'])
def answer_world():
    with open("1.txt", encoding='utf-8') as f:
        res = f.readlines()
        m = len(res) - 1
        i = random.randint(0, m)
        print(res[i])
    return render_template('ans.html',res=res[i])

@app.route('/cj',methods=['GET','POST'])
def answer_cj():
    with open("cj.txt", encoding='utf-8') as f:
        res = f.readlines()
        m = len(res) - 1
        i = random.randint(0, m)
        print(res[i])
    return render_template('ans.html',res=res[i])

if __name__ == '__main__':
    app.run('0.0.0.0',port=7777)
    # app.run('127.0.0.1',port=7777)