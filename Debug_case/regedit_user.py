from selenium import webdriver
import unittest

driver = webdriver.Firefox()
driver.get("http://localhost/ecshop/user.php?act=register")

driver.find_element_by_name("username").send_keys("test")
driver.find_element_by_name("email").send_keys("1090747962@qq.com")

print(driver.find_element_by_id("username_notice").text)

if ("- 用户名长度不能少于 3 个字符。") == driver.find_element_by_id("username_notice").text:
    print("1")
