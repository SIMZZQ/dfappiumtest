# -*- coding: utf-8 -*-

from dfappiumtest.page import elements_tool

pages = elements_tool.parseyaml()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class AcivePage:
    激活手机号 = get_locater('AcivePage', '激活手机号')
    激活验证码 = get_locater('AcivePage', '激活验证码')
    发送激活验证码 = get_locater('AcivePage', '发送激活验证码')
    激活 = get_locater('AcivePage', '激活')

    
class AlertPage:
    确定 = get_locater('AlertPage', '确定')

    
class BindPhone:
    手机号 = get_locater('BindPhone', '手机号')
    绑定手机号 = get_locater('BindPhone', '绑定手机号')
    手机号输入框 = get_locater('BindPhone', '手机号输入框')
    发送验证码 = get_locater('BindPhone', '发送验证码')
    验证码 = get_locater('BindPhone', '验证码')
    确定 = get_locater('BindPhone', '确定')

    
class CashTreasurePay:
    现金宝 = get_locater('CashTreasurePay', '现金宝')
    收益页充值 = get_locater('CashTreasurePay', '收益页充值')
    金额 = get_locater('CashTreasurePay', '金额')
    充值页充值 = get_locater('CashTreasurePay', '充值页充值')
    继续购买 = get_locater('CashTreasurePay', '继续购买')
    我知道了 = get_locater('CashTreasurePay', '我知道了')
    充值成功 = get_locater('CashTreasurePay', '充值成功')
    返回 = get_locater('CashTreasurePay', '返回')

    
class ChangeDealPsw:
    修改资金账户交易密码 = get_locater('ChangeDealPsw', '修改资金账户交易密码')
    修改资金账户交易密码text = get_locater('ChangeDealPsw', '修改资金账户交易密码text')
    原交易密码 = get_locater('ChangeDealPsw', '原交易密码')
    新交易密码 = get_locater('ChangeDealPsw', '新交易密码')
    确认新密码 = get_locater('ChangeDealPsw', '确认新密码')
    确定 = get_locater('ChangeDealPsw', '确定')
    密码修改成功 = get_locater('ChangeDealPsw', '密码修改成功')
    完成 = get_locater('ChangeDealPsw', '完成')

    
class ChangeFundPsw:
    修改资金账户资金密码 = get_locater('ChangeFundPsw', '修改资金账户资金密码')
    修改资金账户资金密码text = get_locater('ChangeFundPsw', '修改资金账户资金密码text')
    原资金密码 = get_locater('ChangeFundPsw', '原资金密码')
    新资金密码 = get_locater('ChangeFundPsw', '新资金密码')
    确认新密码 = get_locater('ChangeFundPsw', '确认新密码')
    确定 = get_locater('ChangeFundPsw', '确定')
    密码修改成功 = get_locater('ChangeFundPsw', '密码修改成功')
    完成 = get_locater('ChangeFundPsw', '完成')

    
class ChangePhone:
    旧手机验证码 = get_locater('ChangePhone', '旧手机验证码')
    更换手机号 = get_locater('ChangePhone', '更换手机号')
    旧手机下一步 = get_locater('ChangePhone', '旧手机下一步')
    新手机号 = get_locater('ChangePhone', '新手机号')
    发送验证码 = get_locater('ChangePhone', '发送验证码')
    验证码 = get_locater('ChangePhone', '验证码')
    新手机号确定 = get_locater('ChangePhone', '新手机号确定')

    
class ChangeShoushiPsw:
    修改手势密码 = get_locater('ChangeShoushiPsw', '修改手势密码')
    请输入原手势密码 = get_locater('ChangeShoushiPsw', '请输入原手势密码')
    请设置手势密码 = get_locater('ChangeShoushiPsw', '请设置手势密码')
    请再次绘制手势密码 = get_locater('ChangeShoushiPsw', '请再次绘制手势密码')
    异常错误 = get_locater('ChangeShoushiPsw', '异常错误')

    
