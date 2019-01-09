# -*- coding: utf-8 -*-
# @Time    : 2018/4/22 16:44
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_ddt_1.py
# @Software: PyCharm

import unittest
from ddt import ddt,data,unpack

#1、@ddt  放到你要调用的ddt装饰器的测试类上
#2、@data 放到你要调用的data数据驱动装饰器的测试用例上
#3、@data() 括号里面放你的测试数据，根据都好来进行分隔，每一个逗号隔开一个数据
#4、如果你想把数据拆分的话，数据变量前面加*号
#5、如果你的测试方法有多个参数要传入值，从你的测试数据里面来的，那么就加一个@unpack

#test_data=[[1,2],[3,4]]
test_data=[{'name':'戒懂','age':18},{'name':'影子','age':20}]
@ddt#用ddt装饰我的测试类
class testPrint(unittest.TestCase):
    def setUp(self):
        print('开始使用ddt咯！！！')

    @data(*test_data)#用data 来装饰我的测试用例
    #加一个* 号可以进行区分单个执行
    #@unpack
    def test_print(self,a):
        print("打印值：",a)

    def tearDown(self):
        print('结束使用ddt了！！')


if __name__ == '__main__':
    unittest.main()
















