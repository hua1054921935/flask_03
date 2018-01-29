# coding=utf-8

from flask import Flask,request,jsonify,render_template

app = Flask(__name__)


# 当参数不全的话，返回errcode=-2
# 当登录名和密码错误的时候，返回 errcode = -1
# 当登录成功之后，返回 errcode = 0
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 接受参数
    username=request.form.get('username')
    password=request.form.get('password')
    # 参数校验
    if not all([username,password]):
        errdic={
            'errcode':-2,
            'errmsg':'参数不完整'
        }
        return jsonify(errdic)
    if username=='python' and password=='123456':
        errdic = {
            'errcode': 0,
            'errmsg': 'success'
        }
        return jsonify(errdic)
    else:
        errdic = {
            'errcode': -1,
            'errmsg': '帐号或密码不正确'
        }
        return jsonify(errdic)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')