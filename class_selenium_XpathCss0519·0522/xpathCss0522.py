# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 9:20
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : xpathCss0522.py
# @Software: PyCharm


#http://120.79.176.157:8012/Index/login.html
#帐号：13760246701/python_test
'''
绝对路径用/
//是相对路劲
其他的 就是找父节点 子节点 祖先节点 才会用::
#xpath定位总结：

nodename	选取此节点的所有子节点。
/	从根节点选取。绝对定位
//	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 相对定位
.	选取当前节点。
..	选取当前节点的父节点。
@	选取属性。
* 通配符。匹配所有元素节点
@* 通配符。匹配元素的所有属性
'''
'''
轴运算：
ancestor：祖先结点 包括父
parent:父结点
preceding: 当前元素节点标签之前的所有结点。（html页面先后顺序）
例：//div//table//td//preceding::td
preceding-sibling: 当前元素节点标签之前的所有兄弟结点
following: 当前元素节点标签之后的所有结点。（html页面先后顺序）
following-sibling：当前元素节点标签之后的所有兄弟结点
'''
'''
函数使用：
text():元素的text内容 例：//*[@id="XXX"]//p[text()="XXXX"]
contains(属性/text(),value):包含函数。例：contains(@class,"XXXX")、contains(text(),"XXXX")
'''
'''
逻辑运算：
and 表示条件与。
or 表示条件或。
例：//div[@class="XXX" and contains(@style,"display:visibility")]
'''
'''
#定位标名
//a[@class="btn btn-special"]#1、使用属性定位
//a[text()="抢投标"]#2、使用文本定位

#通过父标签下的兄弟节点进行定位
//*[text()=" 正经生意需要"]/ancestor::a/following-sibling::div//a

#定位企业3的375完元素
//*[text()="企业3"]/following-sibling::div[contains(@class,"special-color")]//span[@class="mr-10"]


1、可见才可以操作
滚动条操作，滚动到可见区域后，然后操作它
第一步：找到这个元素。
target = driver.find_element_by_id("id_keypair")
第二步：利用js。
driver.execute_script("arguments[0].scrollIntoView();", target)

iframe


'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()#打开浏览器
driver.maximize_window()#窗口最大化
driver.get('https://ke.qq.com/')#进入链接页面
#driver.implicitly_wait(30)#设置全局大范围智能等待最多30秒

driver.find_element_by_id('js_login').click()#点击qq登录
qq_login_button_xpath='//div[@class="ptlogin-wrap"]//a[@data-type="1"]'
driver.find_element_by_xpath(qq_login_button_xpath).click()

#等待iframe出现，切换到iframe
iframe_name='login_frame_qq'
WebDriverWait(driver,20,1).until(EC.frame_to_be_available_and_switch_to_it(iframe_name))

time.sleep(2)#休眠等待2秒
#点击用户名密码登录按钮
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('849080458')


#进入iframe页面中
#driver.switch_to.frame('login_frame_qq')
#driver.find_element_by_id('u')
#从iframe当中退出来
#driver.switch_to.default_content()

#百度登录定位
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
time.sleep(2)#死等2秒钟
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
time.sleep(1)
driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('zhanggh8023')




#显性等待
#明确等到某个条件满足后，去执行下一步
#WebDriverWait类：显性等待类
#WebDriverWait（driver,等待时间，轮循时间）.until()/until_not()

#智能等待：
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By













