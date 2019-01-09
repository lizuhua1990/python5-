# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 14:19
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_1.py
# @Software: PyCharm


class students():

    sex="女"
    hight=168
    grade="python5"
    age=18

    def __init__(self,age,grade):#这是初始化函数，
        # 创建对象的时候同步传入初始化参数
        self.age=age
        self.grade=grade

    def writeHomework(self):
        #print("写作业是学生的天职！")
        #print(self.age)#调用的
        print("我在写"+self.grade+"期的作业")
        print("我今年"+self.age+"岁")
        print("我是父类，我改啦函授")

    def sing(self):
        print(self.age+"会唱歌的人都长得很漂亮！")


#继承
#1、全继承
class B(students):
    pass
#2、部分继承   我只继承一部分，重写函数 函数名不变  其他随意
class C(students):
    def sing(self):#继承
        print("我唱的歌简直难听死啦，五音不全")

    def dance(self):
        print("我的跳舞也很好")

f=students('19','python5')
f.writeHomework()
f.sing()

print("=============================")
t=C('16','6年级')
t.sing()
t.writeHomework()

#改写=重写
#多继承：有多个父类
class add_1:
    def add(self):
        print("我是第一个加法")

class add_2:
    def add(self):
        print("我是第二个加法")

class add(add_1,add_2):#这个是子类
    pass

t=add()
t.add()

















