# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 22:28
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.txt.py
# @Software: PyCharm

'''
def func (i):
    j, tmp = 2, []
    while j * j <= i:
        while i % j == 0:
            tmp.append (j)
            i /= j
        j += 1
    if i > 1:
        tmp.append (1)
    return tmp


while 1:
    try:
        N = int (input ())
        if N == 0:
            break
        values = map (int, input ().split ())
        for i in values:
            num = 1
            tmp = func (i)
            for k in set (tmp):
                num *= tmp.count (k) + 1
            print (num)
    except:
        break

a=input()
if "C" in a:
    F= float(a.strip('C'))*1.8+32
    print("F%.2f"%F)
if "F" in a:
    C= (float(a.strip('F'))-32)/1.8
    print ("C%.2f"%C)


#二叉树遍历
def stree (num):
    list_1 = []
    for i in num:
        if i == '#' and len (list_1) != 0:
            print (list_1.pop (), end=' ')
        else:
            list_1.append (i)
if __name__ == '__main__':
    while True:
        try:
            num = input ()
            stree (num)
        except:
            break
#数组最大值、最小值
while True:
    try:
        n=int(input())
        num=list(map(int,input().split()))
        print(max(num),min(num))
    except:
        break


#0~9的a.b.c三个数abc+bcc=532
for a in range(0,5):
    for b in range(0,5):
        for c in range(0,9):
            if (a+b)*100+(b+c)*10+2*c==532:
                print(a,b,c)


# N<k时，root(N,k) = N，否则，root(N,k) = root(N',k)。N'为N的k进制表示的各位数字之和。
# 输入x,y,k，输出root(x^y,k)的值 (这里^为乘方，不是异或)，2=<k<=16，0<x,y<2000000000，
# 有一半的测试点里 x^y 会溢出int的范围(>=2000000000)
def root (x, y, k):
    temp = 1
    while y:
        # 相当于y%2
        if y & 1 == 1:  # 当是奇数时
            temp = (temp * x) % k
        x = (x * x) % k
        y = y >> 1
        temp = temp if temp else k
    return temp


if __name__ == '__main__':
    while True:
        try:
            x, y, k = map (int, input ().strip ().split ())
            print (root (x, y, k - 1))

        except:
            break

#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '23'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()

'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


time.sleep(2)
driver.quit()


class name:
    def myclass(self):
        print('你的民族是中华名族！')

