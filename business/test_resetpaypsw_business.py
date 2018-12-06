# coding:utf-8
# 重置支付密码案例
from myyamltest.common.deired_caps import basedriver
from myyamltest.page import page
from myyamltest.data import dataes
from myyamltest.common.methods import publicmethods
from appium.webdriver.common.touch_action import TouchAction
import unittest,time,os

#业务流
class resetpaypsw(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_resetpaypsw(self):
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
                (str(dataes.PhoneAccount.重置支付密码手机号['value']))
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
            loc = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'],page.JiuGongGe.九宫格['value']).location
            # 获取九宫格宽高
            jiu_s = publicmethods(self.driver).findelement(page.JiuGongGe.九宫格['type'],page.JiuGongGe.九宫格['value']).size
            # 将获取的九宫格九个点的坐标列表传给gongge
            gongge = publicmethods(self.driver).jiu(loc,jiu_s)
            # print(gongge)
            # print(gongge[1][1])
            # print(type(publicmethods(self.driver).pianyi(1,2,gongge)[0]))
            # 执行解锁（滑动操作） gongge[x]为元组，使用*gongge[x]将元组中的元素提取出来作为参数传入
            # move_to中坐标为绝对坐标，至于到底使用相对偏移量还是绝对坐标，需要查看方法源码
            TouchAction(self.driver).press(*gongge[1]).wait(300).move_to(*gongge[2]).wait(300)\
                .move_to(*gongge[3]).wait(300).move_to(*gongge[6]).wait(300)\
                .move_to(*gongge[9]).wait(300).release().perform()
            publicmethods(self.driver).wait(page.MineInfoPage.密码管理['type'],15,page.MineInfoPage.密码管理['value'])
            publicmethods(self.driver).findelement(page.MineInfoPage.密码管理['type'],page.MineInfoPage.密码管理['value'])\
                .click()
            publicmethods(self.driver).wait(page.MineInfoPage.忘记理财支付密码['type'],15,page.MineInfoPage.忘记理财支付密码['value'])
            publicmethods(self.driver).findelement(page.MineInfoPage.忘记理财支付密码['type']
                                                   ,page.MineInfoPage.忘记理财支付密码['value']).click()
            publicmethods(self.driver).wait(page.ForgetPayPswPage.忘记理财支付密码主页['type'],5
                                            ,page.ForgetPayPswPage.忘记理财支付密码主页['value'])
            # 切换webview之前获取页面宽高
            x = self.driver.get_window_size()['width']  # 获取屏幕宽度
            y = self.driver.get_window_size()['height']  # 获取屏幕高度
            contexts = self.driver.contexts
            # print(contexts)
            # chromedriver与手机webview中的chrome版本必须一致，否则switch_to会报错
            # 切换到webview
            self.driver.switch_to.context(contexts[1])
            # print(self.driver.current_context)
            publicmethods(self.driver).wait(page.ForgetPayPswPage.持卡人['type'],15,page.ForgetPayPswPage.持卡人['value'])
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.持卡人['type'],page.ForgetPayPswPage.持卡人['value'])\
                .send_keys(dataes.ForgetPayPswInfo.持卡人['fullname'])
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.身份证['type'],page.ForgetPayPswPage.身份证['value'])\
                .send_keys(str(dataes.ForgetPayPswInfo.身份证['idno']))
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.卡号['type'],page.ForgetPayPswPage.卡号['value'])\
                .send_keys(str(dataes.ForgetPayPswInfo.卡号['cardno']))
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.手机号['type'],page.ForgetPayPswPage.手机号['value'])\
                .send_keys(str(dataes.ForgetPayPswInfo.手机号['phone']))
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.获取验证码['type'],
                                                   page.ForgetPayPswPage.获取验证码['value']).click()
            time.sleep(2)
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.验证码['type'],page.ForgetPayPswPage.验证码['value'])\
                .send_keys(str(dataes.ForgetPayPswInfo.验证码['code']))
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.确定['type'],
                                                   page.ForgetPayPswPage.确定['value']).click()
            publicmethods(self.driver).wait(page.ForgetPayPswPage.支付密码['type'],5,page.ForgetPayPswPage.支付密码['value'])
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.支付密码['type'],
                                                   page.ForgetPayPswPage.支付密码['value']).click()
            # time.sleep(1)
            publicmethods(self.driver).wait(page.ForgetPayPswPage.安全软键盘页['type'],5,
                                            page.ForgetPayPswPage.安全软键盘页['value'])
            # 自定义软键盘太恶心了，我还是服气了。暴力解决吧。。。
            # adb = 'adb shell input tap 179 1355'
            # os.system(adb)
            # 将获取的软键盘按键坐标点的坐标字典传给numbutton
            numbutton = publicmethods(self.driver).H5keyboard(x,y)
            # 点击按键1
            btn1 = 'adb shell input tap %s %s' %(numbutton[1][0],numbutton[1][1])
            os.system(btn1)
            # 点击按键4
            btn4 = 'adb shell input tap %s %s' % (numbutton[4][0], numbutton[4][1])
            os.system(btn4)
            # 点击按键7
            btn7 = 'adb shell input tap %s %s' % (numbutton[7][0], numbutton[7][1])
            os.system(btn7)
            # 点击按键2
            btn2 = 'adb shell input tap %s %s' % (numbutton[2][0], numbutton[2][1])
            os.system(btn2)
            # 点击按键5
            btn5 = 'adb shell input tap %s %s' % (numbutton[5][0], numbutton[5][1])
            os.system(btn5)
            # 点击按键8
            btn8 = 'adb shell input tap %s %s' % (numbutton[8][0], numbutton[8][1])
            os.system(btn8)
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.确认密码['type'],
                                                   page.ForgetPayPswPage.确认密码['value']).click()
            publicmethods(self.driver).wait(page.ForgetPayPswPage.安全软键盘页['type'], 5,
                                            page.ForgetPayPswPage.安全软键盘页['value'])
            # 点击按键1
            btn1 = 'adb shell input tap %s %s' % (numbutton[1][0], numbutton[1][1])
            os.system(btn1)
            # 点击按键4
            btn4 = 'adb shell input tap %s %s' % (numbutton[4][0], numbutton[4][1])
            os.system(btn4)
            # 点击按键7
            btn7 = 'adb shell input tap %s %s' % (numbutton[7][0], numbutton[7][1])
            os.system(btn7)
            # 点击按键2
            btn2 = 'adb shell input tap %s %s' % (numbutton[2][0], numbutton[2][1])
            os.system(btn2)
            # 点击按键5
            btn5 = 'adb shell input tap %s %s' % (numbutton[5][0], numbutton[5][1])
            os.system(btn5)
            # 点击按键8
            btn8 = 'adb shell input tap %s %s' % (numbutton[8][0], numbutton[8][1])
            os.system(btn8)
            publicmethods(self.driver).findelement(page.ForgetPayPswPage.下一步['type'],
                                                   page.ForgetPayPswPage.下一步['value']).click()
            # 切换回native再找toast元素
            self.driver.switch_to.context(contexts[0])
            try:
                publicmethods(self.driver).wait(page.ToastPage.密码重置成功['type'], 5,
                                                page.ToastPage.密码重置成功['value'])
                publicmethods(self.driver).getScreenShot('忘记支付密码', '成功')
                time.sleep(2)
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
            # 当在H5页面报错时，要切回appium驱动进行操作
            self.driver.switch_to.context(contexts[0])
            publicmethods(self.driver).getScreenShot('忘记支付密码', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()