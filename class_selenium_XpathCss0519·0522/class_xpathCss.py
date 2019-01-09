# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 14:47
# @Author  : zgh
# @Email   : 849080458@qq.com
# @File    : class_xpathCss.py
# @Software: PyCharm


#selenium里面的webdriver会直接控制浏览器（通过不同浏览器的驱动）然后对目标进行测试UI层面的
#selenium自动化代码===》XXdriver.exe====>浏览器
#==========http通信================

#Chrome===>加载chrome-option===>启动chromedirver.exe===>与chromedriver.exe进行http链接===>发送http请求


from selenium import webdriver


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
#百度首页用ID定位
driver.find_element_by_id('kw').send_keys('小宝')
driver.find_element_by_id('su').click()

#百度首页-输入框，用name
driver.find_element_by_class_name('s_ipt')
#driver.find_element_by_XXXXx 查找多个元素

#driver .find_element_by_tag_name('input')
#driver.find_elements_by_tag_name('input')

#精确查询
driver.find_element_by_link_text('新闻')

#模糊查询
driver.find_element_by_partial_link_text('更多')

'''
#查询相对路径下的表达式：
# //input[@name='phone'and @placeholder='手机号'],表示一个input内的名字叫什么？找他就要@它
#通配符：//*[@name='phone'and @placeholder='手机号']

#绝对路径在上级目录变化的情况下会失去定位。

#网页对象操作：  
#   .click()  点击对象  
# .send_keys("xxx") 在对象上模拟按键输入  
# .clear() 用于清除输入框的内容，比如百度输入框里默认有个“请输入关键字”的信息，  
#            再比如我们的登陆框一般默认会有“账号”“密码”这样的默认信息。  
#            clear 可以帮助我们清除这些信息。  
#   .submit() 提交表单  
#   .text  获取该元素的文本  
#   ·get_attribute("属性名，如name")   获得属性值
text():元素的text内容
//*[@id='XXX'] 或者 //p[text()='XXXX']

#Xpath-定位和逻辑：
#contains(@属性/text(),value):包含函数
#文本定位：//span[contains(text()，‘正经生意’)]

逻辑运算：
and 表示条件与
or 表示条件或
例如://div[@class'XXX' and contains(@style,'display:visibility')]要可见的
一个页面的几个操作，都会有弹出框出现，定位到弹出框会有几个，但通过display的值定位到当前显示的那个。

Xpath-轴定位语法
轴运算：
ancestor：祖先节点，包括父
parent：父节点
preceding:当前节点元素标签的所有节点，（heml页面先后顺序）
preceding-sibling：当前元素节点标签之前的所有兄弟节点
following：当前元素节点标签之后的所有节点。（heml页面先后顺序）
following-sibling:当前元素节点标签之后的所有兄弟节点。

使用语法：
轴名称::节点名称(标签名）
例如：//div//table//td//preceding::td
//div[@id='XXX']//table//td//preceding::td

较多的应用场景：页面显示为一个表格样式的数据列，需要通过组合定位元素
例如：钱程贷投标：http://120.79.176.157:8012/index/login.html



###2018年5月22日 20:57:52
//*[text()=" 正经生意需要"]/ancestor::a/following-sibling::div//a
//*[text()="企业3"]/following-sibling::div[contains(@class,"special-color")]//span[@class="mr-10"]

1、可见才可以操作
滚动条操作，滚动到可见区域后，然后操作它
第一步：找到这个元素。
target = driver.find_element_by_id("id_keypair")
第二步：利用js。
driver.execute_script("arguments[0].scrollIntoView();", target)

滚动到顶部
js="varq=document.documentElement.scrollTop=0"
滚动到底部
js="varq=document.documentElement.scrollTop=10000"


智能等待：
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
