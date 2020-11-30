import requests

# ================ get
# get请求
# url = "http://192.168.1.113:8080/dwm/;jsessionid=6F6D401565514468B14E71FDFD7AE8F4#/pages"    # 接口信息
# res = requests.get(url)      # 发送请求并且获取返回值，返回值给res
# print(res.text)             # 打印返回的信息



# ================= post
# 登录
# u = "http://192.168.1.113:8080/cas/login?service=http%3A%2F%2F192.168.1.113%3A8080%2Fdwm%2F"
# d = {"username":"admin","password":"123456"}
# res = requests.post(url=u,json=d)    # 使用post方法相u接口请求，并且使用json格式数据传参数

# # token要从登录之后来取
# token = res.json()["data"]["token"]     # res.json()把返回值变成python的字典


# ================ request
# get
u = "http://192.168.1.113:8080/dwm/;jsessionid=6F6D401565514468B14E71FDFD7AE8F4#/pages"    # 接口信息
requests.request("get",url=u)
print(res.test)


u1 = "http://192.168.1.113:8080/cas/login?service=http%3A%2F%2F192.168.1.113%3A8080%2Fdwm%2F"
d1 = {"username":"admin","password":"123456"}
requests.request("post",url=u1,json=d1)
print(res.test)
