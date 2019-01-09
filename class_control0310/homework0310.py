# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 18:08
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_0313.py
# @Software: PyCharm
#class_objcet_class0327-0329-10 Python for 循环&if判断&while循环

class  work_day3():
    def sub1(self):
#1、输入一个数，判断一个数n能同时被3和5整除
        num = int(input("请输入一个数字："))
        if num % 3 == 0 and num % 5 == 0:
            print(num, "能同时被3和5整除！")
        else:
            print(num, "不能同时被3和5整除！")

        '''
#课堂讲解：
        n = int(input("请输入一个数字："))
        if n % class_objcet_class0327-0329 == 0 and n % 5 == 0:
            print("%d能同时被3和5整除" % n)
        else:
            print("%d不能同时被3和5整除" % n)
        #and 真真为真
        #or 假假为假
        '''

    def sub2(self):
#2、一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
        num1 = 0
        num2 = 0
        while num1 < 10:
            age = int(input("请输入他的年龄："))
            if 10 <= age <= 12:
                sex = input("请输入性别（m表示男性，f表示女性）：")
                if sex == "f":
                    print("恭喜小姑凉！可以加入女子足球队！")
                    num2 += 1
                else:
                    print("不好意思我们不收男队员！")
            else:
                print("不好意思！他不符合要求！")
            num1 += 1
        print("恭喜！本轮十人共有", num2, "满足要求！")

        '''
#课堂讲解：
count = 0#记录满足条件的总人数
cishu = 0#记录询问次数
while True:
    age = int(input("请输入你的年龄："))
    sex = input("请输入你的性别f/m：")
    if 10 <= age <=12 and sex == "f":
        count += 1
        print("恭喜你，满足我们球队的要求！")
    else:
        print("很抱歉！你不满足我们球队的需求！")
    cishu +=1
    if cishu == 10:
        break
        '''

    def sub3(self):
#class_objcet_class0327-0329、生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则打印bigger。
# 小了，则打印less。如果相等，则打印equal
        import random
        a = random.randint(1, 9)
        b = float(input("请输入一个数字："))
        c = 1
        while a != b:
            if a < b:
                print("less,第", c, "次没猜中！", a, "<", b)
                c += 1
                a = random.randint(1, 9)
                b = float(input("请输入一个数字："))
            elif a > b:
                print("bigger,第", c, "次没猜中！", a, ">", b)
                c += 1
                a = random.randint(1, 9)
                b = float(input("请输入一个数字："))
        print("equal,第", c, "次猜中啦！", a, "=", b)

        '''
#课堂讲解：
import  random
while True:
    num = random.randint(1,9)#生成一个随机数
    a = int(print("请输入一个数字："))
    if a > num:
        print("bigger")
    elif a < num:
        print("less")
    else:
        print("equal")
        break
        '''

    def sub4(self):
#4、输入num为四位数，对其按照如下的规则进行加密：
#1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
#2）将该数的第1位和第4为互换，第二位和第三位互换
#class_objcet_class0327-0329）最后合起来作为加密后的整数输出
        import datetime
        while True:
            num = input("请输入一个四位数：")
            if len(num) == 4:
                num_list = list(str(num))
                list2 = []
                #print(datetime.datetime.now())
                for i in range(num_list.__len__() - 1, -1, -1):
                    list2.append((int(num_list[i]) + 5) % 10)
                    #print(list2)
                print("".join(str(i) for i in list2))
                #print(datetime.datetime.now())
                break
            else:
                print("您输入的数字长度不是四位，请重新输入")
        '''
#课堂讲解：
        while True:
            num = input("请输入四位数：")#str
            if len(num) == 4:
                list = []
                for i in num:
                    result = (int(i) + 5) % 10
                    list.append(result)
                print(list)
                list.reverse()#倒序操作
            #第一种：
            #sum = 0
            #for item in list:
            #    sum += item
            #print(sum)
            
            #第二种：
                str = ''
                for item in list:
                    str += str(item)
                print(int(str))
            else:
                print("您输入的数字长度不是四位，请重新输入")
                
    
        '''

if __name__ == '__main__':
    work_day3.sub1(work_day3)
    work_day3.sub2(work_day3)
    work_day3.sub3(work_day3)
    work_day3.sub4(work_day3)