import pymysql

def chaxun(sql):
    """
        查询数据库mysql数据库
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="localhost",user="root",password="123456",db="test10_11")

    # 获取游标：查询窗口
    cur = db.cursor()

    # 执行sql语句
    cur.execute(sql)

    # 得到执行的结果
    res = cur.fetchall()

    # 关闭程序
    db.close()

    return res

# sql = "select * from student where id = 1"
# a = chaxun(sql)
# print(a)
# print(len(a))




def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="localhost",user="root",password="123456",db="test10_11")

    # 获取游标：查询窗口
    cur = db.cursor()

    # 执行sql语句
    cur.execute(sql)

    # 提交修改
    db.commit()

    # 关闭程序
    db.close()

    return True

# # update
# sql = "UPDATE student SET phone = '999999' WHERE id =4"
# commit(sql)

# insert
# sql  = 'INSERT INTo student VALUES(333,26,"李荣浩","男","体育班",18,155,"安平")'
# commit(sql)

# delete
# sql = "delete from student where id = 25"
# commit(sql)
