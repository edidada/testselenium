# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    # 1、创建Chrome实例 。
    driver = webdriver.Chrome()
    # 2、driver.get方法将定位在给定的URL的网页 。
    driver.get("https://ebank.rcbhlj.cn:44380/hljnx-test/sit2/eibs/#/login")

    driver.maximize_window()

    # 3、定位元素 。
    # 3.1、切换到用户号登录
    time.sleep(2) # 等待页面加载
    # 3.2、用id定位手机号输入框，输入手机号
    driver.find_element(By.ID, "phone").send_keys("13800138000")
    # 3.3、用id定位密码输入框，输入密码
    driver.find_element(By.ID, "password").send_keys("123456")
    # 3.4、用id定位登录按钮，点击登录
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(5) # 延迟5秒查看效果
    # 4、退出访问的实例网站。
    driver.quit()
