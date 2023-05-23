from Config.EcshopConf import *
from Public.EcshopAPI import *
import time

import unittest

class zuce(unittest.TestCase):
    def setUp(self):
        self.driver = Ecshop()  # 创建对象 引用Ecshop类下所有的方法
        self.driver.wait(10)   #智能等待十秒
        self.wangzhi=echsop_url   #调取引用 Ecshopconf的前端网址
        self.driver.max_window() #最大化窗口


    def test_01regedit(self):
        s=self.driver  #把self.driver的方法 赋值给s这个变量  ，s就都可以使用他的方法
        s.open(self.wangzhi)  # 打开网址
        s.wait(3)  #智能等待延迟3秒
        s.click_text('登录')  # 单 点击登录

        try:
            s.input_text('name','username',echsop_username)
            s.input_text('name','password',echsop_passwd)
            time.sleep(1)
            s.click('name','submit')
            self.assertTrue(self.driver.get_element("xpath", "//a[@href='user.php?act=logout']"), msg='登录失败')
            print('执行测试用例2--成功')
            print(1)
            s.wait(3)
        except:
            print('执行测试用例2--失败')
            self.assertTrue(self.driver.get_element("xpath", "//a[@href='user.php?act=logout']"), msg='登录失败')
            time.sleep(1)



    def test_02regedit_pass(self):  #用例1    正常注册
        driver=self.driver
        driver.open(self.wangzhi)
        driver.wait(3)
        driver.click_text('免费注册')

        try:
            driver.input_text("name", "username", "qq31")
            driver.wait(1)
            driver.input_text('name', 'email', "390@qq.com")  # 邮件地址
            driver.input_text('name', 'password', '123456')
            driver.input_text('name', 'confirm_password', '123456')
            driver.input_text('name', 'extend_field2', '888')
            driver.input_text('name', 'extend_field3', '888')
            driver.input_text('name', 'extend_field4', '888')
            driver.input_text('name', 'extend_field5', '888')
            driver.click('name', 'Submit')
            self.assertTrue(self.driver.get_element("xpath", "//a[@href='user.php?act=logout']"),msg='注册失败')
            print('注册成功')
            print(1)
        except:
            print('执行--测试用例01--出现错误')

    def tearDown(self):
        # 退出驱动
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

















