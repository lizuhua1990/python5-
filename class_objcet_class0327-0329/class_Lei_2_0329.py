# -*- coding: utf-8 -*-
# @Time    : 2018/3/30 13:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_Lei_2_0329.py
# @Software: PyCharm


#写一个类： 学生类   属性值你们自己定
#函数：写作业  唱歌
#要求写一个实例，并且调用类立马的属性值和方法

class students():
    '''
    sex="女"
    hight=168
    grade="python5"
    age=18
    '''
    def __init__(self,age,grade):#这是初始化函数，
        # 创建对象的时候同步传入初始化参数
        self.age=age
        self.grade=grade

    def writeHomework(self):
        #print("写作业是学生的天职！")
        #print(self.age)#调用的
        print("我在写"+self.grade+"期的作业")
        print("我今年"+self.age+"岁")


    def sing(self):
        print("会唱歌的人都长得很漂亮！")

t=students('16','prthon5')
#print(t.age,t.sex,t.hight,t.grade,)
t.writeHomework()
t.sing()


s=students('20','java4')
s.writeHomework()

