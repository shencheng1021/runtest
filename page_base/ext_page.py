# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class ExtPage(BasePage):
    # 判断是否登录成功
    login_success_loc = (By.XPATH, "//div[@class='el-dropdown']/div")

    #定位立即申请按钮
    apply_now_button_loc=(By.XPATH,"//span[contains(text(),'立即申请')]")

    #定位数据授权协议
    license_agreement_loc=(By.XPATH,"//span[contains(text(),'数字保理数据授权协议')]")

    #登录成功进入E信通产品详情页
    def goto_ext_product_lg_s(self):
        self.presence_of_element_located(ExtPage.login_success_loc)
        self.goto_url('http://172.24.100.75:10006/#/market/detail/e-index')
        self.click(ExtPage.apply_now_button_loc)


    #未登录进入E信通产品详情页
    def goto_ext_product_lg_f(self):
        self.goto_url('http://172.24.100.75:10006/#/market/detail/e-index')
        self.click(ExtPage.apply_now_button_loc)

    #检查是是否弹出校验未登录的弹出窗
    def check_point_not_login(self):
        return self.alert_text()

    def check_point_license_agreement(self):
        return self.get_text(ExtPage.license_agreement_loc)