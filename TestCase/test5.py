from Config.EcshopConf import *
from Public.EcshopAPI import *
import unittest
import time
# from Public.TestCaseExcel import write_excel_xls_append

class ecshophoutai(unittest.TestCase):
    def setUp(self):
        self.driver = Ecshop()  # 创建ecshop类对象
        self.driver.wait(10)   #时间智能等待

        self.ht = ecshop_admin_url  #调用Ecshop商城的登录网址

        self.driver.max_window()  # 把窗口最大化


    def test_03_login(self):   #正常登录测试用例
        d = self.driver   # 把self.driver 赋值给d,这个方法都可以用这个变量
        d.open(self.ht)   # 调用EcshopAPI类   open的方法  打开 后台管理系统网址
        try:
            d.input_text("name", "username", admin_username) # input_text是ecshopAPI类的方法
            d.input_text('name', 'password', admin_passwd)  # input_text是ecshopAPI类的方法
            d.click("class", "btn-a")   #click是 是ecshopAPI类的方法
            time.sleep(3)

            # 网址断言
            # 断言函数 assert断言是声明布尔值必须为真的判定，如果发生异常就说明表达式为假。

            self.assertNotEqual(ecshop_admin_url, d.get_url(), msg="url是否一致")
            print('执行测试用例3--成功(登录)')
            print(2)
            self.driver.wait(5)
            # write_excel_xls_append(1, "Pass")  # 如果执行成功，则写入测试用例，状态为pass.1表示测试用例
        except:
            # driver.save_windows_img(driver.get_image_path())  # 出错的时候，在当前页面进行截图
            # write_excel_xls_append(1, "Fail")  # 如果执行失败，则写入测试用例，状态为.1表示测试用例
            print("测试测试用例3--失败(失败)")

            # 断言在测试报告
            self.assertEqual(ecshop_admin_url, d.get_url(), msg="url是否一致")
            time.sleep(2)



    def test_04login(self):    #登录密码错误
        d=self.driver #重新赋值
        self.driver.wait(3)
        self.ht=ecshop_admin_url  #调用Ecshop商城的登录网址
        d.open(self.ht)
        self.driver.max_window()  # 把窗口最大化

        try:
            d.input_text('name','username',admin_username) # 调用登录帐号
            d.input_text('name','password',admin1)  #调用登录密码
            d.click('class','btn-a') #单机登录
            self.driver.wait(3)

            self.assertTrue(self.driver.get_element("xpath", "//a[@href='javascript:history.go(-1)']"), msg="登录密码错误")
            print(3)
            print('密码错误登录4--验证成功')


        except:
            print('密码错误登录4--验证失败')


    def tearDown(self):
        # 退出驱动
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
















if __name__ == '__main__':
    unittest.main()

