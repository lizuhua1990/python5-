# -*- coding: utf-8 -*-
# @Time    : 2018/5/4 14:59
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : datetime.py
# @Software: PyCharm

'''
import datetime
while True:
    try:
        print(datetime.datetime(*map(int,input().split())).strftime("%j").lstrip("0"))
    except:
        break

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
year, month, day = map (int, input ().split ())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days[2] = 29

summ = 0
for i in range (0, month):
    summ += days[i]

print (summ + day)
'''


print(sum(map(int,input().split())))



