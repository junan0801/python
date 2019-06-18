# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 顶级定义之间空两行, 比如函数或者类定义，下面的函数不空行就会提示警告
def jun_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# 顶级定义之间空两行, 比如函数或者类定义，下面的函数空两行警告消失


def jun_abs2(x):
    if x >= 0:
        return x
    else:
        return -x


for i in (1, 3, -1, 0):
    print(jun_abs2(i))

# 如果想定义一个什么事也不做的空函数，可以用pass语句


def nop():
    pass
# 参数检查


def jun_abs3(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print('jun_abs3', jun_abs3(-2))
# 返回多个值





