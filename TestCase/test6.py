from Config.EcshopConf import *
from Public.EcshopAPI import *
import time

import unittest

class Deletemb(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=Ecshop() # 创建一个对象引用EcshopAPI的Ecshop，且可以使用Ecshop下所有的方法
        self.driver.wait(5) #时间智能等待
        self.wz=ecshop_admin_url   #调用后台网址使用
        self.driver.max_window()  #最大化窗口

    def test_06_login(self):
        try:
            s = self.driver    #把self.driver的方法赋值给s，s也可以使用
            s.open(self.wz)  # 调用Ecshop open方法打开网址
            s.max_window()

            s.input_text('name','username',admin_username)#调用帐号
            s.wait(3)
            s.input_text('name','password',admin_passwd) #调用密码
            s.click('class','btn-a')  #单机登录操作
            time.sleep(1)

            s.switch_to_frame('name','menu-frame') #进入frame模块
            # 会员列表  test 是获取元素，text 是输入
            s.click('xpath','//a[@href="users.php?act=list"]') # 单机进入会员管理
            time.sleep(2)
            s.switch_to_frame_out() #退出frame模块
            time.sleep(1)
            s.switch_to_frame('name','main-frame') #切换至另一个 frame模块
            s.input_text('name','keyword','61ii') #查询指定会员
            s.click('xpath','//input[@value=" 搜索 "]')  #点击搜索
            time.sleep(1)
            s.click('xpath','//input[@name="checkboxes[]" and @type="checkbox"]') # 把搜索指定的会员勾选上

            s.click('id','btnSubmit') #点击删除会员
            time.sleep(1)
            # print(s.accept_txt()) #接收弹窗消息
            s.accept_alert() #获取弹窗消息并删除
            s.wait(2)
            self.assertTrue(s.input_test('link_text','返回上一页'),msg='不成功，未显示返回上一页')
            print('测试用例5--成功，删除会员')

        except:
            print('测试用例5--失败，没有删除会员')





    # def tearDown(self) -> None:
    #     self.driver.quit()
if __name__ == '__main__':
    unittest.main()