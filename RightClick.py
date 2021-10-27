from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from time import sleep

if __name__ == '__main__':
    # 代码的健壮性
    options = webdriver.ChromeOptions()
    out_path = 'D:/PycharmProjects/testselenium'  # 是你想指定的路径
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': out_path}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='D:/PycharmProjects/testselenium/chromedriver.exe', chrome_options=options)
    driver.get('https://www.jianshu.com/');

# 选择元素
    wait = WebDriverWait(driver,10)
    # 右键单击图片
    img = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'img')))
    # 执行鼠标动作
    actions = ActionChains(driver)
    # 找到图片后右键单击图片
    actions.context_click(img)
    actions.perform()
    # 发送键盘按键
    #
    # ，根据不同的网页，
    # 右键之后按对应次数向下键，
    # 找到图片另存为菜单
    pyautogui.typewrite(['down','down','down','down','down','down','down','down','enter','enter'])
    # 单击图片另存之后等1s敲回车
    sleep(1)
    pyautogui.typewrite(['enter'])