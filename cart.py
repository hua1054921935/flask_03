# coding=utf-8
from flask import Blueprint

'''
蓝图大致的实现步骤:
1. 在子模块中创建一个蓝图对象
2. 蓝图对象存储所有的视图函数
3. 在app创建的文件中, 注册蓝图
'''

# 1. 在子模块中创建一个蓝图对象

# 蓝图的名字 = Blueprint(路由里蓝图名字, 模块名:为了查找资源用的)
app_cart=Blueprint('cart_app',__name__)


# 2. 蓝图对象存储所有的视图函数
@app_cart.route('/cart_list')
def cart_list():
    return 'cart_list'


@app_cart.route('/cart_detail')
def cart_detail():
    return 'cart_detail'

@app_cart.route('/cart_goods')
def cart_goods():
    return 'cart_goods'