# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 9:05
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_mysql_insert.py
# @Software: PyCharm

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
'''
#4、进行数据插入操作
#直接插入法===所有的值都需要赋值
sql="insert into student values(97,'bird5',18)"


#直接插入法===只输入不为空的值
sql="insert into student(id,name) values(98,'bird3')"
cursor.execute(sql)#要用元组方式来传入参数
cursor.execute('commit')#执行一下


#元组插入法==通过元组传递数据进行插入
sql="insert into student(id,name) values(%s,%s)"
cursor.execute(sql,(99,'python666'))#要用元组方式来传入参数
cursor.execute('commit')#执行一下


#字典插入法--通过字典传入数据
sql="insert into student(id,name) values(%(id)s,%(name)s)"
dict={'id':96,'name':'aibb'}
cursor.execute(sql,dict)
cursor.execute('commit')#执行一下
'''

#通过列表插入法，插入多条数据
sql="insert into student(id,name) values(%(id)s,%(name)s)"
list_1=[{'id':89,'name':'aibb'},{'id':88,'name':'aibb'},{'id':87,'name':'aibb'}]
#for i in list_1:
#    cursor.execute(sql,i)
cursor.executemany(sql,list_1)
cursor.execute('commit')#执行一下



#5、关闭游标
cursor.close()

#6、关闭连接
conection.close()
