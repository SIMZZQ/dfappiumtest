# coding:utf-8
import unittest,time,os
import HTMLTestRunner

suite = unittest.TestSuite()
runpath = os.path.dirname(os.path.realpath(__file__))
case_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'business') #case的路径
allcases = unittest.defaultTestLoader.discover(case_dir,pattern='test_*.py') #在case路径下找到所有以test开头命名的文件
#将所有案例添加进套件
for case in allcases:
    suite.addTests(case)
# 定义报告路径和名字
now = time.strftime("%Y-%m-%d_%H-%M-%S")
try:
    os.makedirs(os.path.join(runpath,'report'))
except:
    pass
fliename = 'D:/test_case/myyamltest/report/%s_result.html'%now
# 给定文件操作权限
fp = open(fliename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'账户主流程回归测试',
    description=u'测试案例运行结果',
    tester=u'张展齐',
    verbosity=2
)
# runner = unittest.TextTestRunner()
runner.run(suite)
fp.close()