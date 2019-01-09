# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 0:26
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_mysql_select.py
# @Software: PyCharm


#如果这个数据库存在，你要访问这个存在的数据库，就要database配置
#如果你要通过python新建一个数据库，那么database 还需要么？=====不需要

import mysql.connector
#1、数据库连接信息
config={'host':'118.126.108.173',#默认127.0.0.1
        'user':'python5',
        'password':'python5666',
        'port':3306,#默认几位3306
        'database':'test_summer',
        #'charset':'utf8'#默认几位utf8
        }#数据库连接信息

#2、登录数据库
conection=mysql.connector.connect(**config)#  **后面加上配置文件名

#3、获取游标
cursor=conection.cursor()

#4、可以开始愉快的玩耍 了，进行一个查询操作
sql='select * from student where id>%s'
cursor.execute(sql,(6,))#要用元组方式来传入参数
result_1=cursor.fetchone()#读取一行的数据
result=cursor.fetchall()#读取所有的数据，如果先读取，在fetchone就会读不到

print(result_1)
print(result_1[1])
print(type(result_1[1]))
#print(type(result_1))
#print('\n')
#print(result)
#print(type(result))

#5、关闭游标
cursor.close()

#6、关闭连接
conection.close()















