# coding:utf-8
# 手机号注册
from myyamltest.common.deired_caps import basedriver
from myyamltest.page import page
from myyamltest.data import dataes
from myyamltest.common.methods import publicmethods
import unittest,time

exist = 0
#业务流
class phoneregister(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_phoneregister(self):
        try:
            global exist
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
            publicmethods(self.driver).findelement(page.LoginPage.手机号注册['type'],page.LoginPage.手机号注册['value']).click()
            publicmethods(self.driver).wait(page.RegisterPhonePage.手机号输入框['type'],5,page.RegisterPhonePage.手机号输入框['value'])
            # 判断随机手机号是否已注册，已注册则重新清空输入，未注册则继续执行
            while exist == 0:
                try:
                    publicmethods(self.driver).findelement(page.RegisterPhonePage.手机号输入框['type'], page.RegisterPhonePage.手机号输入框['value'])\
                        .clear()
                    publicmethods(self.driver).findelement(page.RegisterPhonePage.手机号输入框['type'],page.RegisterPhonePage.手机号输入框['value'])\
                        .send_keys(publicmethods(self.driver).creatPhone())
                    publicmethods(self.driver).findelement(page.RegisterPhonePage.下一步['type'],page.RegisterPhonePage.下一步['value'])\
                        .click()
                    publicmethods(self.driver).wait(page.ToastPage.手机已注册['type'],5,page.ToastPage.手机已注册['value'])
                except:
                    exist = 1
            publicmethods(self.driver).wait(page.RegisterPhonePage.验证码['type'],5,page.RegisterPhonePage.验证码['value'])
            publicmethods(self.driver).findelement(page.RegisterPhonePage.验证码['type'],page.RegisterPhonePage.验证码['value'])\
                .send_keys(dataes.VerificationCode.验证码['value'])
            publicmethods(self.driver).findelement(page.RegisterPhonePage.登录密码['type'],page.RegisterPhonePage.登录密码['value'])\
                .send_keys(dataes.PhonePassword.手机通用登录密码['value'])
            publicmethods(self.driver).findelement(page.RegisterPhonePage.确认密码['type'],page.RegisterPhonePage.确认密码['value'])\
                .send_keys(dataes.PhonePassword.手机通用登录密码['value'])
            publicmethods(self.driver).findelement(page.RegisterPhonePage.注册['type'],page.RegisterPhonePage.注册['value']).click()
            try:
                # 查询能否找到完成按钮，能找到说明页面跳转，注册成功，案例通过，未找到时进入异常处理，案例失败
                publicmethods(self.driver).wait(page.RegisterPhonePage.完成['type'], 5,
                                                page.RegisterPhonePage.完成['value'])
                publicmethods(self.driver).getScreenShot('手机号注册', '成功')
                publicmethods(self.driver).findelement(page.RegisterPhonePage.完成['type'],
                                                       page.RegisterPhonePage.完成['value']).click()
                publicmethods(self.driver).wait(page.MinePage.资产总览['type'], 5, page.MinePage.资产总览['value'])
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
            publicmethods(self.driver).getScreenShot('手机号注册', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()