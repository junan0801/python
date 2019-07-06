def findMinAndMax(nu):
    if len(nu) == 0:
        print(None, None)
        return None, None
    else:
        m = n = nu[0]
        for x in nu:
            if x > m:
                m = x
            elif x < n:
                n = x
        print(n, m)
        return n, m


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, -10, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
