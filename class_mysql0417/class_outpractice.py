# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 16:48
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_outpractice.py
# @Software: PyCharm

import mysql.connector
from class_mysql0417.db_config import readConfig

#连接数据库
#1、数据库连接信息
config={'host':'118.126.108.173',
        'user':'python5',
        'password':'python5666',
        'port':3306,
        'database':'test_summer',
        }

#2、登录数据库
#conection=mysql.connector.connect(**config)#  **后面加上配置文件名

#调用配置文件模块读取配置信息进行登录
conection= mysql.connector.connect(**readConfig().read_config('db.conf','DBCONFIG','config'))


sql_create_table='''
    CREATE TABLE yyt_practice(
      `id` int(10) NOT NULL AUTO_INCREMENT,
      `name` varchar(10) DEFAULT NULL,
      `age` int(3) DEFAULT NULL,
      PRIMARY KEY (`id`))
      ENGINE=MyISAM DEFAULT CHARSET=utf8'''

zgh='''
    create table zgh_practice(
        id int not null ,
        PRIMARY KEY (`id`) ,
        name varchar(12),
        sex varchar(12),
        class_id int(11),
        address varchar(12),
        create_date datetime,
        updata_date datetime
        )DEFAULT CHARSET=utf8;'''

#建游标
cursor=conection.cursor()

#新建数据库
#cursor.execute("CREATE DATABASE zgh1practice")

#删除数据库
#cursor.execute("drop database zgh_practice")

#cursor.execute(zgh)#新建表单
#cursor.execute(sql_create_table)

#cursor.execute('drop table zgh_practice')#删除表单

sql='insert into zgh_practice(id,name,sex,class_id,address) value (%(id)s,%(name)s,%(sex)s,%(class_id)s,%(address)s)'
list_1=[{'id':1,'name':'seleath','sex':18,'class_id':5,'address':90,},
        {'id':2,'name':'seleath1','sex':22,'class_id':5,'address':90,},
        {'id':3,'name':'seleath2','sex':23,'class_id':5,'address':90,},
        {'id':4,'name':'seleath3','sex':12,'class_id':5,'address':90,},
        {'id':5,'name':'seleath4','sex':31,'class_id':5,'address':90,},
        {'id':6,'name':'seleath5','sex':43,'class_id':5,'address':90,},]
cursor.executemany(sql,list_1)#对表进行内容插入

#修改表中名字为seleath的age值为3
#cursor.execute("update yyt_practice set age=3 where name='seleath4'")

#表中插入一条数据对应值
#cursor.execute("insert into yyt_practice(id,name,age) value(99,'seleath66',55)")


#切记一定要执行
cursor.execute('commit')


#关闭游标
cursor.close()

#关闭连接
conection.close()