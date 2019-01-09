# -*- coding: utf-8 -*-
# @Time    : 2018/class_objcet_class0327-0329/26 20:50
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : 9_9list.py
# @Software: PyCharm

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        product = i * j
        if j>1 and product < 10:
            product = str(product) + '  '
        else:
            product = str(product) + ' '
        print(str(j)+ "*"+ str(i)+ "="+ str(product),end=' ')
    print()


for i in range(1,10):
    for j in range(1,i+1):
        print (str (j) + "*" + str (i) + "=" + str (i*j)+ '\t', end='')#  \t  制表符
    print()


for i in range(1,10):
    for j in range(1,10):
        if i>j:
            line = '{} {} {:<4}'.format('     ','','')
        else:
            line = '{} * {} ={:<4}'.format(i,j,i*j)
        print(line,end = '')
    print()

for i in range(1,10):
    print(" "*10*(i-1),end='')
    for j in range(i,10):
        print('{0}*{1}={2:<6}'.format(i,j,i*j),end='')
    print()



#菱形打印
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
for i in range(-3,4):
    if i<0:
        prespace = -i
    else:
        prespace = i
    print(' '*prespace + '*'*(7-prespace*2))

'''
   $
  $$
 $$$
$$$$$$$
   $$$
   $$
   $
'''
for i in range(-3,4):
    if i<0:
        print(' '*(-i)+'$'*(4+i))
    elif i>0:
        print(' '*3+"$"*(4-i))
    else:
        print('$'*7)


#斐波那契数列

def shuLie(a,b,num):
    '''
    for i in range(1,num):
        c=a+b
        a=b
        b=c
        if c<num:
            print(c)'''
    if num ==1 and num == 0:
        print('0')
    while a<num:
        a,b=b,a+b
        print(a,end=',')
    exit()
shuLie(a=0,b=1,num=int(input("打印截止长度：")))