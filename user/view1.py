# coding=utf-8


from . import app_user
from flask import render_template




@app_user.route('/')
def hello_world():

    return 'hello flask'

@app_user.route('/get_user', methods=['GET', 'POST'])
def get_user():
    # 记得设置templates文件夹的颜色问题
    return render_template('userindex.html')

@app_user.route('/set_user', methods=['GET', 'POST'])
def set_user():
    return 'setuser'

