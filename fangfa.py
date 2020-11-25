"""
    为了代码的复用
"""

# def   固定的
# sum： 方法名
# y，q  在调用方法的时候要传递的参数
# return：  返回值
def sum(y,q):
    he = y + q
    return he

a = 1 
b = 2
c = 3

#  s1 = a + b     # + 运算符
#  s2 = a + c
s1 = sum(a,b)
s2 = sum(a,c)
print(s1)
print(s2)