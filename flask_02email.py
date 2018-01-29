# coding=utf-8

from flask import Flask
from flask_mail import Mail,Message
app = Flask(__name__)
# 配置邮件：服务器／端口／安全套接字层／邮箱名／授权码
app.config['MAIL_SERVER'] = "smtp.163.com"
app.config['MAIL_PORT'] =  465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "hua2680465171@163.com"
app.config['MAIL_PASSWORD'] = "python666"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<hua2680465171@163.com>'
mail=Mail(app)

@app.route('/')
def hello_world():

    return '<a href="/send_email">发送邮件</a>'


@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    msg=Message('这是邮件的主题', recipients=['1054921935@qq.com'],body='This is flask mail')
    mail.send(msg)
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)