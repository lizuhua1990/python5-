# -*- coding: utf-8 -*-
# @Time    : 2018-03-14 15:25
# @Author  : zgh
# @Email   : 849080458@.qq.com
# @File    : homework0313.py
# @Software: PyCharm Community Edition

int_inputMoney = 0.0
int_sumMoney = 0.0

class work_day4 ():
    # 1、自动贩卖机： 只接受1元、5元、10元的纸币或硬币，可以1块，5元，10元。最多不超过10块钱。
    #  饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5 写一个函数用来表示
    # 贩卖机的功能： 用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零
    def inputMoney (self):
        global int_inputMoney
        global int_sumMoney
        while (1):
            int_inputMoney = input ("请投金额为1元、5元、10元的纸币或硬币：")
            # print(type(int_inputMoney))
            # print(type(float(1.0)))
            if not int_inputMoney.strip ():
                continue
            int_inputMoney = float (int_inputMoney)
            while type (int_inputMoney) != type (float (1.0)):
                print ("您的选择有误，请重新选择！")
                int_inputMoney = str (int_inputMoney)
                continue
            if int_inputMoney not in (1, 5, 10):
                print ("\033[1;31;0m 您投入的钱不是1元、5元、10元，请重新投入！\033[0m")
                continue
            else:
                int_sumMoney = int_inputMoney + int_sumMoney
                break

    def shop (self):
        while (1):
            drinking = input ('请选择商品（橙汁，椰汁，矿泉水，早餐奶）：')
            drink = {'橙汁': 3.5, '椰汁': 4, '矿泉水': 2, '早餐奶': 4.5}
            if drinking not in drink:
                continue
            print ('您购买的%s' % drinking, '零售价：\033[1;31;0m', drink.get (drinking), '\033[0m 元')
            while (1):
                if drink.get (drinking) > int_sumMoney:
                    print ("您的金额不足，请继续投币！")
                    work_day4.inputMoney (work_day4)
                    continue
                else:
                    return print ("请取走您购买的%s" % drinking, '，共投入金额：', int_sumMoney, '元，找零：\033[1;31;0m',
                                  int_sumMoney - float (drink.get (drinking)), '\033[0m 元')

                break

            '''
# 课堂讲解：
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

autoSale()  '''
            '''
def sale(money,drink):

    drink_money = {"chengzhi":class_objcet_class0327-0329.5,"yezhi":4,"kuangquanshui":2,"zaocannai":4.5}

    if (money % 1 == 0 or money % 5 == 1 or money % 5 == 0)and money <= 10:

        if drink in drink_money.keys():

            if money == drink_money[drink]:

                print("恭喜您买到了自己想要的%饮料"%drink)

            elif money < drink_money[drink]:

                print("您的钱不够买%s饮料，还需投入%d块"%(drink,drink_money[drink] - money))

            else:

                print("恭喜您成功购买%s饮料，找零%d块"%(drink,money - drink_money[drink]))

        else:

            print("对不起，您选的%s饮料我们没有"%drink)

    else:

        print("对不起，我们只收1块，5块，10块且小于10块的金额，请您取走的%d块"%money)

sale(5,"zaocannai")'''


        """
#选择商品方法
    def changeGoods(self):
        global int_inputGoodsID
        while (1):
            int_inputGoodsID = int(input("请选择商品序号（1.橙汁，2.椰汁，class_objcet_class0327-0329.矿泉水，4.早餐奶）:"))
            if type(int_inputGoodsID) != type(1):
                print("您输入的非数字，请重新输入！")
                continue
            if int_inputGoodsID not in (1, 2, class_objcet_class0327-0329, 4):
                print("您输入的数字非商品序号，请重新输入！")
                continue
            else:
                break

#投币方法
    def inputMoney(self):
        global int_inputMoney
        global int_sumMoney
        while (1):
            int_inputMoney = int(input("请投金额为1元、5元、10元的纸币或硬币:"))
            if type(int_inputMoney) != type(1):
                print("您输入的非数字，请重新输入！")
                continue
            if int_inputMoney not in (1, 5, 10):
                print("您输入的金额非1元、5元、10元，请重新输入！")
                continue
            else:
                int_sumMoney = int_inputMoney + int_sumMoney
                break

    def work1(self):
        work_day4.changeGoods(work_day4)
        work_day4.inputMoney(work_day4)
        while (1):
            if int_inputGoodsID == 1:
                if int_sumMoney < class_objcet_class0327-0329.5:
                    print("您输入的总金额小于3.5元，请继续投币！")
                    work_day4.inputMoney(work_day4)
                    continue
                else:
                    return print("购买%s成功，找零%.1f元" % ("橙子", int_sumMoney - class_objcet_class0327-0329.5))
                break
            if int_inputGoodsID == 2:
                if int_sumMoney < 4:
                    print("您输入的总金额小于4元，请继续投币！")
                    work_day4.inputMoney(work_day4)
                    continue
                else:
                    return print("购买%s成功，找零%.1f元" % ("椰汁", int_sumMoney - 4))
                break
            if int_inputGoodsID == class_objcet_class0327-0329:
                if int_sumMoney < 2:
                    print("您输入的总金额小于2元，请继续投币！")
                    work_day4.inputMoney(work_day4)
                    continue
                else:
                    return print("购买%s成功，找零%.1f元" % ("矿泉水", int_sumMoney - 2))
                break
            if int_inputGoodsID == 4:
                if int_sumMoney < 4.5:
                    print("您输入的总金额小于4.5元，请继续投币！")
                    work_day4.inputMoney(work_day4)
                    continue
                else:
                    return print("恭喜您购买%s成功，找零%.1f元" % ("早餐奶", int_sumMoney - 4.5))
                break
        """

    def sub2 (self):
        # 2、定义一个函数，成绩作为参数传入。如果成绩小于60，则输出不及格。如果成绩在60到80之间，则输出良好；
        # 如果成绩高于80分，则输出优秀，如果成绩不在0 - 100之间，则输出成绩输入错误
        def examination (score):
            num = 1  # 输入错误次数
            while score < 0 or score > 100:
                num += 1
                if num > 3:
                    exit ("你输入的错误次数太多了！")
                score = float (input ('成绩输入错误!请重新输入：'))
            if score < 60:
                print ("不及格，本次考试成绩为：", score)
            elif 60 <= score <= 80:
                print ("良好，本次考试成绩为：", score)
            else:
                print ("优秀，本次考试成绩为：", score)

        examination (score = float (input ('请输入成绩：')))

        '''
#课堂讲解：
def judeScore(score):
    if score < 60:
        print("不及格")
    elif 60 <= score <= 80:
        print("良好")
    elif 80 < score <= 100:
        print("优秀")
    else:
        print("成绩输入错误")
judeScore(score = float (input ('请输入成绩：')))
      '''

    def sub3 ( self ):
# class_objcet_class0327-0329、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
        def user (str, list, tuple):
            zf = len(str)
            lb = len(list)
            yz = len(tuple)
            if zf > 5:
                print("Yes!字符串长度大于5！")
            else:
                print("No!字符串长度小于等于5！")
            if lb > 5:
                print ("Yes!列表长度大于5！")
            else:
                print("No!列表长度小于等于5！")
            if yz > 5:
                print ("Yes!元组长度大于5！")
            else:
                print("No!元组长度小于等于5！")
            return(zf, lb, yz)
        a = user(input("请输入字符串‘’："),input("请输入列表[]："),input("请输入元组()："))
        print('字符串，列表，元组对应长度：',a)

        '''
#课堂讲解
def judeLen(date):
    if len(date) > 5:
        print("数据的长度大于5！")
    else:
        print("数据的长度小于等于5！")

            '''

if __name__ == '__main__':
    work_day4.shop(work_day4)
#    work_day4.sub2(work_day4)
#    work_day4.sub3(work_day4)