class ForgetPayPswPage:
    持卡人 = get_locater('ForgetPayPswPage', '持卡人')
    身份证 = get_locater('ForgetPayPswPage', '身份证')
    卡号 = get_locater('ForgetPayPswPage', '卡号')
    手机号 = get_locater('ForgetPayPswPage', '手机号')
    获取验证码 = get_locater('ForgetPayPswPage', '获取验证码')
    验证码 = get_locater('ForgetPayPswPage', '验证码')
    确定 = get_locater('ForgetPayPswPage', '确定')
    支付密码 = get_locater('ForgetPayPswPage', '支付密码')
    确认密码 = get_locater('ForgetPayPswPage', '确认密码')
    下一步 = get_locater('ForgetPayPswPage', '下一步')
    忘记理财支付密码主页 = get_locater('ForgetPayPswPage', '忘记理财支付密码主页')
    安全软键盘页 = get_locater('ForgetPayPswPage', '安全软键盘页')

    
class ForgetShoushiPsw:
    忘记手势密码 = get_locater('ForgetShoushiPsw', '忘记手势密码')
    输入交易密码 = get_locater('ForgetShoushiPsw', '输入交易密码')
    确定 = get_locater('ForgetShoushiPsw', '确定')
    请设置手势密码 = get_locater('ForgetShoushiPsw', '请设置手势密码')
    请再次绘制手势密码 = get_locater('ForgetShoushiPsw', '请再次绘制手势密码')

    
class FundAccountLoginPage:
    验证码图片 = get_locater('FundAccountLoginPage', '验证码图片')
    资金账户 = get_locater('FundAccountLoginPage', '资金账户')
    交易密码 = get_locater('FundAccountLoginPage', '交易密码')
    图形验证码 = get_locater('FundAccountLoginPage', '图形验证码')
    登录 = get_locater('FundAccountLoginPage', '登录')

    
class H5KeyBoard:
    按键1 = get_locater('H5KeyBoard', '按键1')
    按键2 = get_locater('H5KeyBoard', '按键2')
    按键3 = get_locater('H5KeyBoard', '按键3')
    按键4 = get_locater('H5KeyBoard', '按键4')
    按键5 = get_locater('H5KeyBoard', '按键5')
    按键6 = get_locater('H5KeyBoard', '按键6')
    按键7 = get_locater('H5KeyBoard', '按键7')
    按键8 = get_locater('H5KeyBoard', '按键8')
    按键9 = get_locater('H5KeyBoard', '按键9')
    按键0 = get_locater('H5KeyBoard', '按键0')

    
class HistoryLoginInfo:
    登录记录 = get_locater('HistoryLoginInfo', '登录记录')

    
class JiuGongGe:
    九宫格 = get_locater('JiuGongGe', '九宫格')

    
class LoginForgetPhonePsw:
    忘记登录密码 = get_locater('LoginForgetPhonePsw', '忘记登录密码')
    手机号输入框 = get_locater('LoginForgetPhonePsw', '手机号输入框')
    手机号页下一步 = get_locater('LoginForgetPhonePsw', '手机号页下一步')
    姓名 = get_locater('LoginForgetPhonePsw', '姓名')
    身份证号 = get_locater('LoginForgetPhonePsw', '身份证号')
    实名认证页下一步 = get_locater('LoginForgetPhonePsw', '实名认证页下一步')
    重置登录密码页验证码 = get_locater('LoginForgetPhonePsw', '重置登录密码页验证码')
    重置登录密码页登录密码 = get_locater('LoginForgetPhonePsw', '重置登录密码页登录密码')
    重置登录密码页确认密码 = get_locater('LoginForgetPhonePsw', '重置登录密码页确认密码')
    重置登录密码页完成 = get_locater('LoginForgetPhonePsw', '重置登录密码页完成')
    成功页完成 = get_locater('LoginForgetPhonePsw', '成功页完成')

    
class MineFundAccountPage:
    我的资金账户 = get_locater('MineFundAccountPage', '我的资金账户')
    绑定资金账户 = get_locater('MineFundAccountPage', '绑定资金账户')
    资金账户 = get_locater('MineFundAccountPage', '资金账户')
    交易密码 = get_locater('MineFundAccountPage', '交易密码')
    确定 = get_locater('MineFundAccountPage', '确定')
    绑定成功校验 = get_locater('MineFundAccountPage', '绑定成功校验')
    忘记资金账户 = get_locater('MineFundAccountPage', '忘记资金账户')
    姓名 = get_locater('MineFundAccountPage', '姓名')
    身份证号 = get_locater('MineFundAccountPage', '身份证号')
    下一步 = get_locater('MineFundAccountPage', '下一步')
    我要绑定 = get_locater('MineFundAccountPage', '我要绑定')
    输入交易密码 = get_locater('MineFundAccountPage', '输入交易密码')
    验证交易密码确定 = get_locater('MineFundAccountPage', '验证交易密码确定')
    解绑交易密码确定 = get_locater('MineFundAccountPage', '解绑交易密码确定')
    已绑定 = get_locater('MineFundAccountPage', '已绑定')
    资金账号列表1 = get_locater('MineFundAccountPage', '资金账号列表1')
    删除 = get_locater('MineFundAccountPage', '删除')

    
