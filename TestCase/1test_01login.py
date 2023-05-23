from Config.EcshopConf import *
from Public.EcshopAPI import *
import unittest, time



# from Public.TestCaseExcel import write_excel_xls_append





class ecshoplogin(unittest.TestCase):
    def setUp(self):
        self.driver = Ecshop()  # 创建ecshop类对象
        self.driver.wait(10)
        self.base_url = echsop_url

    def test_01_login(self):
        driver = self.driver
        driver.open(self.base_url)
        driver.click_text("请登录")
        try:
            driver.input_text("name", "username", echsop_username)
            driver.input_text('name', 'password', echsop_passwd)
            driver.click("name", "submit")
            time.sleep(5)

            # 网址断言
            self.assertEqual(echsop_url, driver.get_url(), msg="url是否一致")
            # write_excel_xls_append(1, "Pass")  # 如果执行成功，则写入测试用例，状态为pass.1表示测试用例
        except:
            # driver.save_windows_img(driver.get_image_path())  # 出错的时候，在当前页面进行截图
            # write_excel_xls_append(1, "Fail")  # 如果执行失败，则写入测试用例，状态为.1表示测试用例
            print("testcase error")

            # 断言在测试报告
            self.assertEqual(echsop_url, driver.get_url(), msg="url是否一致")



    def tearDown(self):
        # 退出驱动
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()