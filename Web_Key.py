#封装关键字类
from time import sleep

from selenium import webdriver


def Browser(_type):
    try:
        driver = getattr(webdriver,_type)()
    except:
        driver = webdriver.Chrome()

    return driver

class WebKey():

    def __init__(self,_type):
        self.driver = Browser(_type)
    #启动浏览器
    #driver = webdriver.Chrome

    #访问地址
    def open(self,url):
        self.driver.get(url)
    #获取元素
    def locator(self,name,value):
        return self.driver.find_element(name,value)
    #输入文本
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)
    #点击元素
    def click(self,name,value):
        self.locator(name,value).click()
    #强制等待
    def wait(self,_time):
        sleep(_time)
    #关闭浏览器
    def quit(self):
        self.driver.quit()