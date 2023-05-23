from Config.EcshopConf import *
from Public.EcshopAPI import *
import unittest, time

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
            time.sleep(2)
            # 点击购物车
            driver.click_text('购物车')
            time.sleep(5)
            # 点击’继续购物‘按钮
            driver.click('xpath', '//img[@src="themes/default/images/continue.gif"]')
            time.sleep(2)
            # 点击商品’视频‘
            print("4")
            driver.click('xpath', '//img[@alt="视频"]')
            time.sleep(2)
            # 点击商品’视频‘的’立即购买‘按钮
            print("3")
            driver.click('xpath', '//img[@src="themes/default/images/buybtn1.png"]')
            time.sleep(2)

            # #点击商品’视频‘的数量
            driver.click('xpath', '//input[@type="text" and @class="inputBg"]')
            print("1")
            # 清空商品’视频‘的数量
            driver.input_clear('xpath', '//input[@type="text" and @class="inputBg"]')
            time.sleep(3)
            # #修改商品’视频‘的数量为8
            print("2")
            driver.input_text('xpath', '//input[@type="text" and @class="inputBg"]', '8')
            time.sleep(10)

            # #点击’更新购物车‘按钮
            driver.click('xpath','//input[@value="更新购物车"]')
            time.sleep(10)

            # 网址断言
            # self.assertEqual(echsop_url, driver.get_url(), msg="url是否一致")
            # write_excel_xls_append(1, "Pass")  # 如果执行成功，则写入测试用例，状态为pass.1表示测试用例
        except:
            # driver.save_windows_img(driver.get_image_path())  # 出错的时候，在当前页面进行截图
            # write_excel_xls_append(1, "Fail")  # 如果执行失败，则写入测试用例，状态为.1表示测试用例
            print("testcase error")

            # 断言在测试报告
            self.assertEqual(echsop_url, driver.get_url(), msg="url是否一致")

            # class gouwu(unittest.TestCase):
            #     def test_01addnumber(self):
            #         driver = self.driver
            #         driver.open(self.base_url)
            #         driver.click_text("购物车")
            #         try:
            #             driver.click()
            #

    def tearDown(self):
        # 退出驱动
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