class MineInfoPage:
    密码管理 = get_locater('MineInfoPage', '密码管理')
    忘记理财支付密码 = get_locater('MineInfoPage', '忘记理财支付密码')

    
class MinePage:
    我的 = get_locater('MinePage', '我的')
    交易 = get_locater('MinePage', '交易')
    理财 = get_locater('MinePage', '理财')
    登录 = get_locater('MinePage', '登录')
    系统设置 = get_locater('MinePage', '系统设置')
    资产总览 = get_locater('MinePage', '资产总览')
    重置数据 = get_locater('MinePage', '重置数据')
    退出登录 = get_locater('MinePage', '退出登录')
    我的信息 = get_locater('MinePage', '我的信息')
    机构户我的信息 = get_locater('MinePage', '机构户我的信息')

    
class LoginPage:
    手机号切换按钮 = get_locater('LoginPage', '手机号切换按钮')
    登录手机号 = get_locater('LoginPage', '登录手机号')
    发送登录验证码 = get_locater('LoginPage', '发送登录验证码')
    登录验证码 = get_locater('LoginPage', '登录验证码')
    登录 = get_locater('LoginPage', '登录')
    登录xpath = get_locater('LoginPage', '登录xpath')
    使用登录密码登录 = get_locater('LoginPage', '使用登录密码登录')
    手机号注册 = get_locater('LoginPage', '手机号注册')

    
class PhonePswLoginPage:
    登录手机号 = get_locater('PhonePswLoginPage', '登录手机号')
    登录密码 = get_locater('PhonePswLoginPage', '登录密码')
    登录 = get_locater('PhonePswLoginPage', '登录')

    
class RegisterPhonePage:
    手机号输入框 = get_locater('RegisterPhonePage', '手机号输入框')
    下一步 = get_locater('RegisterPhonePage', '下一步')
    验证码 = get_locater('RegisterPhonePage', '验证码')
    登录密码 = get_locater('RegisterPhonePage', '登录密码')
    确认密码 = get_locater('RegisterPhonePage', '确认密码')
    注册 = get_locater('RegisterPhonePage', '注册')
    完成 = get_locater('RegisterPhonePage', '完成')

    
class SingleAccountLoginPage:
    资金账号 = get_locater('SingleAccountLoginPage', '资金账号')
    交易密码 = get_locater('SingleAccountLoginPage', '交易密码')
    图形验证码 = get_locater('SingleAccountLoginPage', '图形验证码')
    验证码框 = get_locater('SingleAccountLoginPage', '验证码框')
    登录 = get_locater('SingleAccountLoginPage', '登录')

    
class ToastPage:
    手机已注册 = get_locater('ToastPage', '手机已注册')
    密码重置成功 = get_locater('ToastPage', '密码重置成功')
    资金账号验证码错误 = get_locater('ToastPage', '资金账号验证码错误')
    手机号绑定成功 = get_locater('ToastPage', '手机号绑定成功')
    手机号已绑定 = get_locater('ToastPage', '手机号已绑定')
    更换手机号已绑定 = get_locater('ToastPage', '更换手机号已绑定')
    手机号更换成功 = get_locater('ToastPage', '手机号更换成功')
    手势密码修改成功 = get_locater('ToastPage', '手势密码修改成功')

    
class TraderPage:
    选择登录账号 = get_locater('TraderPage', '选择登录账号')
    账号列表 = get_locater('TraderPage', '账号列表')
    交易页下拉箭头 = get_locater('TraderPage', '交易页下拉箭头')
    使用其他用户账户 = get_locater('TraderPage', '使用其他用户账户')
    退出交易 = get_locater('TraderPage', '退出交易')

    