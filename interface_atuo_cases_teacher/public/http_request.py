__author__ = '20489'
import requests
from interface_atuo_cases_teacher.conf import project_path


#logger=Log('auto_cases',project_path.log_path)
class httpRequest:
    def http_request(self,method,url,data):
        if method.upper()=='GET':
            #logger.info("现在进行GET请求")
            result=requests.get(url,data).json()
        elif method.upper()=='POST':
            #logger.info("现在进行POST请求")
            result=requests.post(url,data).json()
        else:
            print("请求方法未知！")
            #logger.info("未知请求方法，请核对后再试")
        return result

