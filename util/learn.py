# -*- coding: utf-8 -*-
import math

print("hello")
print("123")
a = [1,23]
print("数组长度：")
print(a.__len__())
print(a[-2])
a.append(2333)
print(a)
print("shan删除元素List")
print(a.pop(2))
print(a)

print("tupleceshi 测试")
t = ()
print(t)
# t[0]="2"
t  = 2

print(t)

#单元数的tuple
t1 = (1,)


print("注意if的缩进")
a = 234
if a > 23 :
    print('a > 23')
print(a)

print("if--- else ---")
a -= 222;
if a > 23 :
    print("hhha")
else:
    print("bububufbufbfubfufb")

print("if ---elif -- else")
age = 61
if age > 60:
    print("你已经老了60了，可以退休了")
elif age > 20:
    print("你是成年了，正值工作年纪")
elif age > 10:
    print("你还小，该好好学习")
else:
    print("小屁孩")
l = [23,4,5,5,]
print("for循环特别的简单：")
for item in l:
    print(item)

print("测试集合：：")
d={
    "key1":'hahha',
    "key2":22
}
print("集合的特点：")
print("1、查找速度特别的快")
print("2、存储的KEY-VALUE对是没有顺序的")
print("3、作为KEY的元素必须不可变，python的基本类型比如字符串，整数、浮点数都是不可变的，都可以作为KEY。但是list是可变的，就不能作为KEY")


b = {
    '123': [1, 2, 3],  # key 是 str，value是list
    123: '123',  # key 是 int，value 是 str
    ('a', '1'): True  # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}

print("遍历dist")

for key in b:
    print("KEY:")
    print(key)
    print("VALUE:")
    print(b[key])

print("python之SET操作：")
s = set(['a','b','c'])
print(s)
print('b' in s)
print('a' in s);print('cd' in s)

print("python 之SET的特点：")
print("1、set的内部结构和dict很像，唯一的区别是不存储VALUE")
print("2、SET存储的元素和dict的KEY类似，必须是不可变的对象")
print("3、SET元素是无序的")

print("编写函数：：：")
def my_abs(x):
    if x >= 0:
        return x;
    else:
        return -x;
#定义一元二次方程的两个解
def abc(a,b,c):
    t = b * b - 4 * a * c;
    if t < 0 :
        print("参数不合法")
        return
    t = math.sqrt(b*b - 4 * a *c);
    return (-b + t)/2/a,(-b-t)/2/a;

v1 = abc(2,3,0);
print(v1)
v1 = abc(2,4,6)
print(v1)


print("Python之默认参数：")
a = int('123')
print(a)
#第二个参数转换进制
#moren
a = int('123',36)
print(a)

def my_power(x,n=2):
    s = 1
    while n > 0:
        n -= 1;
        s = x * s
    return  s

print("函数默认参数：")
print(my_power(2))
print(my_power(2,5))

print("切片————————》》》》")
print("python对于字符串没有截取函数，只能通过对字符串进行切片操作")
print("123456"[4:3])