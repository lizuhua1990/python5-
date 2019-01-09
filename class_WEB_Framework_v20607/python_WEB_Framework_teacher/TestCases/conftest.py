#Author:Xiao Jian
import pytest
from PageObjects.login_page import LoginPage
from TestDatas.CommonData import *
from selenium import webdriver

@pytest.fixture
def init_env():
    driver = webdriver.Chrome()
    LoginPage(driver).login(web_url, common_user, common_passwd)
    yield driver
    driver.quit()

@pytest.fixture
def login():
    pass

