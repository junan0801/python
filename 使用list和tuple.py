classmate = ['liming', 'tom', 'hanmeimei']
print(classmate)
print('classmate长度:', len(classmate))
print('classmate 第%s个元素为:%s\n第%s个元素为:%s\n第%s个元素为:%s'% (1, classmate[0], 2, classmate[1], 3, classmate[2]))
print('classmate 第{}个元素为:{}\n第{}个元素为:{}\n第{}个元素为:{}'.format(1, classmate[0], 2, classmate[1], 3, classmate[2]))
classmate.insert(1, 'jun')
print(classmate)
classmate.pop(1)
print(classmate)
classmate[1] = 'jun'
print(classmate)
s = ['liming', ['jun', 'an'], 'tom', 'hanmeimei']
print(s)
print(s[1][1])
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
t = (1, 2, 3)
# tuple 不支持修改，如果执行t[0] = 0该句，会提示TypeError: 'tuple' object does not support item assignment
print(t[1])

t = ('a', 'b', ['c', 'd'])
t[2][0] = 'C'
t[2][1] = 'D'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
'''
tuple
空的tuple:
'''
a = ()
print(a)
'''
只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
'''
a = (1, )
print(a)
