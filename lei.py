
class Person():
    # 变量：成员变量：类中的变量
    name = "老爷"
    sex = "男"
    age = 19

    # 功能：成员方法：类中的方法
    # def talk(self):     # self,是成员方法的第一个参数，Ipython的语法要求
    #     print("{}能说话".format(self.name))

    # def eat(self,dx):
    #     print("大吉大利，今晚吃{}".format(dx))
    #     return "吃鸡了"

    # def test(self):
    #     self.talk()
# 实例化类:Person()
# p：实例化对象

# 调用成员变量
p = Person()
print(p.name)
print(p.sex)
print(p.age)

# p.talk()
# a = p.eat("什么")
# print(a)

# p.test()




# class Person1():

#     xm = "老狗"
#     # 构造方法：__init__，在实例化的时候给新建/初始化成员变量：固定的写法
#     def __init__(self,nl):
#         self.age = nl     # 新建一个成员变量age 

# # self：如果成员变量没有写，则新建一个成员变量，写了就是赋值
# p = Person1(18)
# print(p.xm)
# print(p.age)