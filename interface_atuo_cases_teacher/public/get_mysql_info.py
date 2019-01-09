__author__ = '20489'
import mysql.connector
from interface_atuo_cases_teacher.public.read_config import readConfig

class getMysqlInfo:

    def __init__(self,config_path):
        self.config=eval(readConfig().get_value(config_path,'MYSQL','config'))

    def get_cnn(self):
        cnn=mysql.connector.connect(**self.config)
        return cnn

    def get_mysql_info(self,my_sql,condition,code):#从数据库里面传信息了
        cnn=self.get_cnn()
        cursor=cnn.cursor()
        cursor.execute(my_sql,(condition,))
        if code==1:#查询所有的
            result=cursor.fetchall()
        elif code==0:#查询一条信息
            result=cursor.fetchone()
        cursor.close()
        cnn.close()
        return result

