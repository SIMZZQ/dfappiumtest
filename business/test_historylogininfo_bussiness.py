# coding:utf-8
# 资金账号历史登录信息案例
from dfappiumtest.common.deired_caps import basedriver
from dfappiumtest.page import page
from dfappiumtest.data import dataes
from dfappiumtest.common.methods import publicmethods
import unittest,time
#业务流
class historylogininfo(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_historylogininfo(self):
        try:
            try:
                publicmethods(self.driver).wait(page.AlertPage.确定['type'], 15, page.AlertPage.确定['value'])
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                publicmethods(self.driver).tapPage(dataes.Coordinate.行情页坐标['valuex'], dataes.Coordinate.行情页坐标['valuey'])
            except:
                pass
            publicmethods(self.driver).findelement(page.MinePage.我的['type'], page.MinePage.我的['value']).click()
            time.sleep(1)
            publicmethods(self.driver).tapPage(dataes.Coordinate.我的页坐标['valuex'], dataes.Coordinate.我的页坐标['valuey'])
            publicmethods(self.driver).wait(page.MinePage.资产总览['type'], 5, page.MinePage.资产总览['value'])
            try:
                # 上滑页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.8, 0.2)
                publicmethods(self.driver).hideWait(5)
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value']) \
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
            time.sleep(1)
            publicmethods(self.driver).findelement(page.FundAccountLoginPage.资金账户['type'],
                                                   page.FundAccountLoginPage.资金账户['value']).clear()
            publicmethods(self.driver).findelement(page.FundAccountLoginPage.资金账户['type'],
                                                   page.FundAccountLoginPage.资金账户['value']) \
                .send_keys(dataes.FundAccountLogin.资金账号1['account'])
            publicmethods(self.driver).findelement(page.FundAccountLoginPage.交易密码['type'],
                                                   page.FundAccountLoginPage.交易密码['value']) \
                .send_keys(dataes.FundAccountLogin.资金账号1['psw'])
            # 获取验证码text
            res = publicmethods(self.driver).findelement(page.FundAccountLoginPage.验证码图片['type'],
                                                         page.FundAccountLoginPage.验证码图片['value']).text
            # 删除中间出现的空格
            res = res.replace(' ','')
            # print(res)
            publicmethods(self.driver).findelement(page.FundAccountLoginPage.图形验证码['type'],
                                                   page.FundAccountLoginPage.图形验证码['value']).send_keys(res)
            publicmethods(self.driver).findelement(page.FundAccountLoginPage.登录['type'],
                                                   page.FundAccountLoginPage.登录['value']).click()
            publicmethods(self.driver).wait(page.MinePage.我的信息['type'], 5, page.MinePage.我的信息['value'])
            publicmethods(self.driver).findelement(page.MinePage.我的信息['type'], page.MinePage.我的信息['value'])\
                .click()
            try:
                publicmethods(self.driver).wait(page.HistoryLoginInfo.登录记录['type'],5,
                                                page.HistoryLoginInfo.登录记录['value'])
                publicmethods(self.driver).findelement(page.HistoryLoginInfo.登录记录['type'],
                                                       page.HistoryLoginInfo.登录记录['value']).click()
                time.sleep(1)
                publicmethods(self.driver).getScreenShot('资金账号历史登录信息','成功')
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
                self.assertEqual(1,2)
        except:
            publicmethods(self.driver).getScreenShot('资金账号历史登录信息','失败')
            # 报错信息
            raise

    def tearDown(self):
        publicmethods(self.driver).quit()