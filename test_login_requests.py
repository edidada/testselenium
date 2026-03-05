# -*- coding: utf-8 -*-

import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import ssl
from requests.adapters import HTTPAdapter

# 禁用SSL警告
urllib3.disable_warnings(InsecureRequestWarning)

# 创建一个允许不安全重新协商的SSL上下文
class CustomHTTPAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        # 允许不安全的传统重新协商
        context.options |= ssl.OP_LEGACY_SERVER_CONNECT
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

# 创建一个会话
session = requests.Session()
# 使用自定义的HTTP适配器
session.mount('https://', CustomHTTPAdapter())

if __name__ == '__main__':
    # 登录URL
    login_url = "https://ebank.rcbhlj.cn:44380/hljnx-test/sit2/eibs/api/login"
    
    # 登录数据
    login_data = {
        "phone": "13800138000",
        "password": "123456"
    }
    
    # 请求头
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        # 发送登录请求，禁用SSL验证
        response = session.post(login_url, data=json.dumps(login_data), headers=headers, verify=False)
        
        # 打印响应结果
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        # 检查登录是否成功
        if response.status_code == 200:
            print("Login request sent successfully!")
        else:
            print("Login request failed!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 关闭会话
        session.close()
