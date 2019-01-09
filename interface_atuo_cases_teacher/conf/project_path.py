__author__ = '20489'
import os
from interface_atuo_cases_teacher.public.read_config import readConfig

#项目地址
path_conf_path=os.path.join(os.path.split(os.path.realpath(__file__))[0],'path.conf')
print(path_conf_path)
project_path=readConfig().get_value(path_conf_path,"PROJECT_PATH","project_path")
print(project_path)
#http配置文件的路径
http_conf_path=os.path.join(project_path,"conf","http.conf")

#用例执行配置文件路径
case_conf_path=os.path.join(project_path,"conf","case.conf")

#数据库配置文件路径
db_conf_path=os.path.join(project_path,"conf","db.conf")

#注册测试数据的路径
test_data_path=os.path.join(project_path,"test_data","test_data.xlsx")
