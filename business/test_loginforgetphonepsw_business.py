# coding:utf-8
# 登录页忘记手机号登录密码
from myyamltest.common.deired_caps import basedriver
from myyamltest.page import page
from myyamltest.data import dataes
from myyamltest.common.methods import publicmethods
import unittest,time

#业务流
class loginforgetphonepsw(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_loginforgetphonepsw(self):
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
            publicmethods(self.driver).wait(page.LoginForgetPhonePsw.忘记登录密码['type'],5,page.LoginForgetPhonePsw.忘记登录密码['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.忘记登录密码['type'],page.LoginForgetPhonePsw.忘记登录密码['value'])\
                .click()
            publicmethods(self.driver).wait(page.LoginForgetPhonePsw.手机号输入框['type'],5,page.LoginForgetPhonePsw.手机号输入框['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.手机号输入框['type'],page.LoginForgetPhonePsw.手机号输入框['value'])\
                .send_keys(dataes.PhoneAccount.有密码手机号['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.手机号页下一步['type'],page.LoginForgetPhonePsw.手机号页下一步['value'])\
                .click()
            publicmethods(self.driver).wait(page.LoginForgetPhonePsw.姓名['type'],5,page.LoginForgetPhonePsw.姓名['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.姓名['type'],page.LoginForgetPhonePsw.姓名['value'])\
                .send_keys(dataes.IdentityInfo.手机18721627126三要素信息['fullname'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.身份证号['type'],page.LoginForgetPhonePsw.身份证号['value'])\
                .send_keys(dataes.IdentityInfo.手机18721627126三要素信息['idno'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.实名认证页下一步['type'],page.LoginForgetPhonePsw.实名认证页下一步['value'])\
                .click()
            publicmethods(self.driver).wait(page.LoginForgetPhonePsw.重置登录密码页验证码['type'],10,page.LoginForgetPhonePsw.重置登录密码页验证码['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.重置登录密码页验证码['type'],page.LoginForgetPhonePsw.重置登录密码页验证码['value'])\
                .send_keys(dataes.VerificationCode.验证码['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.重置登录密码页登录密码['type'],page.LoginForgetPhonePsw.重置登录密码页登录密码['value'])\
                .send_keys(dataes.PhonePassword.手机通用登录密码['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.重置登录密码页确认密码['type'],page.LoginForgetPhonePsw.重置登录密码页确认密码['value'])\
                .send_keys(dataes.PhonePassword.手机通用登录密码['value'])
            publicmethods(self.driver).findelement(page.LoginForgetPhonePsw.重置登录密码页完成['type'],page.LoginForgetPhonePsw.重置登录密码页完成['value'])\
                .click()
            try:
                # 查询能否找到密码重置成功toast，能找到说明重置密码成功，案例通过，未找到时进入异常处理，给定False值传入Flag，案例失败
                publicmethods(self.driver).wait(page.ToastPage.密码重置成功['type'],5,page.ToastPage.密码重置成功['value'])
                publicmethods(self.driver).getScreenShot('登录页重置手机密码', '成功')
            except:
                print('未找到指定控件，案例失败')
                self.assertEqual(1, 2)
        except:
            publicmethods(self.driver).getScreenShot('登录页重置手机密码', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()