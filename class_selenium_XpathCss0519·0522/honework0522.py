# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 10:19
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : honework0522.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#元素定位和操作作业
#要求：三种方式 都用一下。第三种要重点掌握。
#1、完成前程贷的登陆操作。
#http://120.79.176.157:8012/Index/login.html
#帐号：13760246701/python_test

driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化

driver.get('http://120.79.176.157:8012/Index/login.html')#进入链接页面
#driver.implicitly_wait(30)#设置全局大范围智能等待最多30秒

login_1='//*[@class="form-group"]/*[@class="form-control username"]'#账号路径
login_2='//*[@class="form-group"]/*[@class="form-control"]'#密码路径
login_3='//*[@class="form-group mt-20"]/*[@class="btn btn-special"]'#登录按钮路径
#等待账号输入框元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_1)))
#输入手机号
driver.find_element_by_xpath(login_1).send_keys('13760246701')
time.sleep(1)
#输入密码
driver.find_element_by_xpath(login_2).send_keys('python_test')
#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_3)))
#点击登录
driver.find_element_by_xpath(login_3).click()


#2、前程贷系统  - 找到某个蜂群并点击进入。ps：元素定位、滚动、点击、使用等待方式。
login_4='//div[text()="小麦面粉"]'
time.sleep(2)#休眠2秒
target = driver.find_element_by_xpath(login_4)#找到这个元素。
driver.execute_script("arguments[0].scrollIntoView();", target) #利用js。拖动到可见的元素去
time.sleep(2)#休眠2秒
driver.find_element_by_xpath(login_4).click()#点击进入
#driver.quit()
#从iframe当中退出来
#driver.switch_to.default_content()


#3、腾讯课堂登陆 - 使用iframe和智能等待。
driver.get('https://ke.qq.com/')#进入链接页面
login_5='//a[@class="mod-header__link-login js-login-op"]'#登录元素路径
login_6='//div[@class="content-btns"]/a[@class="js-btns-enter btns-enter btns-enter-qq"]'
login_7='//a[@id="switcher_plogin"]'
#等待登录元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_5)))
driver.find_element_by_xpath(login_5).click()#点击登录
#等待登录类型元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_6)))
driver.find_element_by_xpath(login_6).click()#点击选择qq
time.sleep(1)

#进入iframe页面中
driver.switch_to.frame('login_frame_qq')
#等待输入元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_7)))
#使用元素等待直接可以跳转进入iframe找到元素
#WebDriverWait(driver,10,0.5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,login_7)))

driver.find_element_by_xpath(login_7).click()#点击选择账号密码登录
#输入账号
driver.find_element_by_id('u').send_keys('849080458')
driver.find_element_by_id('p').send_keys('zhang**8023')
driver.find_element_by_id('login_button').click()
