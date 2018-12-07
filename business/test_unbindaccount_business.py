# coding:utf-8
# 解绑资金账号案例
from dfappiumtest.common.deired_caps import basedriver
from dfappiumtest.page import page
from dfappiumtest.data import dataes
from dfappiumtest.common.methods import publicmethods
from appium.webdriver.common.touch_action import TouchAction
import unittest,time

#业务流
class unbindaccount(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_unbindaccount(self):
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
                (str(dataes.PhoneAccount.资金号加手机号['value']))
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
            publicmethods(self.driver).hideWait(5)
            # 获取九宫格起始位置坐标
            loc = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'], page.JiuGongGe.九宫格['value']).location
            # 获取九宫格宽高
            jiu_s = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'], page.JiuGongGe.九宫格['value']).size
            # 将获取的九宫格九个点的坐标列表传给gongge
            gongge = publicmethods(self.driver).jiu(loc, jiu_s)
            # 执行解锁（滑动操作） gongge[x]为元组，使用*gongge[x]将元组中的元素提取出来作为参数传入
            # move_to中坐标为绝对坐标，至于到底使用相对偏移量还是绝对坐标，需要查看方法源码
            TouchAction(self.driver).press(*gongge[1]).wait(300).move_to(*gongge[2]).wait(300)\
                .move_to(*gongge[3]).wait(300).move_to(*gongge[6]).wait(300)\
                .move_to(*gongge[9]).wait(300).release().perform()
            publicmethods(self.driver).wait(page.MineFundAccountPage.我的资金账户['type'],5,
                                            page.MineFundAccountPage.我的资金账户['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.我的资金账户['type'],
                                                   page.MineFundAccountPage.我的资金账户['value']).click()
            publicmethods(self.driver).wait(page.MineFundAccountPage.资金账号列表1['type'],5,
                                            page.MineFundAccountPage.资金账号列表1['value'])
            # 获取需要解绑资金账号列表框的起始点
            loc = publicmethods(self.driver).findelement(page.MineFundAccountPage.资金账号列表1['type'],
                                                         page.MineFundAccountPage.资金账号列表1['value']).location
            # 获取需要解绑资金账号列表框的宽高
            size = publicmethods(self.driver).findelement(page.MineFundAccountPage.资金账号列表1['type'],
                                                          page.MineFundAccountPage.资金账号列表1['value']).size
            publicmethods(self.driver).swipeLeftRight(loc,size,0.8,0.2)
            publicmethods(self.driver).wait(page.MineFundAccountPage.删除['type'],5,
                                            page.MineFundAccountPage.删除['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.删除['type'],
                                                   page.MineFundAccountPage.删除['value']).click()
            publicmethods(self.driver).wait(page.MineFundAccountPage.输入交易密码['type'],5,
                                            page.MineFundAccountPage.输入交易密码['value'])
            publicmethods(self.driver).findelement(page.MineFundAccountPage.输入交易密码['type'],
                                                   page.MineFundAccountPage.输入交易密码['value'])\
                .send_keys(str(dataes.FundAccountPsw.资金账号通用密码['psw']))
            publicmethods(self.driver).findelement(page.MineFundAccountPage.解绑交易密码确定['type'],
                                                   page.MineFundAccountPage.解绑交易密码确定['value']).click()
            try:
                # 判断能否找到我要绑定，找到了则解绑成功，否则失败
                publicmethods(self.driver).wait(page.MineFundAccountPage.我要绑定['type'],10,
                                                page.MineFundAccountPage.我要绑定['value'])
                publicmethods(self.driver).getScreenShot('解绑资金账号', '成功')
                time.sleep(1)
                publicmethods(self.driver).findelement(page.MineFundAccountPage.我要绑定['type'],
                                                       page.MineFundAccountPage.我要绑定['value']).click()
                publicmethods(self.driver).wait(page.MineFundAccountPage.输入交易密码['type'], 5,
                                                page.MineFundAccountPage.输入交易密码['value'])
                publicmethods(self.driver).findelement(page.MineFundAccountPage.输入交易密码['type'],
                                                       page.MineFundAccountPage.输入交易密码['value']) \
                    .send_keys(str(dataes.FundAccountPsw.资金账号通用密码['psw']))
                publicmethods(self.driver).findelement(page.MineFundAccountPage.验证交易密码确定['type'],
                                                       page.MineFundAccountPage.验证交易密码确定['value']).click()
                time.sleep(10)
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
            publicmethods(self.driver).getScreenShot('解绑资金账号', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()