
# class Person():
#     # 变量：成员变量：类中的变量
#     name = "哥哥"
#     sex = "男"
#     age = 21

#     # 功能：成员方法：类中的方法
#     def talk(self):     # self,是成员方法的第一个参数，Ipython的语法要求
#         print("{}能说话".format(self.name))     # 可以调用内部的成员变量

#     def eat(self,dx):
#         print("大吉大利，今晚吃{}".format(dx))      # 也可以调用外部传进来的参数
#         return "吃鸡了"

#     def test(self):     # 内部的成员方法也可以相互调用
#         self.talk()
#         self.eat("鱼")

# 实例化类:Person()
# p：实例化对象
# p = Person()

# 调用成员变量 
# print(p.name)
# print(p.sex)
# print(p.age) 

# 调用talk方法
# p.talk()

# 调用eat方法
# a = p.eat("什么")
# print(a)

# 调用test方法
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








# 练习
# class Jlyz():
#     name = "那个人"
#     age = 18
#     classNme = "3班"

#     def hh(self):
#         print("{}是一个好人".format(self.name))
    
#     def sz(self,ss):
#         print("{}是一个{}".format(self.name,ss))
#         return ("恭喜恭喜！")

#     def nn(self):
#         self.hh()
#         self.sz("瓜娃子")
# j = Jlyz()
# print(j.name)
# j.hh()
# a = j.sz("傻子")
# print(a)
# j.nn()





# class wz():
#     yx = "蒙恬"
#     jn = "蒙家军"
#     dz = "秦国"

#     def mm(self,xm):
#         print("{}的妹妹是{}".format(self.yx,xm))
#         return "登高"

# m = wz()
# e = m.mm("蒙娇娇")
# print(e)



class whh():
    q = "致盲"
    w = "移动加速"
    e = "被动技能"
    r = "蘑菇"
    def mw(self):
        print("{}攻击无效".format(self.q))

kll = whh()
kll.mw()