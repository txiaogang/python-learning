# print('hello world')

# name = input('please input your name:')

# print(name)


a1 = 0.1

a2 = 0.2

print(a1 + a2)

a3 = 1.23e10

print(a3)

a4  = "I'm xiaogang"

print(a4)

a5 = 'I\' xiaogang'

print(a5)

print('\\\\t\\')

print(r'\\\t\\')

# 换行
print('line1\nlin22')

print('''
	line1
	line2
	'''
	)

# 布尔值
# 
print(True,False)

a1 = True

a2 =isinstance(a1, bool)

# print(a2）

print(a1, 'a2')

# 逻辑运算

a1 = True

a2 = False

a3 = a1 and a2

a4  = a1 or a2

a5 = not a1

print('逻辑运算',a1, a2, a3, a4, a5)
# 逻辑运算 True False False True False


# None 特殊的值，特殊的空值

a1 = None

print(a1)
#None


# 变量
a =  'abc'

b = a

a = '123'


print(a, b)

# 常量

print(10 / 3)

print(10 // 3)
#3.3333333333333335
#3


# 编码

'''
ASCII 1 个字节  =编码不够=> Unicode 通常两个字节 =不浪费=>utf-8 1-6个字节 （常用英文字母1个字节、汉字3个字节、生僻字4-6个字节）

计算机内存统一用Unicode 码 需要保存或传输的时候转成utf-8

python 字符串是Unicode

'''

a = '中'

print(ord(a))


b = ord(a)

c = chr(b)

print(a,b,c)
#中 20013 中

a = b'ABC'

b = 'ABC'

print(a, b)

# 编码

print('ASC'.encode('ascii'))

print('中文'.encode('utf-8'))

# 解码

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# with error 
print(b'\xe4\xb8\xad\xe46\x96\x87'.decode('utf-8',errors='ignore'))


print(len('ABC'),len(b'ABC'))
# 3 3
print(len('中国'),len('中国'.encode('utf-8')))
# 2 6


#!/usr/bin/python

# coding: utf-8

print('Hi %s ,I\'m %s,I\'m %d year old'%('xiaogang','xiaotang',19))

# 保留一位数字
print('Hello,{0},成绩提成了{1:.1f}%'.format('xiaotang',19.555))






