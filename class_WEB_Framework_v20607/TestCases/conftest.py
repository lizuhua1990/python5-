# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 21:05
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : conftest.py
# @Software: PyCharm


import pytest
from selenium import webdriver
from class_WEB_Framework_v20607.PageObjects.login_Page import LoginPage
from class_WEB_Framework_v20607.TestDatas.Common_Data import *

@pytest.fixture
def init_driver():
    #相当于setup
    print('web自动化测试开始咯！')
    driver = webdriver.Chrome()
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.login(url,user_name,passwd)
    yield driver #可以返回多过，用列表返回：[driver,1]
    #相当于teardowm
    driver.close()
    driver.quit()
    print('web自动化测试结束了！')
    pass


@pytest.fixture
def hehehe():
    pass

''' 
用fixture装饰器调用fixture：
在测试用例/测试类前面加上@pytest.mark.usefixtures(“fixture函数名字”)
ps: 定义conftest.py文件，在此文件中可定义多个fixture.pytest会自动搜索此文件。'''

