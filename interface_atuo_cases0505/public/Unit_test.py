

import unittest
import requests
import time
import HTMLTestRunnerNew
import os
from ddt import ddt,data,unpack
from interface_atuo_cases0505.public.config import config
from interface_atuo_cases0505.public.readExcel import readExcel

class httpRequest:
    def httpGet(self,url,data_1):
        request=requests.get(url,data_1)
        return request.json()
    def httpPost(self,url,data_1):
        request=requests.post(url,data_1)
        return request.json()

url = config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'http.conf', 'REGISTER', 'recharge')
#data1=[{'mobilephone': 17681829064, 'amount': '200'}]
h = readExcel (os.path.dirname (os.getcwd ()) + '/test_data/' + 'rechargetestcases.xlsx', 'rechargetestcases','init')
data2 = h.read_Excel ()
mode = config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'case.conf', 'FLAG', 'mode')
ID = config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'case.conf', 'FLAG', 'case_list')

list=[]
for i in data2:
    if i['id'] in ID:
        list.insert(len(data2)-1,i['data'])
        print(list)

@ddt#用ddt装饰我的测试类
class testHttpRequset(unittest.TestCase):
    def setUp(self):
        print("============我要开始测试了===============")

    @data(*list)#用data 来装饰我的测试用例
    #加一个* 号可以进行区分单个执行
    #@unpack
    def test_get(self,a):
        data = httpRequest ().httpGet (url,a)
        print(data)
        print("这是第一条！")
        self.assertEqual (data['code'],'10001')
        self.assertEqual (data['msg'], '充值成功')

    def tearDown(self):
        print("===============我要结束测试了！==================")


if __name__ == '__main__':
    unittest.main()

