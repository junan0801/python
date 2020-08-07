from collections.abc import Iterable
d = {'a': 1, 'b': 2, 'c':3}

for key in d:
    print(key)
# 使用d.values 方法迭代出key
print('===========使用d.values 方法迭代出key')
for value in d.values():
    print(value)
# 使用items 方法迭代出key value
print('===========使用d.items 方法迭代出key value')
for ke, va in d.items():
    print(ke, va)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print('x=', x, 'y=', y)


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = max = L[0]
    for i in L:
        if i > max:
            max = i
        elif i < min:
            min = i
    return(min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
if findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')