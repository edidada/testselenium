# -*- coding: utf-8 -*-

import time
from selenium import webdriver

if __name__ == '__main__':
    try:
        # 创建Chrome实例
        driver = webdriver.Chrome()
        # 打开指定网址
        driver.get("https://ebank.rcbhlj.cn:44380/hljnx-test/sit2/eibs/#/login")
        # 最大化窗口
        driver.maximize_window()
        # 等待页面加载
        time.sleep(2)
        
        # 切换到用户号登录（根据实际页面结构调整选择器）
        # 假设用户号登录是通过点击一个标签实现的
        user_login_tab = driver.find_element_by_xpath("//div[contains(text(), '用户号登录')]")
        user_login_tab.click()
        time.sleep(1)
        
        # 输入手机号
        phone_input = driver.find_element_by_id("phone")
        phone_input.send_keys("13800138000")
        # 输入密码
        password_input = driver.find_element_by_id("password")
        password_input.send_keys("123456")
        # 点击登录按钮
        login_button = driver.find_element_by_id("loginBtn")
        login_button.click()
        # 等待登录结果
        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 退出浏览器
        if 'driver' in locals():
            driver.quit()
