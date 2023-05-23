from Public import HTMLTestRunner as HTMLTestRunner  # 导入官网的测试报告
import unittest, time
from Public.SendMail import *  # 邮件
import os

if __name__ == '__main__':

    # 执行用例部分
    test_dir = os.path.join(os.getcwd(), 'TestCase')  # 自动化测试用例路径
    test_report = os.path.join(os.getcwd(), 'Report')  # 自动化测试报告存放路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # discover 查找test_dir目录，并执行以test开头，.py结尾的文件

    # 1.定制时间格式，2.测试报告的名字定制  测试报告的名字
    now = time.strftime("%Y-%m-%d_%H_%M_%S")                # 获取当前时间以年-月-日_时_分_秒
    filename = test_report + '/Ecshop_' + now + '.html'     # 名字 test_report+年月日....html

    # # 如果没有则新建文件，有则打开这个文件，给于写入权限
    fp = open(filename, 'wb')  # 新建测试文件

    try:
        # stream=fp：文件路径，名字  title:输出测试报告的名字 description：描述名字，相当于备注信息
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Ecshop自动化测试报告", description='用例执行情况：')
        runner.run(discover)
        fp.close()
        print("执行成功")
        SendMail(filename, "1090747962@qq.com")

    except:
        print("执行失败")
        fp.close()
        SendMail(filename, "1090747962@qq.com")


"""---------POM分层 结构Page Object Model（页面对象模式）----------
1.Config:放置配置文件,配置变量, 比如前端url,后台url,账号密码,dev,sit,uat环境数据库账号密码
2.Debug_case: 调试测试用例或者代码 (就类似一个草稿)
3.Error_Picture: 出错时，进行截图
4.Log：打印日志
5.Public: 公共的类（封装）
    HTMLTestRunner： 官网下载的测试报告模板（http://tungwaiyip.info/software/HTMLTestRunner.html）
    EcshopMySQL: 数据库操作
    SendMail: 发送测试报告
    TestCaseExcel: 写入测试用例每一条Fail/Pass
    EcshopAPI: 封装了所有的webdriver方法，以及一些通用方法
6.Report: 测试完成，形成测试报告
7.TestCase: 存放自动化测试用例 
    测试用例存放以test开头，unittest框架
8.TestCaseExcel: 存放测试用例excel文件
RunAllTestCase: 执行所有的文件入口
"""


