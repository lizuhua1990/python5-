# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 16:25
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : switch_windows.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化,要保持良好习惯全屏打开
#打开百度首页
driver.get('http://www.baidu.com')
#页面操作  点击click  输入send_keys  清空 clear
driver.find_element_by_id('kw').send_keys('actionchains')
driver.find_element_by_id('su').click()
time.sleep(2)

#链接第一个的元素路径
mypath='//*[@class="result c-container "]//a'

#窗口切换
#1、获取当前所有的窗口
windows=driver.window_handles
#等待元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,mypath)))
#点击进入链接页面
driver.find_element_by_xpath(mypath).click()
time.sleep(2)
#等待窗口出现
WebDriverWait(driver,10,0.5).until(EC.new_window_is_opened(windows))

windows=driver.window_handles
#2、切换好指定的窗口
driver.switch_to.window(windows[-1])#最新打开的窗口
time.sleep(3)
#博客园元素路径
bky_id="blog_nav_sitehome"
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.ID,bky_id)))
#点击进入博客园
driver.find_element_by_id(bky_id).click()
time.sleep(3)

#3、切回原来的窗口
driver.switch_to.window(windows[0])#切换到第一个窗口
time.sleep(3)

#4、获取当前窗口的句柄
print(driver.current_window_handle)

#浏览器退出
driver.quit()


















