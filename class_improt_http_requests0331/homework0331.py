# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 19:41
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0331.py
# @Software: PyCharm


#3-31号作业： Python类与对象 requests学习

#1：利用3-29号写的从txt里面读取的数据的类，完成以下存在txt里面数据的读取，数据格式为：
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/register,mobilephone:13760246701,pwd:123456
#url:http://119.23.241.154:8080/futureloan/mvc/api/member/register,mobilephone:15678934551,pwd:234555
#2:利用课堂上写的http请求类，对从第一步里面利用类获取的测试数据，第一行数据来完成get请求和第二行数据来完成post请求。
#3：做好课堂笔记哦！！！

#文本路径地址：D:\python5\class_improt_http_requests0331\test_1.txt

import requests
import copy
class siMida:
    dict={}
    list=[]
    def __init__(self,address):
        self.address=address#初始化函数
    def luJin(self):
        with open(self.address,'r') as file:#打开路径地址
            for i in file.readlines():#依次读取每一行内容记为:i
                #print(i)
                for ii in i.strip ("\n").split (','):#每次读取的内容删除换行符，再根据“，”进行切割后记为：ii
                    #print(ii)
                    # 对切割后的内容根据第一个“：”进行切割；第一项为key，value为第二项；保存到一个dict里面
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                # list append 动态dict会只存最后修改的一个dict值，因为存的是引用，只能用copy  拷贝dict
                self.list.append(copy.deepcopy(self.dict))#每次从dict里面拷贝的值，插入list
        #print(self.list)
        return self.list#返回值
s=siMida(input("文本路径地址："))

class httpRequest:
    def httpGet(self,url,data_1):
        request=requests.get(url,data_1)
        print(request.json())
        return request.json()
    def httpPost(self,url,data_2):
        request=requests.post(url,data_2)
        print (request.json ())
        return request.json()

if __name__ == '__main__':
    url = str(s.luJin()[0]['url'])
    #url = str(s.luJin()[1]['url'])

    del s.luJin ()[0]['url']
    #print(s.luJin()[0])
    data_1 = s.luJin()[0]
    print(data_1)

    del s.luJin ()[1]['url']
    #print (s.luJin ()[1])
    data_2 = s.luJin()[1]
    print(data_2)

    t=httpRequest()
    t.httpGet(url,data_1)
    t.httpPost(url,data_2)