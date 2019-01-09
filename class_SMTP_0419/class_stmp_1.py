# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 15:06
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_stmp.py
# @Software: PyCharm

#通过smtp协议  邮件服务器
#有smtp协议 的模块，也就是直接发送邮件的模块

import smtplib#发送邮件的
from email.mime.text import MIMEText#负责构造邮件内容，多用途的网际邮件扩充协议
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

#构造内容
msg=MIMEText('hello','plain','utf-8')
msg['subject']='这是一次测试邮件的发送'
msg['from']='849080458@qq.com'
msg['to']='282820742@qq.com'
#print(type(str(msg)))

#发送邮件
s=smtplib.SMTP_SSL("smtp.qq.com",465)#连接上邮箱服务器

s.login('849080458@qq.com','jwlxnzjhqvtfbbfg')

s.sendmail('849080458@qq.com','282820742@qq.com',str(msg))

s.quit()#退出


'''
# 下面是文字部分，也就是纯文本
puretext = MIMEText('我是纯文本部分，')
msg.attach(puretext)

# 下面是附件部分 ，这里分为了好几个类型

# 首先是xlsx类型的附件
xlsxpart = MIMEApplication(open('test.xlsx', 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
msg.attach(xlsxpart)

# jpg类型的附件
jpgpart = MIMEApplication(open('beauty.jpg', 'rb').read())
jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
msg.attach(jpgpart)

# mp3类型的附件
mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
msg.attach(mp3part)

'''


