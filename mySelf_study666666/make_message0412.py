# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 18:52
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : make_message0412.py
# @Software: PyCharm


# Python SMTP发送邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

'''
# 第三方 SMTP 服务
mail_host = "smtp.yeah.net"  # 设置服务器
mail_user = "qian_xing@yeah.net"  # 用户名
mail_pass = "051215"  # 口令

sender = 'qian_xing@yeah.net'
receivers = ['849080458@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")


#Python发送HTML格式的邮件
mail_host = "smtp.yeah.net"  # 设置服务器
mail_user = "qian_xing@yeah.net"  # 用户名
mail_pass = "051215"  # 口令

sender = 'qian_xing@yeah.net'
receivers = ['849080458@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)


mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.txt.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''
# Python 发送带附件的邮件
mail_host = "smtp.yeah.net"  # 设置服务器
mail_user = "qian_xing@yeah.net"  # 用户名
mail_pass = "051215"  # 口令

sender = 'qian_xing@yeah.net'
receivers = ['849080458@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 创建一个带附件的实例
message = MIMEMultipart ()
message['From'] = Header ("菜鸟教程", 'utf-8')#邮件名字
message['To'] = Header ("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header (subject, 'utf-8')

# 邮件正文内容
message.attach (MIMEText ('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt.txt 文件
att1 = MIMEText (open ('test_1.txt', 'rb').read (), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="wotefuck.txt"'
message.attach (att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText (open ('test_2.txt', 'rb').read (), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach (att2)

try:
    smtpObj = smtplib.SMTP ()
    smtpObj.connect (mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login (mail_user, mail_pass)
    smtpObj.sendmail (sender, receivers, message.as_string ())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")