# coding=utf-8


'''

蓝图大致的实现步骤:
1. 在目录中的init文件中定义蓝图对象,把子模块导入init   import view1,view2
2. 把蓝图对象导入子模块,并储存所有视图函数
3. 在app创建的文件中, 注册蓝图


'''
from flask import Blueprint
# 1. 在目录中的init文件中定义蓝图对象
#  设置template_folder的时候, 路径的查询, 会根据__name__的值, 去该模块的同级目录查找
# 为了符合resfull的风格加上前缀url_prefix=‘/api/版本号’
# app_user = Blueprint('user', __name__, template_folder='templates', url_prefix='/api/v1.0')
app_user=Blueprint('user',__name__,template_folder='templates',url_prefix='/api/v1.0')

import view1,view2
