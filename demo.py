print("hello world") 
 

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容：",a+b)


# print(type("大师傅似的"))
# print(type(2233))
# print(type(1.66))
# print(type([]))
# print(type(False))
# print(type(()))
# print(type({})) 

# a = 22
# print(float(a))


# a = "fsadasd啊实打实"
# print(len(a))

# 通过代码获取两端内容，并且计算他们长度的和
# a = len(input("请输入内容："))
# b = len(input("请输入内容："))
# c = len(input("请输入内容："))
# d = len(input("请输入内容："))
# print("总长度：",a+b+c+d)



# 元组,下标,从零开始编号
# a = (2,3,6,45,"老王","老弟","老妹",True,False,2,3,2,2,2)
# print(a[8])
# print(len(a))
# 切片
# print(a[0:4]) # 左闭右开
# print(a[4:7])
# print(a[7:14])


# print(a.index(2))   #查找某个值的下标
# print(a.count(2))   #统计某个值的数量

# 二维元组
# b = (a,16,445,688,848)
# print(len(b))
# print(b[0][5])


# 数组
a = [2,3,6,45,"老王","老弟","老妹",True,False,2,3,2,2,2,"老王","老王","老弟","老弟"]
# 剪切
# print(a)
# print(len(a))
# a.pop(6)
# print(a)
# print(len(a))

# 删除
# print(a)
# print(len(a))
# a.remove("老王")
# print(a)
# print(len(a))

# a.append("apeen")       # 往数组中追加一个
# print(a.index("老王"))   #查找某个值的下标
# print(a.count("老弟"))   #统计某个值的数量 

#元组一旦写好后不可以修改，而数组是可以修改的
# a.insert(3,"插入的值")  #往数组中指定的位置插入数据
# print(a)
# b = a.pop(6)     #剪切
# print(b)

# a.clear()   #清空
# print(a)

# xx = ["你好","再见"]
# a.extend(xx)   #合并数组
# print(a)


# a.remove("老弟")
# print(a)


"""
python的语法
所有的方法都是小括号结尾，比如，print(),int(),input()
元组、数组、字典的取值，都是用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""


"""
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是键值对的结构  key:value
3.字典的取值，是通过key去取这个value
"""
# a ={"name":"张三",55555:"老弟"}
# 取值
# print(a["name"])
# 新增
# a["age"] = "25"
#修改
# a["name"] = "李四"
# print(a)


# b = a.get("name")
# print(b)

# b = a.pop("name")
# print(b)
# print(a)

# a.update(name=1111)
# print(a)


# print(a.get("name"))
# print(a["name"])


# 数组和字典的删除
# del a["name"]
# print(a)

# del a[55555]
# print(a)


"""
获取用户输入的个人信息，并且存储到字典中
个人信息包括：name,age,sex
"""
# a = str(input("请输入您的姓名:"))
# b = int(input("请输入您的年龄:"))
# c = str(input("请输入您的性别:"))
# student = {"name":a,"age":b,"sex":c}
# print(student)