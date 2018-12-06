# coding:utf-8
# 修改手势密码案例
from myyamltest.common.deired_caps import basedriver
from myyamltest.page import page
from myyamltest.data import dataes
from myyamltest.common.methods import publicmethods
from appium.webdriver.common.touch_action import TouchAction
import unittest,time
i = 0
#业务流
class changeshoushipsw(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_changeshoushipsw(self):
        try:
            global i
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
            # 获取验证码图片起始坐标
            beginpoint = publicmethods(self.driver).findelement(page.FundAccountLoginPage.验证码图片['type'],
                                                                page.FundAccountLoginPage.验证码图片['value']).location
            # 获取验证码图片宽高
            codesize = publicmethods(self.driver).findelement(page.FundAccountLoginPage.验证码图片['type'],
                                                              page.FundAccountLoginPage.验证码图片['value']).size
            while i <= 5:
                try:
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.资金账户['type'],
                                                           page.FundAccountLoginPage.资金账户['value']).clear()
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.资金账户['type'],
                                                           page.FundAccountLoginPage.资金账户['value']) \
                        .send_keys(dataes.FundAccountLogin.资金账号1['account'])
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.交易密码['type'],
                                                           page.FundAccountLoginPage.交易密码['value']) \
                        .send_keys(dataes.FundAccountLogin.资金账号1['psw'])
                    # 调用识别验证码
                    res = publicmethods(self.driver).identifyCode(beginpoint, codesize, 223)
                    # print(res)
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.图形验证码['type'],
                                                           page.FundAccountLoginPage.图形验证码['value']).send_keys(res)
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.登录['type'],
                                                           page.FundAccountLoginPage.登录['value']).click()
                    publicmethods(self.driver).wait(page.ToastPage.资金账号验证码错误['type'], 5,
                                                    page.ToastPage.资金账号验证码错误['value'])
                    i = i + 1
                except:
                    try:
                        # 当图片解析异常时，更换验证码图片
                        publicmethods(self.driver).wait(page.FundAccountLoginPage.资金账户['type'], 2,
                                                        page.FundAccountLoginPage.资金账户['value'])
                        publicmethods(self.driver).findelement(page.FundAccountLoginPage.验证码图片['type'],
                                                               page.FundAccountLoginPage.验证码图片['value']).click()
                        i = i + 1
                    except:
                        i = 6
            try:
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            except:
                pass
            publicmethods(self.driver).wait(page.MinePage.我的信息['type'], 5, page.MinePage.我的信息['value'])
            publicmethods(self.driver).findelement(page.MinePage.我的信息['type'], page.MinePage.我的信息['value']) \
                .click()
            publicmethods(self.driver).wait(page.MineInfoPage.密码管理['type'], 5, page.MineInfoPage.密码管理['value'])
            publicmethods(self.driver).findelement(page.MineInfoPage.密码管理['type'],
                                                   page.MineInfoPage.密码管理['value']).click()
            publicmethods(self.driver).wait(page.ChangeShoushiPsw.修改手势密码['type'], 5,
                                            page.ChangeShoushiPsw.修改手势密码['value'])
            publicmethods(self.driver).findelement(page.ChangeShoushiPsw.修改手势密码['type'],
                                                   page.ChangeShoushiPsw.修改手势密码['value']).click()
            publicmethods(self.driver).wait(page.ChangeShoushiPsw.请输入原手势密码['type'], 5,
                                            page.ChangeShoushiPsw.请输入原手势密码['value'])
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
            publicmethods(self.driver).wait(page.ChangeShoushiPsw.请设置手势密码['type'], 5,
                                            page.ChangeShoushiPsw.请设置手势密码['value'])
            TouchAction(self.driver).press(*gongge[1]).wait(300).move_to(*gongge[2]).wait(300) \
                .move_to(*gongge[3]).wait(300).move_to(*gongge[6]).wait(300) \
                .move_to(*gongge[9]).wait(300).release().perform()
            publicmethods(self.driver).wait(page.ChangeShoushiPsw.请再次绘制手势密码['type'], 5,
                                            page.ChangeShoushiPsw.请再次绘制手势密码['value'])
            TouchAction(self.driver).press(*gongge[1]).wait(300).move_to(*gongge[2]).wait(300) \
                .move_to(*gongge[3]).wait(300).move_to(*gongge[6]).wait(300) \
                .move_to(*gongge[9]).wait(300).release().perform()
            try:
                # 查询能否找到修改手势密码，能找到则修改成功，否则失败
                publicmethods(self.driver).wait(page.ChangeShoushiPsw.修改手势密码['type'],5,
                                                page.ChangeShoushiPsw.修改手势密码['value'])
                publicmethods(self.driver).getScreenShot('修改手势密码', '成功')
                time.sleep(1)
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
            publicmethods(self.driver).getScreenShot('修改手势密码', '失败')
            # 报错信息
            raise

    def tearDown(self):
        publicmethods(self.driver).quit()