#Author:Xiao Jian
'''
百度高级搜索功能 - 高级搜索页面中，下拉框选择时间和文档类型选择 - 搜索操作.
'''

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

# options = webdriver.ChromeOptions()

# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])

# options.add_argument("--test-type")

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("http://www.baidu.com")

#查找‘设置’按钮并使鼠标悬浮于其上

set_But = driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_settingicon']")

ac = ActionChains(driver)

ac.move_to_element(set_But).perform()

#先获得窗口的handler个数并获取下拉菜单中的高级搜索按钮并点击

advanceSearch_But = driver.find_element_by_xpath("//div[@class='bdpfmenu']/a[text()='高级搜索']")

advanceSearch_But.click()

#获取时间,文档类型下拉框

select_time = Select(driver.find_element_by_xpath("//select[@name='gpc']"))

select_type = Select(driver.find_element_by_xpath("//select[@name='ft']"))

#选择第二个时间和第三种格式

select_time.select_by_index(1)

select_type.select_by_index(2)

#获取全部的关键词输入框并传入python关键字

driver.find_element_by_xpath("//input[@id='adv_keyword']").send_keys("python")

#获取搜索按钮并点击

driver.find_element_by_xpath("//input[@value='高级搜索']").click()