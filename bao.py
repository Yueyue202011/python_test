# """
#     自带的包
# """
# import time     # 时间相关 time.sleep(3)
# import sys      # 系统相关
# import unittest     # 自动化测试框架


# # 第三方包的导入
# from selenium import webdriver

# # requests
# import requests

# # 自定义的包
from test.a import aa
print(aa)

"""
    异常处理
"""
try:
    a = [7,6,1]
    print(a[55])
    print("200")
except:
    print("404")

print("999")