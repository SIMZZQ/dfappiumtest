# coding:utf-8
# 手机号+登录密码登录
from myyamltest.dfappiumtest.common.deired_caps import basedriver
from myyamltest.dfappiumtest.page import page
from myyamltest.dfappiumtest.data import dataes
from myyamltest.dfappiumtest.common.methods import publicmethods
import unittest,time

#业务流
class phonepswlogin(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_phonepswlogin(self):
        try:
            try:
                publicmethods(self.driver).wait(page.AlertPage.确定['type'], 15, page.AlertPage.确定['value'])
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                publicmethods(self.driver).tapPage(dataes.Coordinate.行情页坐标['valuex'], dataes.Coordinate.行情页坐标['valuey'])
            except:
                pass
            publicmethods(self.driver).findelement(page.MinePage.我的['type'],page.MinePage.我的['value']).click()
            time.sleep(1)
            publicmethods(self.driver).tapPage(dataes.Coordinate.我的页坐标['valuex'], dataes.Coordinate.我的页坐标['valuey'])
            publicmethods(self.driver).wait(page.MinePage.资产总览['type'], 5, page.MinePage.资产总览['value'])
            try:
                # 上滑页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.8, 0.2)
                publicmethods(self.driver).hideWait(5)
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value']).click()
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                # 下拉页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.2, 0.8)
                publicmethods(self.driver).hideWait(5)
            except:
                # 下拉页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.2, 0.8)
                publicmethods(self.driver).hideWait(5)
            publicmethods(self.driver).findelement(page.MinePage.登录['type'], page.MinePage.登录['value']).click()
            publicmethods(self.driver).wait(page.LoginPage.登录xpath['type'], 5, page.LoginPage.登录xpath['value'])
            publicmethods(self.driver).findelement(page.LoginPage.手机号切换按钮['type'],page.LoginPage.手机号切换按钮['value']).click()
            publicmethods(self.driver).findelement(page.LoginPage.使用登录密码登录['type'],page.LoginPage.使用登录密码登录['value']).click()
            publicmethods(self.driver).wait(page.PhonePswLoginPage.登录手机号['type'],15,page.PhonePswLoginPage.登录手机号['value'])
            publicmethods(self.driver).findelement(page.PhonePswLoginPage.登录手机号['type'], page.PhonePswLoginPage.登录手机号['value']).\
                clear()
            publicmethods(self.driver).findelement(page.PhonePswLoginPage.登录手机号['type'],page.PhonePswLoginPage.登录手机号['value']).\
                send_keys(dataes.PhoneAccount.有密码手机号['value'])
            publicmethods(self.driver).findelement(page.PhonePswLoginPage.登录密码['type'],page.PhonePswLoginPage.登录密码['value']).\
                send_keys(dataes.PhonePassword.手机通用登录密码['value'])
            publicmethods(self.driver).findelement(page.PhonePswLoginPage.登录['type'],page.PhonePswLoginPage.登录['value'],num=1).click()
            try:
                try:
                    publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                except:
                    pass
                # 查询能否找到资产总览按钮，能找到说明页面跳转，登录成功，案例通过，未找到时进入异常处理，给定False值传入Flag，案例失败
                publicmethods(self.driver).wait(page.MinePage.资产总览['type'],5,page.MinePage.资产总览['value'])
                publicmethods(self.driver).getScreenShot('手机号登录密码登录', '成功')
                time.sleep(1)
                # 上滑页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.8, 0.2)
                publicmethods(self.driver).hideWait(5)
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value']).click()
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            except:
                print('未找到指定控件，案例失败')
                self.assertEqual(1, 2)
        except:
            publicmethods(self.driver).getScreenShot('手机号登录密码登录', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()