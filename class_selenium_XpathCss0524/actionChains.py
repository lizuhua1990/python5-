# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 13:45
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : actionChains.py
# @Software: PyCharmz

#鼠标操作
#有seleniu的ActionChains类来完成农牛鼠标操作
#主流操作流程
#1、存储鼠标操作     2、perform（）来执行鼠标操作
'''
#支持的操作如下：
1、double_click 双击操作
2、context_click 右键操作
3、dra_and_drop 拖拽操作。左键按住拖动某一元素到另外一个区域，然后释放按键
4、move_to_element()  鼠标悬停操作
'''

#引入类ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
#AC.方法名1（）.context_click().perform()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化,要保持良好习惯全屏打开
#打开百度首页
driver.get('http://www.baidu.com')
#设置元素---表达式
setting_xpath='//div[@id="u1"]//a[@name="tj_settingicon"]'
#等待1秒
time.sleep(1)
#设置元素的webelment对象
set_ele=driver.find_element_by_xpath(setting_xpath)
#获取元素的文本内容
print(set_ele.text)
#获取元素的某一个属性值
print(set_ele.get_attribute('name'))

#鼠标悬停操作  先实例化ActionCains类，在调用其方法，最后使用perform（）来执行鼠标操作
ActionChains(driver).move_to_element(set_ele).perform()
#高级搜索的定位路径
mypath='//div[@class="bdpfmenu"]//a[text()="高级搜索"]'
#等待元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,mypath)))
#点击高级搜索进入
driver.find_element_by_xpath(mypath).click()












