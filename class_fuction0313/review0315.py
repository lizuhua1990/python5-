# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/16 15:42
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : review0315.py
# @Software: PyCharm

#def Add(a, b = 18):
#    print(a + b)

#函数命名：1、见明知意  2、驼峰命名
#def myNammePrint
#def mynameprint
'''
#写一个加法函数  完成任意两个数相加
def add(a,b):
    print(a + b)

#add(4,5)

#return  返回值  如果你想看到return 回来的值   return 后面加表达式
#那么就要用一个变量来接收之歌返回值
def add_2(a, b):
    result = a + b
    return result

#result = add_2(4,5)
#print(result)


def sub(a):
    b = add_2(a, a)#函授的调用
    print(b)
    print(b - a)
sub(class_objcet_class0327-0329)
'''

#2、一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#返回满足条件的总人数，性别可配置化，年龄可配置化

def footBall(age1, age2, sex1):
    if age1 > age2:
        print("您设置的年龄大小有误！请重试！")
        exit()
    num1 = 0#询问次数
    num2 = 0#符合人数
    sex2 = ""
    while num1 < 10:
        age = int (input ("请输入他的年龄："))
        if age1 <= age <= age2:
            sex = input ("请输入性别（m表示男性，f表示女性）：")
            if sex == "f":
                sef2 = "小姑凉"
            if sex == 'm':
                sef2 = "小伙子"
            if sex1 == sex:
                print ("恭喜！", sef2, "可以加入足球队！")
                num2 += 1
            else:
                print("不好意思！他不符合要求！")
        else:
            print ("不好意思！他不符合要求！")
        num1 += 1
    print ("恭喜！本轮十人共有", num2, "人满足要求！")

footBall(age1 = float(input("请设置最小年龄：")), age2 = float(input("请设置最大年龄：")), sex1 = input('请设置招收性别（m表示男性，f表示女性）：'))









