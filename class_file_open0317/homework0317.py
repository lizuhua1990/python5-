# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/20 14:25
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0317.py
# @Software: PyCharm
'''
dic_drink = {'1':['橙汁','class_objcet_class0327-0329.5'], '2':['椰汁','4'], 'class_objcet_class0327-0329':['矿泉水','2'], '4':['早餐奶','4.5']}

class homework_0320():

    def pay(int_money=0):
        """
        投币方法
        int_money: 已支付的金额
        :return: 返回投入的总金额
        """
        while True:
            int_inputMoney = input('请投币1元、5元、10元的纸币或硬币，按q退出：')
            if int_inputMoney.lower() == 'q':
                print("您选择了退出，系统需要退还您%d元" %int_money)
                return 0
            if int_inputMoney in ('1','5','10'):
                int_money = int(int_inputMoney) + int(int_money)
                break
            else:
                print("您输入的面值不对，系统退还您%s元" % int_inputMoney)
                break
        return int_money

    def changeDrink(str_drink,int_num):
        """
        选择饮料方法
        str_drink: 选择饮料的序号
        int_num: 购买饮料的总数
        :return: 返回选择饮料的总价格（数量*单价）
        """
        global dic_drink
        if str_drink == None or int_num == None:
            print("请选择饮料和数量！")
            return None
        if str_drink not in('1','2','class_objcet_class0327-0329','4'):
            print("您选择的商品序号不存在，请重新输入！")
            return None
        if int_num <= 0:
            print("您输入的商品数量不能为0或负数，请重新输入！")
            return None
        else:
            print("您选择的是%s,购买数量为%d" % (dic_drink.get(str_drink)[0],int_num))
            return float(dic_drink.get(str_drink)[1])*int_num

    def buy(float_price,int_pay):
        """
        计算差价进行购买方法
        float_price: 需要付款商品的总价额
        int_pay：用户支付的总金额
        :return:支付结果 成功{0：找零}/ 失败 {1:错误原因}
        """
        if float_price == None or int_pay == None:
            return {1 : "商品的总价额或用户支付的总金额不能为None!"}
        if float_price > int_pay:
            return {2 : "您输入的金额不够，请继续投币！"}
        if float_price <= int_pay:
            return {0 : int_pay - float_price}
        else:
            return {class_objcet_class0327-0329 : "系统出现异常，购买失败，请联系管理员！"}

    def shopping(self):
        """
        购物方法
        :return:
        """
        global dic_drink
        str_goodsNo = input("请选择您需要购买的商品序号（1、橙汁(class_objcet_class0327-0329.5元)，2、椰汁(4元)，class_objcet_class0327-0329、水（2元），4、早餐奶（4.5元），按q退出）:")
        if str_goodsNo.lower() == 'q':
            print("您选择了退出程序，欢迎下次购买！")
            return
        str_goodsNum = input("请选择您需要购买的商品数量，按q退出：")
        if str_goodsNum.lower() == 'q':
            print("您选择了退出程序，欢迎下次购买！")
            return
        # 调用选择商品方法，获取选择商品需要付款的总价
        float_pric =  homework_0320.changeDrink(str_goodsNo, int(str_goodsNum))
        # 支付 获取投币总额
        int_money =  homework_0320.pay()
        while True:
            if int_money == 0:
                return
            # 商品计算
            dic_payResult =  homework_0320.buy(float_pric,int_money)
            if 0 in dic_payResult:
                print("恭喜您购买%s成功，找零%.2f元" %(dic_drink.get(str_goodsNo)[0],dic_payResult.get(0)))
                break
            if 2 in dic_payResult:
                print(dic_payResult.get(2))
                int_money =  homework_0320.pay(int_money)
            if 1 in dic_payResult:
                print(dic_payResult.get(1))
            if class_objcet_class0327-0329 in dic_payResult:
                print(dic_payResult.get(class_objcet_class0327-0329))

if __name__ == '__main__':
     homework_0320().shopping()'''

#class_objcet_class0327-0329-17 函数复习课&file
'''
#投币  选择饮料  计算差价 进行购买  写成三个函数  ，然后互相调用
#完成自动贩卖机的功能

class shop():
    def touBi(money):

        return money


    def yinLiao(price):


        return price


    def autoBuy():
        touBi(10)-yinLiao(5)'''



