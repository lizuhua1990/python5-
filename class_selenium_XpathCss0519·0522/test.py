# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 22:07
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : test.py
# @Software: PyCharm



import time
from selenium import webdriver
#智能等待：
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#time.sleep(10)
#driver.find_element_by_id("kw").send_keys("北京")
#driver.find_element_by_id("su").click()
#login=r"//div[@id='u1']//a[@name='tj_login']"#//*[@id="u1"]/a[7]
#driver.find_element_by_xpath(login).click()
#time.sleep(3)
#er_img=r"//p[@title='用户名登录']"#//*[@id="TANGRAM__PSP_10__footerULoginBtn"]
#driver.find_element_by_xpath(er_img).click()

#browser.quit()

user_login_id='TANGRAM__PSP_10__footerULoginBtn'
#等待元素可见，user_login_id可见
#用户名密码登录方式
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')))

#百度登录定位
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
time.sleep(2)
#用户输入框等待
WebDriverWait(driver,10,0.5).until(EC.visibility_of_all_elements_located((By.ID,user_login_id)))

driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
time.sleep(1)
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys("zhanggh8023")
