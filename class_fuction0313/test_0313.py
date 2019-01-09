# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 18:08
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_0313.py
# @Software: PyCharm


#为什么要命名变量
#变量引用前为啥要申明一下
#格式也要正确，层级关系要搞清楚
#
'''
a = 11
#while True:
while a > 10:#while 判断条件满足情况下，为真  执行下去
    #a = int(input("请输入你的数字："))
    if a > 5:
        print("a大于5")
    else:
        print("a小于5")
        break
        '''



# 课堂讲解：
'''
def autoSale ():
    money = 0
    orange_num = 0
    yezhi_num = 0
    water_num = 0
    milk_num = 0
    drink_dict = {"orange": class_objcet_class0327-0329.5, "yezhi": 4, "water": 2, "milk": 4.5}  # 饮料
    while True:
        while True:  # 投币循环
            input_money = input ("请投入1、5、10面值的钱,退出请按q：")
            if input_money == '1' or input_money == '5' or input_money == '10':
                money = money + int (input_money)
                print("您总共投币%s"%money)
            elif input_money=="q":
                print("投币结束，请按任意键投币或按q退出！")
                break
            else:
                print("您输入的面值不对，系统退还您的钱%s" % input_money)
                choice = input ("您输入的面值不对，按任意键重新投币或者按q退出！")
                if choice == 'q':
                    break  # 退出当前投钱循环
                else:
                    continue  # 继续当前循环

        #开始买饮料
        while True:
            drink=input("请选择你要的饮料：1、橙汁，2、椰汁，class_objcet_class0327-0329、水，4、早餐奶，按q退出")
            if drink=="1":
                price = price + drink_dict['orange']
                orange_num=orange_num+1
                continue
            elif drink=="2":
                price = price + drink_dict['yezhi']
                yezhi_num=yezhi_num+1
                continue
            elif drink=="class_objcet_class0327-0329":
                price = price + drink_dict['water']
                water_num=water_num+1
                continue
            elif drink=="4":
                price = price + drink_dict['milk']
                milk_num=milk_num+1
                continue
            elif drink=='q':
                print("退出选择饮料，目前您选择了%s瓶橙汁%s瓶椰汁%s瓶水%s早餐奶"%(orange_num,yezhi_num,water_num,milk_num))
                print("选择的饮料总价;%s元"%price)
                break
            else:
                print("您输入的选择不存在，请重新输入")
                continue

        #计算金额
        if money == price:
            print("您购买了%s瓶橙汁%s瓶椰汁%s瓶水%s早餐奶"%(orange_num,yezhi_num,water_num,milk_num))
            print("总共花费：%s元"%price)
        elif money>price:
            print ("您购买了%s瓶橙汁%s瓶椰汁%s瓶水%s早餐奶" % (orange_num, yezhi_num, water_num, milk_num))
            print ("总共花费：%s元,还差%s元" % (price, (price - money)))
        else:
            print ("您购买了%s瓶橙汁%s瓶椰汁%s瓶水%s早餐奶" % (orange_num, yezhi_num, water_num, milk_num))
            print ("总共花费：%s元,还差%s元" % (price, (price - money)))
            if choice =='q':
                print("您放弃购买，找回你的钱%s"%money)
                break
            else:
                continue

autoSale()'''

#投币  选择饮料  计算差价 进行购买  写成三个函数  ，然后互相调用
#完成自动贩卖机的功能

class shop():
    def touBi(money):

        return money


    def yinLiao(price):


        return price


    def autoBuy():
        touBi(10)-yinLiao(5)



if __name__ == '__main__':
    shop.autoBuy(shop)































