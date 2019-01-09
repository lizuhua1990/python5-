#Author:Xiao Jian
'''
腾讯课堂登陆 - QQ登陆 - 用户名和密码输入方式  - iframe的应用
'''

from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

#driver.implicitly_wait(30)
driver.get("https://ke.qq.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_id("js_login").click()
#qq登陆按钮 - 登陆方式选择
qq_login_button_xpath = '//div[@class="ptlogin-wrap"]//a[@data-type="1"]'
driver.find_element_by_xpath(qq_login_button_xpath).click()

#等待iframe出现,切换到iframe
iframe_name = "login_frame_qq"
WebDriverWait(driver,20,1).until(EC.frame_to_be_available_and_switch_to_it(iframe_name))
#点击用户名密码登陆按钮
time.sleep(2)
driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("u").send_keys("34567788")


