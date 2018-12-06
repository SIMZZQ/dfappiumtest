# coding:utf-8
# 现金宝充值案例
from myyamltest.dfappiumtest.common.deired_caps import basedriver
from myyamltest.dfappiumtest.page import page
from myyamltest.dfappiumtest.data import dataes
from myyamltest.dfappiumtest.common.methods import publicmethods
import unittest,time

#业务流
class cashtreasurepay(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_cashtreasurepay(self):
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
                (str(dataes.PhoneAccount.现金宝充值手机号['value']))
            publicmethods(self.driver).findelement(page.LoginPage.发送登录验证码['type'],page.LoginPage.发送登录验证码['value']).click()
            publicmethods(self.driver).findelement(page.LoginPage.登录验证码['type'],page.LoginPage.登录验证码['value']).send_keys\
                (str(dataes.VerificationCode.验证码['value']))
            publicmethods(self.driver).findelement(page.LoginPage.登录['type'],page.LoginPage.登录['value'],num=1).click()
            try:
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            except:
                pass
            publicmethods(self.driver).wait(page.MinePage.理财['type'],5,page.MinePage.理财['value'])
            publicmethods(self.driver).findelement(page.MinePage.理财['type'],page.MinePage.理财['value']).click()
            publicmethods(self.driver).hideWait(10)
            publicmethods(self.driver).wait(page.CashTreasurePay.现金宝['type'],5,page.CashTreasurePay.现金宝['value'])
            publicmethods(self.driver).findelement(page.CashTreasurePay.现金宝['type'],
                                                   page.CashTreasurePay.现金宝['value']).click()
            publicmethods(self.driver).wait(page.CashTreasurePay.收益页充值['type'],5,
                                            page.CashTreasurePay.收益页充值['value'])
            publicmethods(self.driver).findelement(page.CashTreasurePay.收益页充值['type'],
                                                   page.CashTreasurePay.收益页充值['value']).click()
            publicmethods(self.driver).wait(page.CashTreasurePay.金额['type'],5,page.CashTreasurePay.金额['value'])
            publicmethods(self.driver).findelement(page.CashTreasurePay.金额['type'],page.CashTreasurePay.金额['value'])\
                .send_keys(dataes.CashTreasure.金额['value'])
            publicmethods(self.driver).findelement(page.CashTreasurePay.充值页充值['type'],
                                                   page.CashTreasurePay.充值页充值['value']).click()
            try:
                publicmethods(self.driver).wait(page.CashTreasurePay.继续购买['type'],5,
                                                page.CashTreasurePay.继续购买['value'])
                publicmethods(self.driver).findelement(page.CashTreasurePay.继续购买['type'],
                                                       page.CashTreasurePay.继续购买['value']).click()
            except:
                pass
            publicmethods(self.driver).wait(page.CashTreasurePay.我知道了['type'],5,page.CashTreasurePay.我知道了['value'])
            publicmethods(self.driver).findelement(page.CashTreasurePay.我知道了['type'],page.CashTreasurePay.我知道了['value'])\
                .click()
            publicmethods(self.driver).wait(page.H5KeyBoard.按键1['type'],5,page.H5KeyBoard.按键1['value'])
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键1['type'],page.H5KeyBoard.按键1['value']).click()
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键4['type'],page.H5KeyBoard.按键4['value']).click()
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键7['type'],page.H5KeyBoard.按键7['value']).click()
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键2['type'],page.H5KeyBoard.按键2['value']).click()
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键5['type'],page.H5KeyBoard.按键5['value']).click()
            publicmethods(self.driver).findelement(page.H5KeyBoard.按键8['type'],page.H5KeyBoard.按键8['value']).click()
            try:
                publicmethods(self.driver).wait(page.CashTreasurePay.充值成功['type'],5,
                                                page.CashTreasurePay.充值成功['value'])
                time.sleep(2)
                publicmethods(self.driver).getScreenShot('现金宝充值','成功')
                publicmethods(self.driver).findelement(page.CashTreasurePay.返回['type'],
                                                       page.CashTreasurePay.返回['value']).click()
                time.sleep(1)
                # 返回至我的页面
                publicmethods(self.driver).backKey()
                publicmethods(self.driver).findelement(page.MinePage.我的['type'], page.MinePage.我的['value']).click()
                time.sleep(1)
                # 上滑页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.8, 0.2)
                publicmethods(self.driver).hideWait(5)
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value'])\
                    .click()
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).\
                    click()
            except:
                print('未找到指定控件，案例失败')
                self.assertEqual(1, 2)
        except:
            publicmethods(self.driver).getScreenShot('现金宝充值', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()