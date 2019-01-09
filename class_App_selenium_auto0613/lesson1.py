# -*- coding: utf-8 -*-
# @Time    : 2018/6/30 14:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : lesson1.py
# @Software: PyCharm

from appium import webdriver
import time

#帐号：13760246701/python_test

desired_caps={}

desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1"
desired_caps["deviceName"]="Android Emulator"

desired_caps["appPackage"]="com.xxzb.fenwoo"
#进入app之后的第一个activity（除了引导页面之外）
#desired_caps["appActivity"]=".activity.MainActivity"
desired_caps["appActivity"]=".activity.addition.WelcomeActivity"
#desired_caps["appWaitDuration"]=10000


#连接appium server ，并告诉appium要操作的对象是谁
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


time.sleep(10)
#通过resouce-id来定位--但它并不是绝对唯一的
#driver.find_element_by_id("com.xxzb.fenwoo:id/tv_loanterm")
#driver.find_element_by_accessibility_id()"content-desc"

#重要提醒：在java中是new实例化对象，在className中要用"",里面是字符串
#driver.find_element_by_android_uiautomator('new UiSelector().className(\"android.widget.TextView\").textContains(\"2月\").resourceId(\"com.xxzb.fenwoo:id/tv_loanterm\")')

#定位首页 的标的借款金额数字
#ele=driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xxzb.fenwoo:id/tv_amount")')
#print(ele.text)


#获取当前屏幕大小
phone_size=driver.get_window_size()
print(phone_size)
for index in range(0,3):
    driver.swipe(phone_size["width"]*0.9,phone_size["height"]*0.5,phone_size["width"]*0.1,phone_size["height"]*0.5)
    time.sleep(1)

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


#等待
start_id='com.xxzb.fenwoo:id/btn_start'
WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((MobileBy.ID,start_id)))

#点击立即体验
ele=driver.find_element_by_id(start_id)
ele.click()
ele.location
ele.size







