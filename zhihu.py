# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhihu
   Description :   selenium 模拟知乎 登录
   Author :       wsm
   date：          19-1-12
-------------------------------------------------
   Change Activity:
                   19-1-12:
-------------------------------------------------
"""
__author__ = 'wsm'
import time
from scrapy.selector import Selector
from selenium import webdriver

# 写你下载的对应 浏览器 diver 的驱动路径
browser = webdriver.Chrome(executable_path='/home/wsm/Downloads/chromedriver')

browser.get('https://www.zhihu.com/signup?next=%2F')

browser.find_element_by_css_selector('.SignContainer-switch span').click()

# 填充表单元素
username = '13001380337'
password = 'Geronimo1701'

user_input = browser.find_element_by_css_selector(".SignFlow-accountInput input[name='username']")
for char in username:
    user_input.send_keys(char)
    time.sleep(0.2)

passwd_input = browser.find_element_by_css_selector(".SignFlow-password input[name='password']")
for char in password:
    passwd_input.send_keys(char)
    time.sleep(0.2)

# 触发点击事件
browser.find_element_by_css_selector('.SignFlow-submitButton').click()

# browser.quit()

