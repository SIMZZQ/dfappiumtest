# coding:utf-8
from appium import webdriver
import yaml,os

def basedriver():
    yp = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','config','desired_caps.yml')) #yaml文件路径
    with open(yp,'r',encoding='utf-8') as file:
        data = yaml.load(file) # 读取配置文件数据

    ap = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..','app'))
    app_path = lambda x: os.path.join(ap,x)  # 安装包路径
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    # desired_caps['app'] = app_path(data['app'])
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['automationName'] = data['automationName']
    # print(desired_caps)
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    return driver

# if __name__ == '__main__':
#     basedriver()