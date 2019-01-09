# -*- coding: utf-8 -*-
# @Time    : 2018/5/15 14:42
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : html_login.py
# @Software: PyCharm
'''
登录：
POST https://www.ketangpai.com/UserApi/login HTTP/1.1
Host: www.ketangpai.com
Connection: keep-alive
Content-Length: 50
Accept: application/json, text/javascript, */*; q=0.01
Origin: https://www.ketangpai.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.ketangpai.com/User/login.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=3papndcqsfcscft7a2087eh6g3

email=18668162176&password=Admin!989898&remember=1

考勤：
GET https://www.ketangpai.com/SummaryApi/attence?courseid=MDAwMDAwMDAwMLOGx5WIubts HTTP/1.1
Host: www.ketangpai.com
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
Referer: https://www.ketangpai.com/StudentsV2/classDetail/courseid/MDAwMDAwMDAwMLOGx5WIubts.html
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8
Cookie: PHPSESSID=3papndcqsfcscft7a2087eh6g3; ketangpai_home_remember=think%3A%7B%22username%22%3A%22MDAwMDAwMDAwMLOGy5aHz82whc5-3LLfkZ4%22%2C%22expire%22%3A%22MDAwMDAwMDAwMLOGud2Hz7Nqhd6Y3rHMdZ4%22%2C%22token%22%3A%22MDAwMDAwMDAwMMurrpWavLehhs1-3LKpm9uD3Z3cepuomcWmmqaMiHtnr5ylzYWosKKZq6HQxtOK0ZCme5p-q6iZu2yrn4uNhJ3KedDYk7ivboS4it2yz4WThN2V3n6gYW0%22%7D


'''

import requests


login_url='https://www.ketangpai.com/UserApi/login'
login_data={'email':18668162176,'password':'Admin!989898','remember':1}

s=requests.session()

#header={'User-Agent':'Mozilla/5.0'}
#请求登录
#login_request=requests.post(login_url,login_data,verify=False)
s.post(login_url,login_data,verify=False)

#现在获取相应结果
#cookies=login_request.cookies
#print(cookies)

#获取考勤信息
kq_url='https://www.ketangpai.com/SummaryApi/attence?courseid=MDAwMDAwMDAwMLOGx5WIubts'

#kq_request=requests.get(kq_url,cookies=cookies,verify=False)
kq_request=s.get(kq_url,verify=False)

#获取考勤信息列表
print(kq_request.text)







