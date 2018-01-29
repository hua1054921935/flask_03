# coding=utf-8

from . import app_user



@app_user.route('/s')
def hello_worlds():

    return 'hello flask'

@app_user.route('/get_users', methods=['GET', 'POST'])
def get_users():
    return 'getuser'

@app_user.route('/set_users', methods=['GET', 'POST'])
def set_users():
    return 'setuser'