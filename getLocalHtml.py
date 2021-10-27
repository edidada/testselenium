# -*- coding: utf-8 -*-

from selenium import webdriver


def printHandlers():
    # 获取所有的打开的标签页句柄
    all_handles = driver.window_handles
    print('tab_count: ' + str(len(all_handles)))


if __name__ == '__main__':

    # 1、创建Chrome实例 。
    driver = webdriver.Chrome()
    # 2、driver.get方法将定位在给定的URL的网页 。
    driver.get("file:///D:/PycharmProjects/testselenium/html/a.html") # get接受url可以是如何网址，此处以百度为例

    driver.maximize_window()

    # 3、定位元素 。
    # 3.1、用id定位输入框对象，
    driver.find_element_by_id("dfasdfa").send_keys("python")

    driver.find_element_by_id("a__a").click()

    printHandlers()

    # 切换到标签页1
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_id("bb_d").click()
    printHandlers()

    # 4、退出访问的实例网站。
    # driver.quit()
