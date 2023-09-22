# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base1.base_page import BasePage


class HomePage(BasePage):

    #登录成功的定位
    login_success_loc=(By.XPATH, "//div[@class='el-dropdown']/div")



