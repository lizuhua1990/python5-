# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 22:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : calss_Lei_1.py
# @Software: PyCharm

#类的划分：一定是他们据有某些相同的属性 或这是特征
#这些相同的属性  特征  是谁决定的？ 谁规定的？
#函数里面也有类的，这个类是怎么做的呢？
#看python里面类的语法：
#关键字：class   类名（驼峰命名） 见明知意

#大佬的特征
#静态的：IQ=140   skillValue=100
#动态的：code think fly run

#静态的---已经声明的变量值
#动态的——变成函数

#类里面包含的属性值（变量值）函数：

class daLao:
    IQ=140#在某个范围内，不会写死的，属性值可能会进程变化
    skillValue=100

    def code(self,language,linse='1000'):#类里面的函数会多加一个self
        #类里面的函数用法  跟普通的函授是一模一样的
        print(self.IQ)#类函数里面要调用类的属性值的话  self.属性值名称
        print(language,"代码写的6666666")
        print("大佬一秒钟写",linse)

    def think(self):
        print("大佬会思考！思考66666")

    def fly(self):
        print("大佬会思考，写代码又好，可以装逼可以飞6666！")

#对象====类中的某一个个体
#uix不是本来就存在的，类他也不是本来就存在  都是需要我们人为去创建的
#需要根据泪来创建你所需要的个体====对象
#创建对象   实例:
t = daLao()#这就是根据类创建的一个实例

#既然是实例=对象   我刚刚创建的这个t
print("大佬的t是IQ是：",t.IQ)#实例的可以直接调用类里面的属性值
print("大佬t的技能值是：",t.skillValue)

t.code("java",100)#这就是根据类创建的一个实例
t.fly()
t.think()


class zhaZha:
    pass




























