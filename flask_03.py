# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
# 1. 导入扩展
from flask_migrate import Migrate,MigrateCommand
'''
需要SQLAlchemy， Migrate,Manager
给manager绑定Migrate命令
使用时依次执行init，migrate，upgrate
命令是
python flask_03.py db init，
python flask_03.py db migrate，
python flask_03.py db upgrade(升高一个版本)
python 文件名.py db current(查看当前版本)
python 文件名.py db history(查看历史版本)
python 文件名.py db downgrade(降低一个版本)
'''

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:root:mysql@127.0.0.1/flask_21migrate'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/flask_21migrate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.debug=True
# 创建数据库
db=SQLAlchemy(app)

manager=Manager(app)
# 2. 创建迁移对象
migrate=Migrate(app,db)
# 3. 给manager添加迁移命令
# 第一个参数时终端要用的名字
manager.add_command('db',MigrateCommand)

# 创建模型
class Role(db.Model):
    __tablename__='roles'
    # 定义字段
    # db.Column 表示一个字段
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    info = db.Column(db.String(16))
    users=db.relationship('User',backref='role')
    def __repr__(self):
        return '<Role: %s %s>' % (self.name, self.id)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, index=True)
    email = db.Column(db.String(32), unique=True)
    info = db.Column(db.String(16))
    password = db.Column(db.String(32))
    # 表示外键   ForeignKey 表名.id
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name, self.id,self.email,self.role_id)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
