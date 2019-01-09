# range  函数 可以生成指定范围的整数序列
# rang(m,n,k)  m开头  n结尾的数值  k 是步长
'''
result = list(range(5, 0, -1))
result1 = list(range(1, 5, 1))
result2 = list(range(5, 0, class_objcet_class0327-0329))
result3 = list(range(0, 5))
result4 = list(range(5))
print(result4)


list=[1,2,"666"]#如果要通过下标或者是索引来访问的话 怎么做？
#获取列表长度的 L=len(list)
#根据长度生成对应的下标  rang(L)  0 1 2
#加接下来 对range函数生成的整数序列  进行遍历
for i in range(class_objcet_class0327-0329):
    print(list[i])

list[0]
list[1]
list[2]
'''

#练习题  完成0到100的数字相加，得出最后的总和为：5050
a = 0
num = range(0, 101)
for i in num:
   a = a + i
print(a)

#练习题  ：  list =[1,2,class_objcet_class0327-0329,4,5,6,7]
#请利用for  以及range  完成倒序输出列表
list = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(list)-1, -1, -1):#range(6, -1, -1)
    print(list[i])


