from pymysql_demo import chaxun


# 查询
username = input("请输入姓名：")
ages = input("请输入年龄：")

sql = 'SELECT * FROM student where name = "{}" and age = {}'.format(username,ages)
print(sql)
a = chaxun(sql)

if len(a) == 0:
    print("查无此人")
else:
    print("查询成功")
    print(a)