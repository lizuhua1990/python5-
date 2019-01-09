# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 23:03
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0327.py
# @Software: PyCharm


#作业：写一个超人类，属性值以及动态的技能，你自己定！ 或者你可以拓展~~
# 你自己随便写个类也是OK的。

class superMan:
    high=199
    weight=180

    def code(self):
        print("身披金属铠甲")

    def arms(self):
        print("手持无极射线")

    def Partner(self):
        print("身边还有一个女超人！")

if __name__ == '__main__':
    superMan.code(superMan)
    superMan.arms(superMan)
    superMan.Partner(superMan)




'''
str_name = "超人"
int_age = 18
list_hobby = ["打怪兽","吃吃吃","看书","打球"]

class superMan():

    def daguaishou(self):
        print("%d岁的%s喜欢的爱好有:%s"%(int_age,str_name,list_hobby))

    def groupUp(int_age):
        list_hobby.append("谈恋爱")
        print("%s成长到了%d岁，爱好有：%s"%(str_name,int_age,list_hobby))

    def changeName(self,str_changName):
        global str_name
        str_name = str_changName
        print("超人把自己名字改成了%s" %(str_name))

superMan.daguaishou(superMan)
superMan.groupUp(20)
superMan.changeName(superMan,"超超超超人")
'''