#!/usr/bin/python
# _*_ coding: utf-8 _*_

# list 有序的集合 

classmate = ['xiao', 'gang', 'tang']

print(classmate)

print(len(classmate))

classmate.append('ze')

classmate.insert(1,'gan')
print(classmate)

# tuple

# 有序列表 初始化后不能改变

t = () # 空的tuple

a = (1)

# error
print(a)
# 不是tuple

# ok
a = (1,)
print(a)

a = (1, 2, [3, 4])

print(a)

a[2][0] = 'x'
a[2][1] = 'y'

print(a)
#(1, 2, ['x', 'y'])



# dict 相当于其他语言的map

# 通过key 计算 位置 hash 算法

map = {'a' : 1, 'b' : 2, 'c' : 3}

print(map)
# {'a': 1, 'b': 2, 'c': 3}

print('a' in map)
# True


# set 和 dict 类似 。存key ，但是不存value 且 key 无重复 无序 

s = set([1, 2, 3, 3, 2])
print(s)
# {1, 2, 3}


# 总结
'''
	list 和 tuple 是一套  有序 可以重复
	dict 和 set 是一套	key :无序 、无重复 、不可变对象
	
	可变对象： list
	不可变对象： str

'''

a = {(1, 2, 3):1}
b = set((1, 2, 3))

print(a, b)


# a = {(1, [2, 3]):1}

b = set((1, [2, 3]))

print(a, b)


