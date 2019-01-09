#循环  while循环
#如果只执行一次while循环怎么办

#while True:
#    print("我要上天~~~！")
#   break


#练习题：
#通过控制台输入一个大于10 的数字，利用while判断 执行减一操作

#a=int(input("请输入一个数字："))
#while a>10:
#     print(a)
#     a-=1

#练习：
#用一个数字， num_1来记录女学生的个数，当女学生的个数大于5的时候停止循环
#通过控制台输入学生的性别，当性别为F 为女生， 为M为男生

num_1=0
while num_1<=5:
    sex=input("性别F/M:")
    if sex=="F":
        num_1+=1
        print("当前女生个数：",num_1)
        if num_1>5:
            break
