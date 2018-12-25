# coding:utf-8
# 激活手机号案例
from dfappiumtest.common.deired_caps import basedriver
from dfappiumtest.page import page
from dfappiumtest.data import dataes
from dfappiumtest.common.methods import publicmethods
import unittest,time

#业务流
class activephone(unittest.TestCase):
    def setUp(self):
        self.driver = basedriver()
        # 等待指定页面加载完成后执行后续操作
        # publicmethods(self.driver).waitActivity('.major.activity.HomeActivity', 30)

    def test_activephone(self):
        try:
            # 当出现法律弹框时操作弹框内容
            try:
                # self.assertIsNotNone(publicmethods(self.driver).findelement(page.AlertPage.确定['type'],page.AlertPage.确定['value']))
                publicmethods(self.driver).wait(page.AlertPage.确定['type'],15,page.AlertPage.确定['value'])
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                publicmethods(self.driver).tapPage(dataes.Coordinate.行情页坐标['valuex'], dataes.Coordinate.行情页坐标['valuey'])
            except:
                pass
            publicmethods(self.driver).findelement(page.MinePage.我的['type'],page.MinePage.我的['value']).click()
            time.sleep(1)
            publicmethods(self.driver).tapPage(dataes.Coordinate.我的页坐标['valuex'],dataes.Coordinate.我的页坐标['valuey'])
            publicmethods(self.driver).wait(page.MinePage.资产总览['type'], 5, page.MinePage.资产总览['value'])
            # 上滑页面
            publicmethods(self.driver).swipeUpDown(0.5,0.8,0.2)
            time.sleep(1)
            publicmethods(self.driver).findelement(page.MinePage.系统设置['type'],page.MinePage.系统设置['value']).click()
            publicmethods(self.driver).wait(page.MinePage.重置数据['type'],5,page.MinePage.重置数据['value'])
            publicmethods(self.driver).findelement(page.MinePage.重置数据['type'],page.MinePage.重置数据['value']).click()
            publicmethods(self.driver).wait(page.AlertPage.确定['type'], 5, page.AlertPage.确定['value'])
            publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
            # 重置系统数据后，为防止后续操作找不到元素，所以重启一次APP，获取最新driver执行操作
            self.driver = basedriver()
            # publicmethods(self.driver).waitActivity('.major.activity.HomeActivity', 30)
            # 当出现法律弹框时操作弹框内容
            try:
                # self.assertIsNotNone(publicmethods(self.driver).findelement(page.AlertPage.确定['type'],page.AlertPage.确定['value']))
                publicmethods(self.driver).wait(page.AlertPage.确定['type'], 15, page.AlertPage.确定['value'])
                publicmethods(self.driver).findelement(page.AlertPage.确定['type'], page.AlertPage.确定['value']).click()
                publicmethods(self.driver).tapPage(dataes.Coordinate.行情页坐标['valuex'], dataes.Coordinate.行情页坐标['valuey'])
            except:
                pass
            publicmethods(self.driver).findelement(page.MinePage.我的['type'], page.MinePage.我的['value']).click()
            publicmethods(self.driver).findelement(page.MinePage.登录['type'],page.MinePage.登录['value']).click()
            try:
                publicmethods(self.driver).wait(page.AcivePage.短信激活['type'],5,page.AcivePage.短信激活['value'])
                publicmethods(self.driver).findelement(page.AcivePage.短信激活['type'],page.AcivePage.短信激活['value'])\
                    .click()
            except:
                pass
            publicmethods(self.driver).wait(page.AcivePage.激活手机号['type'],5,page.AcivePage.激活手机号['value'])
            publicmethods(self.driver).findelement(page.AcivePage.激活手机号['type'],page.AcivePage.激活手机号['value']).send_keys(
                publicmethods(self.driver).creatPhone())
            publicmethods(self.driver).findelement(page.AcivePage.发送激活验证码['type'],page.AcivePage.发送激活验证码['value']).click()
            publicmethods(self.driver).findelement(page.AcivePage.激活验证码['type'], page.AcivePage.激活验证码['value']).send_keys(
                publicmethods(self.driver).creatCode())
            publicmethods(self.driver).findelement(page.AcivePage.激活['type'], page.AcivePage.激活['value']).click()
            try:
                # 查询能否找到登录按钮，能找到说明页面跳转，激活成功，案例通过，未找到时进入异常处理，给定False值传入Flag，案例失败
                # self.assertIsNotNone(publicmethods(self.driver).findelement(page.AcivePage.激活['type'], page.AcivePage.激活['value']))
                publicmethods(self.driver).wait(page.LoginPage.登录xpath['type'],5,page.LoginPage.登录xpath['value'])
                # publicmethods(self.driver).wait(page.LoginPage.登录xpath['type'],5,page.LoginPage.发送登录验证码['value'])
                publicmethods(self.driver).getScreenShot('激活手机号', '成功')
            except:
                print('未找到指定控件，案例失败')
                self.assertEqual(1,2)
        except:
            publicmethods(self.driver).getScreenShot('激活手机号', '失败')
            # 报错信息
            raise

    def tearDown(self):
        publicmethods(self.driver).quit()