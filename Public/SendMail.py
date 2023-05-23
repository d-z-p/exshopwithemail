# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os


def SendMail(file_new, to_mail):  # file_new 为发送的文件内容，to_mail为接收人
    # 获取测试报告的内容
    try:
        file_html = open(file_new, 'rb')
        mail_body = file_html.read()
        file_html.close()

        # qq邮箱账号密码，授权密码
        send_user = '1090747962@qq.com'
        send_user_password = 'xikssyitvlljhefd'

        # 模块构造的带附件的邮件如图
        msg = MIMEMultipart()
        # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文


        # 发送正文
        text = MIMEText(mail_body, 'html', 'utf-8')
        text['Subject'] = Header('Ecshop-自动化测试报告', 'utf-8')
        msg.attach(text)

        # 发送附件
        # Header()用于定义邮件标题
        msg['Subject'] = Header('自动化测试报告', 'utf-8')
        msg_file = MIMEText(os.path.join(os.getcwd(),r'\Report'), 'html', 'utf-8')
        # msg_file = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file["Content-Disposition"] = 'attachment; filename="Ecshop-zidongceshibaogao.html"'
        msg.attach(msg_file)  #


        msg['from'] = Header(send_user)  # 发送邮件的人
        msg['to'] = Header(to_mail)     # 接收者的邮箱

        # 连接邮箱服务器，登陆服务器，发送邮件
        smtp = smtplib.SMTP('smtp.qq.com', 25)  # 连接服务器
        smtp.login(send_user, send_user_password)  # 登录的用户名和密码
        smtp.sendmail(send_user, to_mail, msg.as_string())  # 发送邮件
        smtp.quit()
        print('邮件发送成功！')
    except smtplib.SMTPException as error_sender:
        # 断开连接
        smtp.quit()
        print("邮件发送失败", error_sender)