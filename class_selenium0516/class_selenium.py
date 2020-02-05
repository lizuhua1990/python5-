# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 20:53
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_selenium.py
# @Software: PyCharm

import time
from selenium import webdriver

driver = webdriver.Chrome()#实例 没有传参
driver.maximize_window()
#发起一个get请求， 打开一个页面
driver.get("http://www.baidu.com")
#等待，未来加载这个元素出来
time.sleep(2)
#driver.quit()


#完成搜索功能
#id class name  type  基础的
#xpath

#完成一个搜索功能

#1、输入搜索的内容
#driver.find_element_by_id()#id 肯定是唯一的 首选项
#driver.find_element_by_name()#除了id我们可以用name来定位  确保不会重复、没有冲突
#driver.find_element_by_class_name()#建议用这个么？你能确定她是唯一的，且有没有id


#页面操作  点击click  输入send_keys  清空 clear
driver.find_element_by_id('kw').send_keys('百度')
driver.find_element_by_id('su').click()
time.sleep(4)
driver.quit()

#启动浏览器===打开网页====定位元素（id  name  class_name ）html标签对最丑====进行对应的操作



