# coding=utf-8

from flask import Flask
from cart import app_cart

app = Flask(__name__)
# 3. 在app创建的文件中, 注册蓝图
app.register_blueprint(app_cart)

@app.route('/')
def hello_world():

    return 'hello flask'

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)