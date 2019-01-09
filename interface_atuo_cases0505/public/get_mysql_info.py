# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 21:15
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : get_mysql_info.py
# @Software: PyCharm

from interface_atuo_cases0505.public.config import config
import mysql.connector
import os


mobilephone = data[1]['data']['mobilephone']
print(mobilephone)
conection = mysql.connector.connect (
    **config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'db.conf', 'DBCONFIG', 'config'))
cursor = conection.cursor ()
sql = 'select * from member where MobilePhone=%s'
result_1 = cursor.execute (sql, (mobilephone,))
result = cursor.fetchall ()
print (result_1)
# cursor.execute('commit')
cursor.close ()
conection.close ()
