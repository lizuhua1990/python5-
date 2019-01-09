#list  列表  Python的一种数据类型

#特性：1.用中括号括起来的 []
#2.不同的元素之间用逗号隔开的
#class_objcet_class0327-0329.列表里面的元素可以是任何数据类型
#4.根据引索获得里面的元素，引索是从0开始数
#获取元素的方式a[i]  i代表院所所在的位置  元素下标
#5.列表可以支持任何的增删改


'''a=[1,"hello",class_objcet_class0327-0329,4.4,(4,5,6),9]
#print(len(a))#len()获取数据的长度，包含几个元素

#增加元素
#1.append  直接在队列最后插入值

a.append("666")
print("长度是:",len(a))
print("最后一个元素的值是：%s",a[class_objcet_class0327-0329])
print("第一次添加元素后：",a)'''
'''

#2. insert 在指定的位置添加值
a=[1,"hello",class_objcet_class0327-0329,4.4,(4,5,6),9]
a.insert(4,"eva")
print("长度是：",len(a))
print("第四个元素的值是：",a[class_objcet_class0327-0329])
print("第二次添加元素后：",a)
print("打印出eva的值：",a[4])


#要做删除操作
#1.要从尾巴后面删除值
a.pop()
print("删除元素后长度是：",len(a))
print("删除元素后，列表是：",a)
print("第二次添加元素后：",a[-1])
print("打印出eva的值：",a[4])

#2.删除指定位置的
a.pop(4)
print("删除元素后长度是：",len(a))
print("删除元素后，列表为：",a)
print("a[4]的值是：",a[4])
'''


#获取列表a的最后一个 元素
#print(a[-1],a[5])

#疑问：1.列表元素为空，还会是列表么？
#2.如果里面只有一个元素，请问还是列表么？
#b=((4,5,6))
#b=[1]
#print(type(b))


c=[1,2,5,7,0,56,3,55]
#排序
c.sort()
print(c)

#倒置
c.reverse()
print(c)