# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/14 18:08
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test_0313.py
# @Software: PyCharm


class work_day2():
    def sub1(self):
        L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa'] ]
#打印Apple、Python、Lisa
        print(L[0][0],L[1][1],L[2][2])

    def sub2(self):
#合并下面的两个list并去重（去重可以使用set函数）
        list1 = [2,3,8,4,9,5,6]
        list2 = [5,6,10,17,11,2]
        a=list1+list2
        print(set(a))

    def sub3(self):
#完成数据从大到小的排序，大的放在前面，小的放在后面
        a=[44,88,1,3,100,67,56]
        #b=sorted(a)
        #print(b[::-1])
        a.sort()
        a.reverse()
        print(a)

if __name__ == '__main__':
    work_day2.sub1(work_day2)
    work_day2.sub2(work_day2)
    work_day2.sub3(work_day2)