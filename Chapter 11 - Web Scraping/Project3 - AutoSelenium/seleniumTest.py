#================================================================================================
# (1) 使用前准备
# 更新 FireFox 浏览器到最新版本
#       安装方式 : http ://getfirefox.com/
#       更新方式 ：帮助 -> 关于 firefox -> 更新
#
# 安装 geckodriver
#   1) 下载地址：https :/ /github.co m /mozill a /geckodrive r /releases
#   2) 下载解压后将getckodriver.exe复制到Firefox的安装目录下，如（C:\Program Files\Mozilla Firefox）
#       在环境变量Path中添加路径：C:\Program Files\Mozilla Firefox；
#================================================================================================
from selenium import webdriver

browser = webdriver.Firefox()
type(browser)
browser.get('http://cn.bing.com')


browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')