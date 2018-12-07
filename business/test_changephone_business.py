# coding:utf-8
# 更换手机号案例
from dfappiumtest.common.deired_caps import basedriver
from dfappiumtest.page import page
from dfappiumtest.data import dataes
from dfappiumtest.common.methods import publicmethods
import unittest,time

i = 0
exist = 0
#业务流
class changephone(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()

    def test_changephone(self):
        try:
            global i,exist
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
                                                           page.FundAccountLoginPage.资金账户['value'])\
                        .send_keys(dataes.ChangePhone.资金账号['account'])
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.交易密码['type'],
                                                           page.FundAccountLoginPage.交易密码['value'])\
                        .send_keys(dataes.ChangePhone.资金账号['psw'])
                    # 调用识别验证码
                    res = publicmethods(self.driver).identifyCode(beginpoint,codesize,223)
                    # print(res)
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.图形验证码['type'],
                                                       page.FundAccountLoginPage.图形验证码['value']).send_keys(res)
                    publicmethods(self.driver).findelement(page.FundAccountLoginPage.登录['type'],
                                                           page.FundAccountLoginPage.登录['value']).click()
                    publicmethods(self.driver).wait(page.ToastPage.资金账号验证码错误['type'],5,
                                                    page.ToastPage.资金账号验证码错误['value'])
                    i = i+1
                except:
                    try:
                        # 当图片解析异常时，更换验证码图片
                        publicmethods(self.driver).wait(page.FundAccountLoginPage.资金账户['type'],2,
                                                        page.FundAccountLoginPage.资金账户['value'])
                        publicmethods(self.driver).findelement(page.FundAccountLoginPage.验证码图片['type'],
                                                               page.FundAccountLoginPage.验证码图片['value']).click()
                        i = i+1
                    except:
                        i = 6
            try:
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            except:
                pass
            publicmethods(self.driver).wait(page.MinePage.我的信息['type'],5,page.MinePage.我的信息['value'])
            publicmethods(self.driver).findelement(page.MinePage.我的信息['type'],page.MinePage.我的信息['value'])\
                .click()
            publicmethods(self.driver).wait(page.BindPhone.手机号['type'],5,page.BindPhone.手机号['value'])
            publicmethods(self.driver).findelement(page.BindPhone.手机号['type'],page.BindPhone.手机号['value']).click()
            publicmethods(self.driver).wait(page.ChangePhone.更换手机号['type'],5,page.ChangePhone.更换手机号['value'])
            publicmethods(self.driver).findelement(page.ChangePhone.更换手机号['type'],
                                                   page.ChangePhone.更换手机号['value']).click()
            publicmethods(self.driver).wait(page.ChangePhone.旧手机验证码['type'],5,
                                            page.ChangePhone.旧手机验证码['value'])
            publicmethods(self.driver).findelement(page.ChangePhone.旧手机验证码['type'],
                                                   page.ChangePhone.旧手机验证码['value'])\
                .send_keys(dataes.VerificationCode.验证码['value'])
            publicmethods(self.driver).findelement(page.ChangePhone.旧手机下一步['type'],
                                                   page.ChangePhone.旧手机下一步['value']).click()
            publicmethods(self.driver).wait(page.ChangePhone.新手机号['type'],5,page.ChangePhone.新手机号['value'])
            # 判断随机生成的手机号是否已被绑定，被占用则重新生成，否则继续执行
            while exist == 0:
                try:
                    publicmethods(self.driver).findelement(page.ChangePhone.新手机号['type'],
                                                           page.ChangePhone.新手机号['value'])\
                        .send_keys(publicmethods(self.driver).creatPhone())
                    publicmethods(self.driver).findelement(page.ChangePhone.发送验证码['type'],
                                                           page.ChangePhone.发送验证码['value']).click()
                    publicmethods(self.driver).wait(page.ToastPage.更换手机号已绑定['type'],5,
                                                    page.ToastPage.更换手机号已绑定['value'])
                except:
                    exist = 1
            publicmethods(self.driver).findelement(page.ChangePhone.验证码['type'],page.ChangePhone.验证码['value'])\
                .send_keys(dataes.VerificationCode.验证码['value'])
            publicmethods(self.driver).findelement(page.ChangePhone.新手机号确定['type'],
                                                   page.ChangePhone.新手机号确定['value']).click()
            try:
                # 判断能否找到手机号更换成功，找到了则更换成功，否则失败
                publicmethods(self.driver).wait(page.ToastPage.手机号更换成功['type'],10,
                                                page.ToastPage.手机号更换成功['value'])
                publicmethods(self.driver).getScreenShot('更换手机号', '成功')
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
            publicmethods(self.driver).getScreenShot('更换手机号', '失败')
            # 报错信息
            raise
    def tearDown(self):
        publicmethods(self.driver).quit()