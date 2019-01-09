# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 23:01
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_excel_read.py
# @Software: PyCharm


#配置文件  filename.conf

#配置文件包含  标签[]  配置的详细内容   key——value  键值对

#配置文件里面可以有多个标签，随你定，每项标签下面  可以有很多个  key_value键值对

#我们如果要读取配置的信息， 那么我就需要打开配置文件  用指定的类和函数去读取

#什么样的内容放到配置文件里面去？
#1、经常变动的数据内容   2、公用比较多的   3,方便控制


#注意：******从excel 和 conf里面读取的都是“str”类型
#import requests
#requests.get()

import configparser#引入模块
cf=configparser.ConfigParser()#创建一个读取配置文件的实例
cf.read('http.conf',encoding='utf-8')#打开配置文件
#1、如果读取的配置文件里面有有中文要配置编码

#读取配置文件的值   sectiom :标签    option  ==key

print(cf.get("HTTP",'ip'))
print(cf['STUDENT']['name'])
print(cf.get("STUDENT",'name'))

#2、从配置文件里面读取的内容是什么样的数据类型
#三种方法可以进行转换类型为数字的
print(type(cf['STUDENT']['name']))
age=cf.getint('STUDENT','age')
print('age类型：',type(age))

age1=eval(cf.get('STUDENT','age'))
print('age类型：',type(age1))

age2=int(cf.get('STUDENT','age'))
print('age类型：',type(age2))


#如果你的配置文件里面的是字典或者是列表形式的了？读出来的类型？
print('case_list数据类型：',type(eval(cf['FLAG']['case_list'])))

#eval------> 把从Excel  配置文件  mysql 里面读取出来的
#指定数据编程Python可识别的数据类型
str='18'
print(type(eval(str)))





