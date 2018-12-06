# coding:utf-8
# 绑定资金账号案例
from myyamltest.dfappiumtest.common.deired_caps import basedriver
from myyamltest.dfappiumtest.page import page
from myyamltest.dfappiumtest.data import dataes
from myyamltest.dfappiumtest.common.methods import publicmethods
import unittest,time

#业务流
class bindaccount(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_bindaccount(self):
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
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value'])\
                    .click()
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                # 下拉页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.2, 0.8)
                publicmethods(self.driver).hideWait(5)
            except:
                # 下拉页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.2, 0.8)
                publicmethods(self.driver).hideWait(5)
            publicmethods(self.driver).findelement(page.MinePage.登录['type'], page.MinePage.登录['value']).click()
            publicmethods(self.driver).wait(page.LoginPage.登录xpath['type'],5,page.LoginPage.登录xpath['value'])
            publicmethods(self.driver).findelement(page.LoginPage.手机号切换按钮['type'],page.LoginPage.手机号切换按钮['value']).click()
            publicmethods(self.driver).wait(page.LoginPage.登录手机号['type'],5,page.LoginPage.登录手机号['value'])
            publicmethods(self.driver).findelement(page.LoginPage.登录手机号['type'],page.LoginPage.登录手机号['value']).clear()
            publicmethods(self.driver).findelement(page.LoginPage.登录手机号['type'],page.LoginPage.登录手机号['value']).send_keys\
                (str(dataes.PhoneAccount.绑定资金账号手机号['value']))
            publicmethods(self.driver).findelement(page.LoginPage.发送登录验证码['type'],page.LoginPage.发送登录验证码['value']).click()
            publicmethods(self.driver).findelement(page.LoginPage.登录验证码['type'],page.LoginPage.登录验证码['value']).send_keys\
                (str(dataes.VerificationCode.验证码['value']))
            publicmethods(self.driver).findelement(page.LoginPage.登录['type'],page.LoginPage.登录['value'],num=1).click()
            try:
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            except:
                pass
            publicmethods(self.driver).wait(page.MinePage.我的信息['type'],5,page.MinePage.我的信息['value'])
            publicmethods(self.driver).findelement(page.MinePage.我的信息['type'],page.MinePage.我的信息['value']).click()
            publicmethods(self.driver).wait(page.MineFundAccountPage.我的资金账户['type'],5,
                                            page.MineFundAccountPage.我的资金账户['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.我的资金账户['type'],
                                                   page.MineFundAccountPage.我的资金账户['value']).click()
            publicmethods(self.driver).wait(page.MineFundAccountPage.绑定资金账户['type'],5,
                                            page.MineFundAccountPage.绑定资金账户['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.绑定资金账户['type'],
                                                   page.MineFundAccountPage.绑定资金账户['value']).click()
            publicmethods(self.driver).wait(page.MineFundAccountPage.资金账户['type'],5,
                                            page.MineFundAccountPage.资金账户['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.资金账户['type'],
                                                   page.MineFundAccountPage.资金账户['value'])\
                .send_keys(dataes.BindAccountInfo.资金账号['account'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.交易密码['type'],
                                                   page.MineFundAccountPage.交易密码['value'])\
                .send_keys(dataes.BindAccountInfo.资金账号['psw'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.确定['type'],
                                                   page.MineFundAccountPage.确定['value']).click()
            try:
                # 判断能否找到绑定的资金账号列表，找到了则绑定成功，否则失败
                publicmethods(self.driver).wait(page.MineFundAccountPage.已绑定['type'],5,
                                                page.MineFundAccountPage.已绑定['value'])
                time.sleep(2)
                publicmethods(self.driver).getScreenShot('绑定资金账号', '成功')
                time.sleep(3)
                # 返回至我的页面
                publicmethods(self.driver).backKey()
                publicmethods(self.driver).backKey()
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
            publicmethods(self.driver).getScreenShot('绑定资金账号', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()
