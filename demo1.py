# 去判断用户是否登陆成功
# db = [
#     {"username":"张三","password":"123456"},
#     {"username":"李四","password":"654321"}
#     ]

# zh = input("请输入账号：")
# mm = input("请输入密码：")

# for i in db:
#     # 先判断账号相等
#     if zh == i.get("username"):     # 账号相等
#         if mm == i.get("password"):
#             print("{}登陆成功".format(zh))
#             break   # 终止循环
#         else:
#             print("登录失败,密码错误")
#     else:
#         continue # 跳过本次循环,开始下一次循环


# bug1:版本
# for i in db:
#     if zh == i.get("username") and mm == i.get("password"):
#         print("输入的账号{}登录成功！".format(zh))
#     else:
#         print("登录失败！")


# for循环嵌套
# for i in db:
#     for a in i:
#         print(a)
#         print(i.get(a))
#         print("=========")


# bili = [
#     {"username":"王二","password":"555"},
#     {"username":"麻子","password":"999"},
#     {"username":"张三","password":"123456"},
#     {"username":"李四","password":"654321"}
#     ]

# zh = input("请输入账号：")
# mm = input("请输入密码：")

# for i in bili:
#     if zh == i.get("username"):
#         print(i)
#         if mm == i.get("password"):
#             print("{}登陆成功!".format(zh))
#         else:
#             print("密码错误,登录失败!")
#     else:
#         continue




# wyy = [
#     {"username":"王二","password":"555"},
#     {"username":"麻子","password":"999"},
#     {"username":"张三","password":"123456"},
#     {"username":"李四","password":"654321"}
# ]

# u = input("请输入账号：")
# p = input("请输入密码：")

# for i in wyy:
#     if u == i.get("username"):
#         if p == i.get("password"):
#             print("{}登录成功".format(u))
#             break
#         else:
#             print("账号密码错误，登录失败")





# 不同方式取值的区别
# wyy = [
#     {"username":"王二","password":"555"},
#     {"username":"麻子","password":"999"},
#     {"username":"张三","password":"123456"},
#     {"username":"李四","password":"654321"}
# ]
# d = {"username":"沈小姐","password":"123456"}

# for i in wyy:
    # print(i)
    # print(i.get("username"))
    # print(i.get("password"))
    # for a in i:
        # print(i)
        # print(a)
        # print(i[a])
        # print(i.get("username"))
        # print(i.get("password"))
# for i in d:
#     print(i)
#     print(d[i])
#     print(d.get(i))