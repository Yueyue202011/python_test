# # 循环语句：有规律且重复操作的语句

# # 列表
# a = [1,2,3,4]
# for i in a :    # for中的in不是判断
#     print(i)

# # 元组
# b = ("123", 13,15,55)
# for i in b:
#     print(i)

# # 字符串变量
# c = "春节快乐"
# for i in c :
#     print(i)

# # 字典
# d = {"username":"沈小姐","password":"123456"}
# for i in d :
#     print(i)
#     # print(d[i])         # key方式取值
#     print(d.get(i))     # get的方式取值
#     print("===========")

# # d.get("laodi")和d["laodi"]的区别如果键值对不存在，get取空值，key值会报错
# a = d.get("laodi")
# print(a)
# b  = d["laodi"]
# print(b)


# while

# a = 1 
# while a < 10:   # 满足条件，就继续执行while里面的内容，不满足，就不会执行了
#     print(a)
#     a = a + 1


"""
输入账号和密码，去判断bili中是否存在，如果已经存在，就修该账号的密码，如果不存在，
就新增一个字典
"""
bili = [
    {"username":"laodi","password":"666"},
]
u = input("请输入账号：")
p = input("请输入密码：")

for i in bili:
    if u == i.get("username"):
        if p == i.get("password"):
            print("{}登陆成功！".format(u))
            newPass = input("请输入新的密码：")
            i["password"] = newPass
            print("您的新密码是：",i.get("password"))
            print(bili)
            break
        else:
            print("账号密码错误，登录失败！")
    else:
        c = {}
        c["username"] = u
        c["password"] = p
        bili.append(c)
        print(bili)
        break
