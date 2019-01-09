# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 20:24
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : selenium_alert.py
# @Software: PyCharm

#鼠标操作：https://blog.csdn.net/huilan_same/article/details/52305176


#等待的三种方式
#1、强制等待----sleep(秒)

#2、隐性等待----implicitly_wait(秒)

#3、智能等待----WebDriverWait（driver，10，0.5）
#1)、presence_of_element_located 元素存在
#2）、visibility_of_element_located 元素可见

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化

driver.get(os.getcwd()+'/test_alert.html')
#找到
driver.find_element_by_id('pres').click()
time.sleep(2)

#等待windows弹出框元素出现
WebDriverWait(driver,10,0.5).until(EC.alert_is_present())

#switch_to  进入到 windows弹出框当中
#Alert类提供了一系列的操作方法：1、dismiss（）：否  2、accept（）：是  3、text属性：获取弹出框里的内容
al=driver.switch_to.alert
#获取弹出框当中的内容
print(al.text)
#确认okay
al.accept()















