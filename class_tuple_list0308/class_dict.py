#dict  字典   Python的第二常用的一种数据类型  dictionary

#特性：
#1.用花括号  大括号括起来的  ｛｝
#2.不同的元素之间用逗号隔开的
#class_objcet_class0327-0329.列表里面的元素可以是任何数据类型
#4.字典是键值对形式的数据  我们根据key（键）去找值
#5.字典可以支持任何的增删改


#获取元素的值
#print(a["name"])
#print(a['age'])

#key可以相同吗？
#key是唯一的，不能相同，会被覆盖替换

#增加元素 字典没有的key值
#a['address']='css'
#print(a)

#修改元素的值
#a["sex"]='boy'
#print(a['sex'])
#print(a)

#我们新增元素的时候   如果key值已经存在  那么就是修改key对应的value
#如果key 不存在  则新增一个key-value值
'''
#添加元素后，排序变了  怎么插入第二个位置
a={"name":"苗疆","job":"leader","sex":"girl","age":18}

#做删除操作 pop 删除某个指定的元素
a.pop("job")
print(a)'''


#问题：
a=[1,2,3,'text',]#有序
b=[7,6,8,9,'text2']#有序
c={"name":"苗疆","job":"leader","sex":"girl","age":18}


#数据类型 到底是有序还是无序的？
print(a)
print(b)
print(c)
print(c.keys())
print(c.items())