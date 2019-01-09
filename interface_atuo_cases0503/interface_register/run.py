# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 20:52
# @Author  :
# @Email   :
# @File    : run.py
# @Software: PyCharm


import requests
import os
from interface_atuo_cases0503.public.config import config
from interface_atuo_cases0503.public.readExcel import readExcel
from interface_atuo_cases0503.public.writeExcel import writeExcel

url = config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'http.conf', 'HTTP', 'url')
#print (url)
h = readExcel (os.path.dirname (os.getcwd ()) + '/test_data/' + 'testcases.xlsx', 'test_cases','init')
data=h.read_Excel()
t=writeExcel(os.path.dirname (os.getcwd ()) + '/test_data/' + 'testcases.xlsx', 'test_cases')
print (data)
mode = config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'case.conf', 'FLAG', 'mode')
#print(mode)
list=[]


try:
    if mode==0:
        ID=config ().read_config (os.path.dirname (os.getcwd ()) + '/conf/' + 'case.conf', 'FLAG', 'case_list')
        #print (ID)

    #for ii in range(len(data)):
        for i in data:
            #print(i)
            if i['id'] in ID:
                #print(i)
                data=list.insert(len(data)-1,i)
                #print(list)
                data=list
                #print(data)

    for i in range(len(data)):
        request=requests.get(url,data[i]['data'])
        result=request.json()
        #print (result)
        #print (data[i]['data'])
        #写入excel数据
        t.write_Excel( i + 2, 4, result['code'])
        #result
        if int(result['code'])== data[i]['code']:
            t.write_Excel( i + 2, 5, 'pass')
        else:
            t.write_Excel (i + 2, 5, 'fail')
        #result
        t.write_Excel( i + 2,6, result['msg'])
except Exception as e:
    print('出错了')
    raise e














