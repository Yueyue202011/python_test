# from pymysql_demo import chaxun


# 查询
# username = input("请输入姓名：")
# ages = input("请输入年龄：")

# sql = 'SELECT * FROM student where name = "{}" and age = {}'.format(username,ages)
# print(sql)
# a = chaxun(sql)

# if len(a) == 0:
#     print("查无此人！")
# else:
#     print("查询成功！")
#     print(a)




# from pymysql_demo import chaxun
# user = input("请输入您的姓名：")
# nl = input("请输入您的年龄：")

# sql = 'SELECT * from student WHERE name = "{}" and age = {} '.format(user,nl)
# print(sql)
# jieGuo = chaxun(sql)

# if  len(jieGuo) != 0:
#     print(jieGuo)
#     print("查询成功！")
# else:
#     print("查询失败！")


# 修改
# from pymysql_demo import commit
# upname = input("请输入名字：")
# updizhi = input("请输入您要修改的地址：") 

# sql = 'UPDATE student SET diZhi = "{}" WHERE name = "{}"'.format(updizhi,upname)
# print(sql)
# b = commit(sql)
# print(b)
# if b == True:
#     print("修改成功！")
# else:
#     print("修改失败！")


# 删除
# from pymysql_demo import commit
# delId = input("请输需要删除的ID：")
# sql = "DELETE FROM student WHERE id = {}".format(delId)
# c = commit(sql)
# print(sql)
# if c == True:
#     print("删除成功！")
# else:
#     print("删除失败！")


# 增加
from pymysql_demo import commit
zjId = input("请输入增加的ID：")
zjName = input("请输入名字：")
zjBj = input("请输入班级：")
sql ='INSERT INTO teacher (id,teacher,className) VALUES({},"{}","{}")'.format(zjId,zjName,zjBj)
d = commit(sql)
print(d)
if d == True:
    print("添加成功！")
else:
    print("添加失败！")