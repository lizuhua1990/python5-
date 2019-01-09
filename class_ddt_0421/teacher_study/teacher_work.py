# -*- coding: utf-8 -*-
# @Time    : 2018/4/21 14:35
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : teacher_work.py
# @Software: PyCharm

#获取测试数据
#地址：D:\python5\class_unittest_html0412\teacher\test.txt
import requests
import copy
import unittest

from class_ddt_0421.teacher_study.class_unittest_yuanLi import testHttpRequset

class siMida:
    dict={}
    list=[]
    def __init__(self,address):
        self.address=address#初始化函数
    def luJin(self):
        with open(self.address,'r') as file:#打开路径地址
            for i in file.readlines():#依次读取每一行内容记为:i
                for ii in i.strip ("\n").split (','):#每次读取的内容删除换行符，再根据“，”进行切割后记为：ii
                    self.dict[ii.split(':',1)[0]] = ii.split(':',1)[1]
                self.list.append(copy.deepcopy(self.dict))#每次从dict里面拷贝的值，插入list
        return self.list#返回值
t=siMida('test.txt')
print(t.luJin())
list=t.luJin()

for i in range(len(list)):
    url=list[i]['url']
    list[i].pop('url')

    method=list[i]['method']
#    if method=='get':
#        methodName='test_get'
#    if method=='post':
#        methodName='test_post'
    list[i].pop('method')

    suite=unittest.TestSuite()
    suite.addTest(testHttpRequset(url,list[i],method))

    runner=unittest.TextTestRunner()
    runner.run(suite)





