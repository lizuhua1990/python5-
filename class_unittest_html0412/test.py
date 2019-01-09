# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 14:02
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.txt.py
# @Software: PyCharm

class Student:
    def __init__(self,a=8,b=7):#这是初始化函数，当有默认值的时候可以不传
        # 创建对象的时候同步传入初始化参数
        self.a=a
        self.b=b
    def test_get(self):
        print("hello world!",self.a + self.b)

if __name__ == '__main__':
    Student(5,7).test_get()#类里面有变量，要传入值