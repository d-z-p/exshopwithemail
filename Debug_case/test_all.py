import time
import os
from selenium import webdriver


# image_path = os.path.join(r'C:\Users\Administrator\PycharmProjects\ts16\day8\Error_Picture\\')
# now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# image = image_path + now + ".png"
# time.sleep(1)
#
# print(image)
# image_path = os.path.join(os.getcwd(), 'Error_Picture\\')
# now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
# image = image_path + "_" + now + ".png"
# time.sleep(1)
# # print(image)
# return image



driver = webdriver.Firefox()
image_path = os.path.join(os.getcwd(), 'Error_Picture\\')
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
image = image_path + now + ".png"
time.sleep(1)
print(image)
driver.get_screenshot_as_file(image)

