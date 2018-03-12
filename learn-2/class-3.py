#!/usr/bin/python
#_*_ coding: utf-8 _*_

age = 3

if age >= 18:
	print('adult')
elif age > 6:
	print('teenager')
else:
	print('child')


# birth = input('your birth is:')

# if int(birth) > 2000:
# 	print('00 后')
# else:
# 	print('00前')


names = ['x', 'y', 'z']

for item in names:
	print(item)


sum  = 0

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9,10]:
	sum+=x

print(sum)

print(list(range(5)))
#	[0, 1, 2, 3, 4]

print(range(5))

sum = 0

for x in range(101):
	sum += x * x + 1


print(sum)


def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x

print(my_abs(10))

print(my_abs(-1))

# print(my_abs('A'))
'''
  File "learn-2/class-3.py", line 61, in <module>
    print(my_abs('A'))
  File "learn-2/class-3.py", line 51, in my_abs
    raise TypeError('bad operand type')
TypeError: bad operand type
'''

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)


print(x, y)
# 151.96152422706632 130.0 返回值是一个tuple


# 小结
'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple


'''

# 函数的参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L = []):
	L.append('end')
	return L

# 可变参数 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

def calc(* numbers):
	sum  = 0 
	for x in numbers:
		sum += x
	print(sum)
calc(1, 2, 3, 4)
# 10

# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)

person('xiaogang', 19)
# name: xiaogang age: 19 other: {}

person('gang', 10, city='beijing', job='coder')
# name: gang age: 10 other: {'city': 'beijing', 'job': 'coder'}


# 命名关键字参数. 限制关键字参数的名字. 
# 明确位置参数 和 关键字参数
def person(name, age, *, city, job):
	print(name, age, city, job)

person('xiaogang', 19, city='beijing', job = 'coder')
#xiaogang 19 beijing coder
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)










