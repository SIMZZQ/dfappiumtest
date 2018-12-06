# coding:utf-8
# 资金账号历史登录信息退出二级案例
from myyamltest.dfappiumtest.common.deired_caps import basedriver
from myyamltest.dfappiumtest.page import page
from myyamltest.dfappiumtest.data import dataes
from myyamltest.dfappiumtest.common.methods import publicmethods
from appium.webdriver.common.touch_action import TouchAction
import unittest,time
#业务流
class historylogininfoexitsec(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_historylogininfoexitsec(self):
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
            publicmethods(self.driver).wait(page.MinePage.交易['type'], 5, page.MinePage.交易['value'])
            publicmethods(self.driver).findelement(page.MinePage.交易['type'], page.MinePage.交易['value']).click()
            publicmethods(self.driver).wait(page.TraderPage.退出交易['type'],5,page.TraderPage.退出交易['value'])
            publicmethods(self.driver).findelement(page.TraderPage.退出交易['type'],page.TraderPage.退出交易['value'])\
                .click()
            publicmethods(self.driver).wait(page.AlertPage.确定['type'],5,page.AlertPage.确定['value'])
            publicmethods(self.driver).findelement(page.AlertPage.确定['type'],page.AlertPage.确定['value']).click()
            publicmethods(self.driver).findelement(page.MinePage.我的['type'],page.MinePage.我的['value']).click()
            publicmethods(self.driver).wait(page.MinePage.我的信息['type'], 5, page.MinePage.我的信息['value'])
            publicmethods(self.driver).findelement(page.MinePage.我的信息['type'], page.MinePage.我的信息['value'])\
                .click()
            publicmethods(self.driver).hideWait(5)
            # 获取九宫格起始位置坐标
            loc = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'],
                                                         page.JiuGongGe.九宫格['value']).location
            # 获取九宫格宽高
            jiu_s = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'], page.JiuGongGe.九宫格['value']).size
            # 将获取的九宫格九个点的坐标列表传给gongge
            gongge = publicmethods(self.driver).jiu(loc, jiu_s)
            # 执行解锁（滑动操作） gongge[x]为元组，使用*gongge[x]将元组中的元素提取出来作为参数传入
            # move_to中坐标为绝对坐标，至于到底使用相对偏移量还是绝对坐标，需要查看方法源码
            TouchAction(self.driver).press(*gongge[1]).wait(300).move_to(*gongge[2]).wait(300) \
                .move_to(*gongge[3]).wait(300).move_to(*gongge[6]).wait(300) \
                .move_to(*gongge[9]).wait(300).release().perform()
            try:
                publicmethods(self.driver).wait(page.HistoryLoginInfo.登录记录['type'], 5,
                                                page.HistoryLoginInfo.登录记录['value'])
                print('找到不应出现控件，案例失败')
                self.assertEqual(1, 2)
            except:
                publicmethods(self.driver).getScreenShot('资金账号历史登录信息退出二级', '成功')
                publicmethods(self.driver).backKey()
                time.sleep(1)
                # 上滑页面
                publicmethods(self.driver).swipeUpDown(0.5, 0.8, 0.2)
                publicmethods(self.driver).hideWait(5)
                publicmethods(self.driver).findelement(page.MinePage.退出登录['type'], page.MinePage.退出登录['value']).click()
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
        except:
            publicmethods(self.driver).getScreenShot('资金账号历史登录信息退出二级','失败')
            # 报错信息
            raise

    def tearDown(self):
        publicmethods(self.driver).quit()