# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d.pop('Michael')
print(d)
"""
dict内部存放的顺序和key放入的顺序是没有关系的。
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
"""
s = set([1, 2, 3])
print(s)
s1 = set([1, 2, 2, 3, 4])
print(s1)
s1.add(5)
print(s1)
print('s1 &s=', s1 & s)
s1.remove(5)
print(s1)
# dict
d = (1, 2, 3)
print(d)
d1 = (1, [2, 3])
print(d1)
# set
s = set([1, 2, 3])
print(s)
