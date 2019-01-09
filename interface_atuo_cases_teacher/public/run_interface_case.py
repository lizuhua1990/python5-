__author__ = '20489'
import unittest
from interface_atuo_cases_teacher.public.http_request import httpRequest
from interface_atuo_cases_teacher.public.R_W_Excel import R_W_Excel
from interface_atuo_cases_teacher.conf import project_path
from interface_atuo_cases_teacher.public.read_config import readConfig
from ddt import ddt,data,unpack
from interface_atuo_cases_teacher.public.get_mysql_info import getMysqlInfo

mode=readConfig().get_value(project_path.case_conf_path,'FLAG','mode')
case_list=eval(readConfig().get_value(project_path.case_conf_path,'FLAG','case_list'))

t=R_W_Excel(project_path.test_data_path,'register','init')
test_data=t.read_excel(mode,case_list)

@ddt
class testInterFaceCase(unittest.TestCase):
    def setUp(self):
        print("开始接口测试啦！")

    @data(*test_data)
    @unpack
    def test_interface(self,id,method,url,data,Expected_code,sql):
        print("正在执行第%s条用例"%id)
        result_dict={}
        result=httpRequest().http_request(method,url,data)
        sql_result=getMysqlInfo(project_path.db_conf_path).get_mysql_info(sql['my_sql'],sql['condition'],sql['code'])
        result_dict['Actual_code']=result['code']
        result_dict['Reason']=result['msg']
        if result['code']==Expected_code and sql_result[0]==sql['result']:
            result_dict['Result']='pass'
            result_dict["sql_result"]='pass'
        else:
            result_dict['Result']='fail'
            result_dict["sql_result"]='fail'
        t.write_excel(id+1,result_dict)

    def tearDown(self):
        print("结束接口测试啦")
