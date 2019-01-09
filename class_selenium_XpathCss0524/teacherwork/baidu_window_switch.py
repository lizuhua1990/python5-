#Author:Xiao Jian
'''
百度首页 - 搜索selenium并打开新窗口 - 跳转到selenium网官网站,进入下载页面.
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

driver.implicitly_wait(10)

#在百度首页输入selenium进行搜索

driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

driver.find_element_by_xpath("//input[@id='su']").click()

#获取窗口handler，点击第四个链接，显示等待新窗口出现，并切换

old_window_handler = driver.window_handles

driver.find_element_by_xpath('//div[@class="result c-container "]//a[contains(text(),"Web Browser Automation")]').click()

WebDriverWait(driver,10,0.5).until(EC.new_window_is_opened(old_window_handler))

now_window_handler = driver.window_handles

print(now_window_handler)

driver.switch_to.window(now_window_handler[-1])

print(driver.current_window_handle)

#在新页面(selenium官方网站)中,点击download下载图标

WebDriverWait(driver,120,1).until(EC.visibility_of_element_located((By.XPATH,'//a[@title="Get Selenium"]')))
driver.find_element_by_xpath('//a[@title="Get Selenium"]').click()