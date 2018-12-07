# -*- coding: utf-8 -*-

from dfappiumtest.data import data_tool

dataes = data_tool.parseyaml()


def get_dataes(clazz_name, method_name):
    datum = dataes[clazz_name]['Data']
    for data in datum:
        if data['name'] == method_name:
            return data


class BindAccountInfo:
    资金账号 = get_dataes('BindAccountInfo', '资金账号')

    
class BindPhone:
    资金账号 = get_dataes('BindPhone', '资金账号')

    
class CashTreasure:
    金额 = get_dataes('CashTreasure', '金额')

    
class ChangePhone:
    资金账号 = get_dataes('ChangePhone', '资金账号')

    
class Coordinate:
    行情页坐标 = get_dataes('Coordinate', '行情页坐标')
    我的页坐标 = get_dataes('Coordinate', '我的页坐标')

    
class ForgetAccountInfo:
    账号00123382三要素 = get_dataes('ForgetAccountInfo', '账号00123382三要素')

    
class ForgetPayPswInfo:
    持卡人 = get_dataes('ForgetPayPswInfo', '持卡人')
    身份证 = get_dataes('ForgetPayPswInfo', '身份证')
    卡号 = get_dataes('ForgetPayPswInfo', '卡号')
    手机号 = get_dataes('ForgetPayPswInfo', '手机号')
    验证码 = get_dataes('ForgetPayPswInfo', '验证码')

    
class FundAccountLogin:
    资金账号1 = get_dataes('FundAccountLogin', '资金账号1')
    资金账号2 = get_dataes('FundAccountLogin', '资金账号2')

    
class FundAccountPsw:
    资金账号通用密码 = get_dataes('FundAccountPsw', '资金账号通用密码')

    
class IdentityInfo:
    手机18721627126三要素信息 = get_dataes('IdentityInfo', '手机18721627126三要素信息')

    
class PhoneAccount:
    实名纯手机号 = get_dataes('PhoneAccount', '实名纯手机号')
    资金号加手机号 = get_dataes('PhoneAccount', '资金号加手机号')
    有密码手机号 = get_dataes('PhoneAccount', '有密码手机号')
    重置支付密码手机号 = get_dataes('PhoneAccount', '重置支付密码手机号')
    绑定资金账号手机号 = get_dataes('PhoneAccount', '绑定资金账号手机号')
    忘记资金账号手机号 = get_dataes('PhoneAccount', '忘记资金账号手机号')
    现金宝充值手机号 = get_dataes('PhoneAccount', '现金宝充值手机号')

    
class PhonePassword:
    手机通用登录密码 = get_dataes('PhonePassword', '手机通用登录密码')

    
class VerificationCode:
    验证码 = get_dataes('VerificationCode', '验证码')

    