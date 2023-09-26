# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
from base1.base_util import BaseUtil
from page_base.ext_page import ExtPage
from page_base.login_page import LoginPage


class TestExtdetails(BaseUtil):

    def test_extdetails_01(self):
        self.mylogger.info("****************E信通二级页面，校验企业是否实名认证，测试开始****************")

        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754856657','230516')
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        actual=EP.check_pointt_auth_status()
        self.assertEqual(actual,"查询完成,未完成实名认证")
        self.mylogger.info("****************E信通二级页面，校验企业是否实名认证，测试结束****************")

    def test_extdetails_02(self):
        self.mylogger.info("****************E信通二级页面，校验是否登录，测试开始****************")
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_f()
        actual=EP.check_point_not_login()
        self.assertEqual(actual,"系统检测到您尚未登录，或者登录已过期，请先登录以继续操作")
        self.mylogger.info("****************E信通二级页面，校验是否登录，测试结束****************")

    def test_extdetails_03(self):
        self.mylogger.info("****************E信通二级页面，校验授权协议弹出窗，测试开始****************")
        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754856658','230516')
        ep = ExtPage(self.driver)
        ep.goto_ext_product_lg_s()
        actual=ep.check_point_license_agreement()
        self.assertEqual(actual,"E信通业务合作协议")
        self.mylogger.info("****************E信通二级页面，校验授权协议弹出窗，测试结束****************")



