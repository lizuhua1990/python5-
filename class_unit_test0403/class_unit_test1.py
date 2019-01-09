# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 19:24
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : unit_test.py
# @Software: PyCharm

#单元测试
#测试用例
#1、编号  用例标题   测试数据   期望结果   实际结果   是否通过
#2、txt  里面的测试数据  自己写了一个类  获取测试数据类  都写好了
#3、写用例  不同的测试数据  针对的就是不同的测试用例

class mathMethod:
    def add(self,a,b):
        return  a+b

    def sub(self,a,b):
        return a-b

#python   有自带的可以让我们写测试用例 自动执行测试用例并帮你比对结果
# 并输出测试报告的这么一套框架
#unittest------》单元测试
#现在要开始飞了  写用例了
import unittest
#写测试用例  我们还是对mathMethod  类里面的加法写测试用例
class testMathMethod(unittest.TestCase):#测试用例  类
    #写测试用例 所有的测试用例的名字必须是以test_开头
    def test_add_negative_positive(self):
        t = mathMethod ()
        try:#2018年4月12日教学补充，测试用例html报告中容错，抛出结果
            resutl=t.add (1, 2)  # 实际结果
            self.assertEqual(2,resutl)#改变一个错误的期望结果
        except Exception as e:
            print("用例执行失败，错误是%s"%e)
            #raise e#在出错后不返回错误，会认为是人为忽略这个错误，判断通过

    def test_add_two_positive (self):
        t = mathMethod ()
        resutl =t.add (3, 3)
        self.assertEqual (6, resutl)

    def test_add_two_negative (self):
        t = mathMethod ()
        resutl =t.add (-3, -6)
        self.assertEqual (-9, resutl)

    def test_add_two_zero (self):
        t = mathMethod ()
        resutl =t.add (0, 0)
        self.assertEqual (0, resutl)

    def test_add_two_flosts (self):
        t = mathMethod ()
        resutl =t.add (0.1,0.3)
        self.assertEqual (0.4, resutl)

if __name__ == '__main__':#执行函数入口
    unittest.main()







'''
#对这个类里面的加法去写测试用例
#1、一正一负相加
#2、正、负数、0、小数、类型、

#准备测试数据和期望结果
#1、1，2  3
#2、3，3  6
#3、-3，-6  -9

#利用python代码去写这个加法的测试用例
t=mathMethod()
t.add(1,2)#实际结果
t.add(3,3)
t.add(-3,-6)
t.add(0,0)
t.add(0.1,0.3)

#判断用例是否通过  pass   fail
if t.add(1,-2)==-1:
    print("pass")
if t.add(3,3)==-1:
    print("pass")
if t.add(-3,-6)==-1:
    print("pass")
if t.add(0,0)==-1:
    print("pass")
if t.add(0.1,0.3)==-1:
    print("pass")
'''















