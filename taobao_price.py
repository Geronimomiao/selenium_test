# 获取动态加载 网页内容
from scrapy.selector import Selector
from selenium import webdriver

# 设置 无图 加载
chrome_opt = webdriver.ChromeOptions()
#1允许所有图片；2阻止所有图片；3阻止第三方服务器图片
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
chrome_opt.add_experimental_option('prefs', prefs)

# 写你下载的对应 浏览器 diver 的驱动路径
# browser = webdriver.Chrome(executable_path='/home/wsm/Downloads/chromedriver')
browser = webdriver.Chrome(executable_path='/Users/wsm/Downloads/chromedriver', chrome_options=chrome_opt)


browser.get('https://item.taobao.com/item.htm?spm=a21wu.241046-tw.4691948847.3.41cab6cb990Y0R&scm=1007.15423.84311.100200300000005&id=522616952140&pvid=8523ab1c-56b6-41b1-9a21-71f9f82e10ee')
# 此处的 page_source 是相当于 运行完 js 生成的 代码
# print(browser.page_source)
t_selector = Selector(text=browser.page_source)
price = t_selector.css('.tb-rmb-num::text').extract_first()
print(price)
browser.quit()
