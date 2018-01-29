# coding=utf-8


from flask import Flask
from user import app_user

app = Flask(__name__)
# 3. 在app创建的文件中, 注册蓝图
# url_prefix可以在蓝图建立对像是实现，也可以放在注册时处理，建议放在注册的时候
app.register_blueprint(app_user,url_prefix='/api/v2.0')


@app.route('/')
def hello_world():

    return 'hello flask'

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)