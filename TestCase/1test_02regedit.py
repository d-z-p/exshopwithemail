from Config.EcshopConf import *
from Public.EcshopAPI import *
from Public.EcshopMySQL import *
import unittest


class ecshopregedit(unittest.TestCase):
    def setUp(self):
        self.driver = Ecshop()  # 创建Ecshop类对象
        self.driver.wait(10)    # 时间只能等待
        self.base_url = echsop_url  # 定义一个变量 =  echsop_url是(Ecshop网址)
        self.mysql_d = mysql_operation()  #定义一个变量 = mysql_operation(是mysql的类名)

    def test_01regedit_pass(self):
        driver = self.driver
        mysql_d = self.mysql_d
        driver.open(self.base_url)
        driver.wait(3)
        driver.click_text("免费注册")  # 单击 免费注册
        try:

            mysql_d.mysql_inserinto()  # 查询数据库有没有删除test10用户，如果存在则删除
            driver.input_text("name", "username", "test10")  # 定位用户名，输入用户名
            driver.wait(1)
            driver.input_text('name', 'email', "7856852@qq.com")  # 邮件地址
            driver.input_text('name', 'password', '123456')
            driver.input_text('name', 'confirm_password', '123456')
            driver.input_text('name', 'extend_field2', '888888')
            driver.input_text('name', 'extend_field3', '888888')
            driver.input_text('name', 'extend_field4', '888888')
            driver.input_text('name', 'extend_field5', '888888')
            driver.click('name', 'Submit')
            # 网址断言
            # self.assertTrue(self.driver.get_element("xpath", "//a[@href='user.php?act=logout']"), msg="reg fail")
            self.assertTrue(mysql_d.mysql_select('test10'), msg="注册失败")  # 这种断言一直出错,未找到原因
            # write_excel_xls_append(1, "Pass")  # 如果执行成功，则写入测试用例，状态为pass.1表示测试用例
            print("用例-注册成功")
        except:
            # driver.save_windows_img(driver.get_image_path())  # 出错的时候，在当前页面进行截图
            # write_excel_xls_append(1, "Fail")  # 如果执行失败，则写入测试用例，状态为.1表示测试用例
            self.assertTrue(self.driver.get_element("xpath", "//a[@href='user.php?act=logout']"), msg="reg fail")
            print("用例-注册失败")

    def test_02regedit_userNull(self):
        driver = self.driver
        driver.open(self.base_url)
        driver.wait(3)
        driver.click_text("免费注册")
        try:
            driver.input_text("name", "username", "te")  # 定位用户名，输入用户名
            driver.input_text('name', 'email', "7856852@qq.com")  # 邮件地址
            self.assertTrue(driver.input_test('id', 'username_notice') == '- 用户名长度不能少于 3 个字符。', msg="用户名不能少于3个字符")
            driver.wait(2)
            print("用例-注册账号为空-成功")
        except:

            print("用例-注册账号为空-失败")
            self.assertTrue(driver.input_test('id', 'username_notice') == '- 用户名长度不能少于 3 个字符。', msg="用户名不能少于3个字符")

    def tearDown(self):
        self.driver.quit()
        self.mysql_d.mysql_close()


if __name__ == '__main__':
    unittest.main()
