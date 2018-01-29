# coding=utf-8
import unittest
from flask_login import app
import json


class LoginTestCase(unittest.TestCase):
    def setUp(self):
    #     准备工作和一些代码可以放在这
        # 打开测试模式, 能够方便去排除错误
        app.testing = True

        self.client = app.test_client()


    # 参数不完整的测试用例
    def test_empty_username_password(self):
        # 获得测试客户端
        # client=app.test_client()
        # 模拟发出请求
        # 路由和数据
        response=self.client.post('/login',data={})
        # 获取响应的数据
        response_data=response.data
        # 4. 将字符串数据转成字典
        # json.loads(): 将字符串转字典   json.dumps(): 将字典转字符串
        response_json=json.loads(response_data)

        # 5. 先判断是否有errcode这个key
        # assertIn: 判定某个值, 是否在某个对象中
        self.assertIn('errcode',response_json,'None errcode')

        # 6. 再判断errcode是否为-2
        errcode=response_json['errcode']

        self.assertEqual(errcode,-2,'errcode must -2, but current is %s' % errcode)
        print errcode

    # 参数用户名密码不正确的测试用例
    def test_correct_username_password(self):
        response = self.client.post('/login', data={'username': 'python', 'password': '123456'})
        response_data = response.data
        response_dict = json.loads(response_data)
        self.assertIn('errcode', response_dict, 'no errcode')
        errcode = response_dict['errcode']
        self.assertEqual(errcode, 0, 'errcode must 0, but current is %s' % errcode)
        print errcode
    # 参数用户名密码正确的测试用例
    def test_empty_username(self):
        response = self.client.post('/login', data={'username': '', 'password': '123456'})
        response_data = response.data
        response_dict = json.loads(response_data)
        self.assertIn('errcode', response_dict, 'no errcode')
        errcode = response_dict['errcode']
        self.assertEqual(errcode, -2, 'errcode must 0, but current is %s' % errcode)
        print errcode# 参数用户名密码不正确的测试用例
    def test_empty_password(self):
        response = self.client.post('/login', data={'username': 'python', 'password': ''})
        response_data = response.data
        response_dict = json.loads(response_data)
        self.assertIn('errcode', response_dict, 'no errcode')
        errcode = response_dict['errcode']
        self.assertEqual(errcode, -2, 'errcode must 0, but current is %s' % errcode)
        print errcode
        # 参数用户名密码不正确的测试用例
    def test_notcorrect_username_password(self):
        response = self.client.post('/login', data={'username': 'itheima', 'password': '666661'})
        response_data = response.data
        response_dict = json.loads(response_data)
        self.assertIn('errcode', response_dict, 'no errcode')
        errcode = response_dict['errcode']
        self.assertEqual(errcode, -1, 'errcode must 0, but current is %s' % errcode)
        print errcode


if __name__ == '__main__':
    unittest.main()