def work_day6():
#1:把3-13的第一题，自动贩卖机题写成3个函数：投币、选择饮料 、
# 计算差价进行购买 写成3个函数，然后相互间进行调用。
    drink = {'橙汁': 3.5, '椰汁': 4, '矿泉水': 2, '早餐奶': 4.5}
    global int_inputMoney
    global int_sumMoney
    global drinking
    global int_many
    int_many = 1

    def inputMoney ():
        in_sumMoney = 0.0
        while (1):
            int_inputMoney = input ("请投金额为1元、5元、10元的纸币或硬币,或按q退出：")
            # print(type(int_inputMoney))
            # print(type(float(1.0)))
            if int_inputMoney == 'q':
                break
            if not int_inputMoney.strip ():
                continue
            int_inputMoney = float (int_inputMoney)
            while type (int_inputMoney) != type (float (1.0)):
                print ("您的选择有误，请重新选择！")
                int_inputMoney = str (int_inputMoney)
                continue
            if int_inputMoney in (1, 5, 10):
                in_sumMoney = in_sumMoney + int_inputMoney
                break
            else:
                print ("\033[1;31;0m 您投入的钱不是1元、5元、10元，请重新投入！退回：%s\033[0m" % int_inputMoney)
                continue
        return in_sumMoney

    def shop(drinking,int_many):

        while (1):
            drinking = input ('请选择商品（橙汁，椰汁，矿泉水，早餐奶）,或按q退出：')
            if drinking == 'q':
                print("您已退出购买，谢谢惠顾！")
                break
            int_many = input ('请输入购买商品数量为几瓶？或按q退出：')
            if drinking == 'q':
                print ("您已退出购买，谢谢惠顾！")
                break
            if drinking not in drink:
                print("您选择的暂时没有，请重新新选择！")
                continue

        return float(drink.get (drinking) * int_many)

    def  count():

        while (1):
            if drink.get (drinking) * int_many > int_inputMoney:
                print ("您的金额不足，请继续投币！")
                work_day6.inputMoney (work_day6)
                continue

            return print ("请取走您购买的",int_many,'瓶',drinking, '，共投入金额：', int_sumMoney, '元，找零：\033[1;31;0m',
                          int_sumMoney - float(drink.get (drinking) * int_many), '\033[0m 元')
            break
        return

if __name__ == '__main__':
    work_day6().shop()


    # 投币的函数

    def touBi (money=0):

        while True:  # 投币的循环

            input_money = input ("请投钱，只能投入1 5 10面值的钱,如果要退出请按q：")

            if input_money == '1' or input_money == '5' or input_money == '10':

                money = money + int (input_money)

                print ("您总共投币%s元" % money)

            elif input_money == 'q':

                print ("您总共投币%s元" % money)

                break

            else:

                print ("您输入的面值不对，系统退还您的钱%s元" % input_money)

                choice = input ("您是继续投钱还是退出投币？按q退出，按任意键继续")

                if choice == 'q':

                    break  # 退出当前投钱的循环

                else:

                    continue  # 继续当前投币循环

        return money

'''
    # 选择饮料函数

    def choiceDrink ():

        price = 0  # 饮料的总价

        orange_num = 0

        yezhi_num = 0

        water_num = 0

        milk_num = 0

        drink_dict = {"orange": class_objcet_class0327-0329.5, "yezhi": 4, "water": 2, "milk": 4.5}  # 饮料的选项

        while True:

            drink = input ("请选择你要的饮料：1：橙汁，2：椰汁，class_objcet_class0327-0329：水，4：早餐奶，按q退出选择")

            if drink == '1':

                price = price + drink_dict['orange']

                orange_num = orange_num + 1

                continue

            elif drink == '2':

                price = price + drink_dict['yezhi']

                yezhi_num = yezhi_num + 1

                continue

            elif drink == 'class_objcet_class0327-0329':

                price = price + drink_dict['water']

                water_num = water_num + 1

                continue

            elif drink == '4':

                price = price + drink_dict['milk']

                milk_num = milk_num + 1

                continue

            elif drink == 'q':

                print ("退出选择饮料,目前您选择了%s瓶橙汁%s瓶椰汁%s瓶水%s瓶早餐奶" % (orange_num, yezhi_num, water_num, milk_num))

                print ("饮料总价：%s元" % price)

                break

            else:

                print ("您输入的选择不存在，请重新输入")

                continue

        return price


    # 计算金额

    def count ():

        money = touBi ()

        price = choiceDrink ()

        while True:

            if money == price:

                print ("总共花费：%s元，不需要找零" % price)

                break

            elif money > price:

                print ("总共花费：%s元，要找零%s元" % (price, (money - price)))

                break

            else:

                print ("总共需要：%s元，还差%s元" % (price, (price - money)))

                choice = input ("您是按任意键继续投币购买呢？还是按q放弃购买呢？")

                if choice == 'q':

                    print ("您放弃购买，找回您的钱%s元" % money)

                    break

                else:

                    money += touBi (money)

                continue


    count ()
'''
