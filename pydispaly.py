# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pydispaly
   Description :
   Author :       wsm
   date：          2019-01-13
-------------------------------------------------
   Change Activity:
                   2019-01-13:
-------------------------------------------------
"""
__author__ = 'wsm'

from pyvirtualdisplay import Display
from selenium import webdriver

# 以不打开浏览器的 加载 web 动态 页面
# 在 linux 下 使用
display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Chrome(executable_path='/Users/wsm/Downloads/chromedriver')
browser.get('https://www.baidu.com')
browser.close()