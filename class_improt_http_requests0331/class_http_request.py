# -*- coding: utf-8 -*-
# @Time    : 2018/3/31 15:55
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_http_requests.py
# @Software: PyCharm

import requests

url='http://www.baidu.com'
#  get 请求
request=requests.get(url)

#看结果  把结果写到txt里面去
print(request.status_code)#查看状态
print(request.encoding)#看编码
file = open('http_result.txt','w+',encoding='utf-8')
file.write(request.text)
file.close()

#print(request.text)


# post 请求
requests.post(url)



