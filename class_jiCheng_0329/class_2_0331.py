# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 19:47
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_2.py
# @Software: PyCharm


#继承
class A:
    def printA(self):
        print("A")
        print("B")
        print("C")
#部分继承  我们该写了父类里面的函数。  那么子类的实例  调用的是子类的函数不能在调用父类的函数
#改写====重写

#class B(A):
#    def printA(self):
#        print("a")

#大招：你的我也要   但我又要有自己的个性
#超继承
class B(A):
    def printA(self):
        super(B,self).printA()
        print("a")

t=B()
t.printA()


#==============================
class Methoh_1:
    def add(self,a,b):
        print("两数之和",a+b)

#部分继承  改写了、重写了add函数
class Methoh_2(Methoh_1):
    def add(self,a,b,c):
        super(Methoh_2,self).add(a,b)
        #print ("两数之和", a + b)
        print("三数之和",a+b+c)

t=Methoh_2()
t.add(3,4,5)