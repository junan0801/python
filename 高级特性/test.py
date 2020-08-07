def findMinAndMax(L):
    if 0 == len(L):
        return ('None1', None)
    else:
        min = L[0]
        max = L[0]
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