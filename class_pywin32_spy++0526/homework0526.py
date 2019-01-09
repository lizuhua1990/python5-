# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 21:16
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : homework0526.py
# @Software: PyCharm


'''
web自动化作业
设计前程贷的投资用例 - 成功投资（不清楚的同学可以看视频回放）。
然后用自动化代码实现你设计的测试用例。。


web自动化--访问地址及帐号
http://120.79.176.157:8012/Index/login.html
帐号：13760246701/python_test
帐号2：18684720553/python
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


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


#2、前程贷系统  - 找到某个投标并点击进入。ps：元素定位、滚动、点击、使用等待方式。
#投标元素定位路径
login_4='//div[@class="b-title"]//span[text()=" python自动化项目"]'
#投标按钮元素定位路径
login_5='//span[text()=" python自动化项目"]/ancestor::a/following-sibling::div//a'

time.sleep(2)#休眠2秒
target = driver.find_element_by_xpath(login_4)#找到这个元素。
driver.execute_script("arguments[0].scrollIntoView();", target) #利用js。拖动到可见的元素去
time.sleep(2)#休眠2秒
driver.find_element_by_xpath(login_5).click()#点击进入

#投标元素定位
login_6='//div[@class="float_left"]//span[text()="python自动化项目"]'
#输入框元素定位路径
login_7='//input[@data-id="5765"]'
#投标按钮元素定位路径
login_8='//button[@class="btn btn-special height_style"]'

#等待登录按钮元素出现
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,login_6)))
target = driver.find_element_by_xpath(login_6)#找到这个元素。
driver.execute_script("arguments[0].scrollIntoView();", target) #利用js。拖动到可见的元素去
time.sleep(1)#休眠2秒

# #输入投标金额100
driver.find_element_by_xpath(login_7).send_keys('100')
time.sleep(1)#休眠2秒
#点击投标按钮投标
driver.find_element_by_xpath(login_8).click()



#退出浏览器
#driver.quit()








