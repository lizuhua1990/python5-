#for 循环 他的作用 就是对元素进行一个遍历
#对数据集合  （字符串 列表 元组 字典）  里面的元素一次访问

str="hello"
for item in str:
    print(item)

list = [1, 2, 3, 4, "666"]
for item in list:
    print(item)


dict={"age:": 5, "sex:":"girl"}
for item in dict:
#对key 进行 遍历 然后取值按key判断
    print(dict[item])
