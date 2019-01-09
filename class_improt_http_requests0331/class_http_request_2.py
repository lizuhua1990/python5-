# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 15:58
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_http_request_2.py
# @Software: PyCharm

#现在有一个这样的地址

url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
#data={"mobilephone":"18688009090","pwd":"123456"}
import requests
#接口测试的时候  都是用字典来传值的
data={ 'mobilephone': '13760246701', 'pwd': '123456'}
request=requests.get(url,data)
print(request.json)
print(type(request.json()))



#写一个类  类里面有2个函数  一个完成http get
# 一个是完成http post  属性值自己家

class httpRequest:
    #def __init__(self,url,data):
        #self.url=url
        #self.data=data

    def httpGet(self,url,data):
        request=requests.get(url,data_1)
        return request.json()

    def httpPost(self,url,data):
        request=requests.post(url,data_2)
        return request.json()

if __name__ == '__main__':
    url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    data_1 = {"mobilephone": "18688009092", "pwd": "123456"}
    data_2 = {"mobilephone": "18688009091", "pwd": "123456"}
    t=httpRequest()
    t.httpGet(url,data_1)
    t.httpPost(url,data_2)