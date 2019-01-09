# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 17:11
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : BasePage.py
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class BasePage:
    # 初始化
    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,by=By.XPATH,wait=15,frequnce=0.5):
        # 等待页面元素出现
        #确认你给我的定位表达式是 selenium可以用的
        if by not in By.__dict__.values():
            print('定位类型不支持，请更换成selenium支持的定位类型！')
        #开始等待的时间
        start_time=time
        #try:
        WebDriverWait(self.driver, wait, frequnce).until(EC.visibility_of_element_located((by,locator)))
        #except:
        #使用drdiver的截图功能
        #等待结束的时间
        over_time=time
        #等待时长=结束-开始
        #wait_time=over_time - start_time

    #查找元素
    def get_element(self,locator,by=By.XPATH,wait=15,frequnce=0.5):
        #等待元素可见
        self.wait_eleVisible(locator,by,wait,frequnce)
        #查找元素
        #开始查找时间
        startfind_time=time
        ele=self.driver.find_element(by=by,value=locator)
        #结束查找时间
        overfind_time=time
        #查找时间
        #find_time=overfind_time - startfind_time
        return ele

    #查找多个元素
    def get_elements(self,locator,by=By.XPATH,wait=15,frequnce=0.5):
        #等待元素可见
        self.wait_eleVisible(locator,by,wait,frequnce)
        #查找元素
        return self.driver.find_elements(by=by,value=locator)

    #滚动元素到可见区域
    def scroll_element_intoView(self,xpath):
        target = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #获取当前的url



