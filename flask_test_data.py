# coding=utf-8
import unittest
from flask_test_sqlacm import *
class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        # 配置项
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test0'
        self.app = app
        # 创建表
        db.create_all()
    def tearDown(self):
        # 移除session中的数据,删除表
        db.session.remove()
        db.drop_all()

    def test_append_data(self):
        role=Role(name='admin')
        db.session.add_all([role])
        db.session.commit()
        roless=Role.query.filter(id==1).first()
        self.assertIsNotNone(roless)
