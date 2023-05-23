from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

'''
封装这些类，是有利于修改和维护，而且使用起来也方便很多
'''


class Ecshop:
    def __init__(self):
        # 选择默认火狐浏览器---根据自己选择而定
        driver = webdriver.Chrome()
        self.driver = driver

    def element_wait(self):
        "implicitly_wait 智能等待五秒钟"

        self.driver.implicitly_wait(5)

    def get_element(self, ele, ele_path):
        '''
        Judge element positioning way, and returns the element.
        --------判断元素，并反回操作
        '''

        if ele == "id":
            element = self.driver.find_element_by_id(ele_path)
        elif ele == "name":
            element = self.driver.find_element_by_name(ele_path)
        elif ele == "class":
            element = self.driver.find_element_by_class_name(ele_path)
        elif ele == "link_text":
            element = self.driver.find_element_by_link_text(ele_path)
        elif ele == "xpath":
            element = self.driver.find_element_by_xpath(ele_path)
        elif ele == "css":
            element = self.driver.find_element_by_css_selector(ele_path)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        '''
        open url.
        --------打开页面
        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)

    def max_window(self):
        '''
        Set browser window maximized.
        --------最大化窗口
        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.
        --------设置页面的宽度与高度
        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)

    def input_text(self, ele, ele_path, text):
        '''
        Operation input box.
        --------输入信息操作
        Usage:
        driver.type("css=>#el","selenium")
        '''
        # self.element_wait()  # 智能等待
        el = self.get_element(ele, ele_path)  # 按照指定的去匹配用什么方式去查找元素
        el.send_keys(text)

    def input_test(self, ele, ele_path):
        el = self.get_element(ele, ele_path)  # 按照指定的去匹配用什么方式去查找元素
        return el.text

    def input_clear(self, ele, ele_path):
        '''
        Clear the contents of the input box.
        --------清除操作
        Usage:
        driver.clear("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        el.clear()

    def click(self, ele, ele_path):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        --------单击操作
        Usage:
        driver.click("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        el.click()

    def right_click(self, ele, ele_path):
        '''
        Right click element.
        --------右击操作
        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, ele, ele_path):
        '''
        Mouse over the element.
        --------悬浮操作
        Usage:
        driver.move_to_element("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, ele, ele_path):
        '''
        Double click element.
        --------双击操作
        Usage:
        driver.double_click("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.
        --------拖动元素操作
        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.element_wait()
        element = self.get_element(el_css)
        self.element_wait()
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        '''
        Click the element by the link text
        --------单击操作
        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.
        --------关掉当前操作页面页面
        Usage:
        driver.close()
        '''
        self.driver.close()

    def quit(self):
        '''
        Quit the driver and close all the windows.
        --------关闭浏览器（包括多个table页面）
        Usage:
        driver.quit()
        '''
        self.driver.quit()

    def submit(self, ele, ele_path):
        '''
        Submit the specified form.
        --------submit按钮提交
        Usage:
        driver.submit("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        el.submit()

    def F5(self):
        '''
        Refresh the current page.
        --------刷新页面
        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        '''
        Execute JavaScript scripts.
        --------js脚本执行
        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)

    def get_attribute(self, ele, ele_path, attribute):
        '''
        Gets the value of an element attribute.
        --------获取属性值
        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(ele, ele_path)
        return el.get_attribute(attribute)

    def get_text(self, ele, ele_path):
        '''
        Get element text information.
        --------获取元素的文本
        Usage:
        driver.get_text("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        return el.text

    def get_display(self, ele, ele_path):
        '''
        Gets the element to display,The return result is true or false.
        --------获取当前按钮的可以状态
        Usage:
        driver.get_display("css=>#el")
        '''
        self.element_wait()
        el = self.get_element(ele, ele_path)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.
        --------获取当前页面的标题
        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.
        ------获取当前地址URL
        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def save_windows_img(self, file_path):
        '''
        Get the current window screenshot.
        --------
        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)

    def get_image_path(self):
        """
        --------断言时，进行一个截图，放在当前目录下的Error_Picture下
        """
        import time, os
        image_path = os.path.join(os.getcwd(), 'Error_Picture\\')
        now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        image = image_path + now + ".png"
        time.sleep(1)
        # print(image)
        return image

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.
        --------等时间
        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        '''
        Accept warning box.
        --------获取弹窗消息
        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.
        --------弹窗，点击取消
        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, ele, ele_path):
        '''
        Switch to the specified frame.
        --------切到另一个frame标签中
        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        self.element_wait(
        )
        iframe_el = self.get_element(ele, ele_path)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        --------切到frame标签框外
        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()

    def open_new_window(self, ele, ele_path):
        '''
        Open the new window and switch the handle to the newly opened window.
        ---------打开新的一个窗口，而且切换到当前窗口句柄
        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element(ele, ele_path)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def accept_txt(self):
        '''
        Accept warning box.
        --------获取弹窗消息
        Usage:
        driver.accept_alert()
        '''
        a = self.driver.switch_to.alert
        return a.text