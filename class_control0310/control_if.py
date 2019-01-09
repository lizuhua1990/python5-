#红灯停 绿灯行 黄灯等
#根据什么来约束人 偶然车的行为 ，起到一个分支分流的作用
#灯的演示来判断

'''
color=input("请输入等的颜色：")
if color=='red':
    print("请停车！")
elif color=='yellow':
    print("请等一等！")
elif color=='green':
    print("你可以通过了！")
else:
    print("你是色盲么！")
'''


#1、一家商场在降价促销。
# 如果购买金额50-100元(包含50元和100元)之间，
# 会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格

price = float(input("请输入金额："))
if 50 <= price <= 100:
    print("你折扣价格是：%.2f"%(price*(1-0.1)))
elif price > 100:
    print("你的折扣价格是：%.2f"%(price*(1-0.2)))
else:
    print("没有优惠，没钱别买！ %.2f " %price)
