# 求平方函数
def power(x):
    return x * x


for i in (range(5)):
    print(power(i))


# 求n 次方函数
# power 1 必须输入x,n 两个参数，否则会出现 TypeError: power1() missing 1 required positional argument: 'n'
def power1(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


# power 2 设置默认 n = 2,所以只输入x 时，n 取默认值2，该函数就不会出现错误
def power2(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


print('power1:', power1(3, 2))
print('power2:', power2(3))
"""
而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。

从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
如果默认参数放在前面会导致python 无法区分输入的参数是默认参数还是必选参数

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度
"""


def enroll(name, gender, age = 6, city ='Beijing'):
    print('name:', name,  'gender:', gender)


print(enroll('jun', 'M'))


def add_end(s=[]):
    s.append('END')
    return s


print(add_end([1, 2, 3]))
print(add_end([1, 4, 6]))
a = add_end()
print('第一次使用函数的默认值:', a)
b = add_end()
print('第二次使用函数的默认值:', b)

"""
默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

原因解释如下：
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，
不再是函数定义时的[]了。
第一次调用函数时默认值 s =[] 第二次调用函数时默认值  s=[END]
"""


# 通过设置默认s = None,每次取默认值时候会将s 清空，避免函数中的s被改变
def add_end1(s1=None):
    if s1 is None:
        s1 = []
    s1.append('END')
    return s1


print('add_end1')
print(add_end1([1, 2, 3]))
print(add_end1([1, 4, 6]))
a = add_end1()
print('第一次使用函数的默认值:', a)
b = add_end1()
print('第二次使用函数的默认值:', b)


