# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 10:18
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : mysql_newdatabase.py
# @Software: PyCharm

'''
create table 创建表
alter table 修改表
drop table 删除表
truncate table 删除表中所有行
create index 创建索引
drop index 删除索引**
'''

from class_mysql0417.db_config import readConfig
import mysql.connector

conection = mysql.connector.connect(**readConfig().read_config('db.conf','DBCONFIG','config'))
#调用类函数，读取配置文件，连接mysql库
#创建游标
cursor=conection.cursor()#

#新建表
yyt_database = '''
    create table yyt_database(
        StdID int primary key not null,
        StdName varchar(100) not null,
        Gender enum('M','F') not null,
        Age int 
    )
'''


yyt_database1='''
    create table yyt_database1(
        id int not null PRIMARY key null ,
        yname varchar(12),
        sex varchar(12),
        class_id int(11),
        address varchar(12),
        create_date datetime,
        updata_date datetime
        )DEFAULT CHARSET=utf8;'''

#cursor.execute(yyt_database)
#cursor.execute(yyt_database1)

#插入数据
sql="insert into yyt_database(StdID,StdName,Gender,Age) values(%(StdID)s,%(StdName)s,%(Gender)s,%(Age)s)"
list_1=[{'StdID':1,'StdName':'aibb','Gender':'M','Age':19},
        {'StdID': 2, 'StdName': 'aibb1', 'Gender': 'M', 'Age': 19},
        {'StdID': 3, 'StdName': 'aibb2', 'Gender': 'F', 'Age': 44},
        {'StdID': 4, 'StdName': 'aibb3', 'Gender': 'F', 'Age': 33},
        {'StdID': 5, 'StdName': 'aibb4', 'Gender': 'M', 'Age': 23},
        {'StdID': 6, 'StdName': 'aibb5', 'Gender': 'M', 'Age': 543},
        {'StdID': 7, 'StdName': 'aibb6', 'Gender': 'F', 'Age': 12}]
#cursor.executemany(sql,list_1)
#cursor.execute('commit')


#删除一个表
#cursor.execute("delete from yyt_database where StdName='aibb5'")
#cursor.execute("insert into yyt_database value (676,'hhh','F',008)")
#cursor.execute("update yyt_database set Age='66'where StdID='66'")
#cursor.execute('drop table yyt_database1')

#切记一定要执行
cursor.execute('commit')

#5、关闭游标
cursor.close()

#6、关闭连接
conection.close()


