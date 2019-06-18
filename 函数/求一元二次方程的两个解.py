# 如果 b²-4ac <= 0 ,方程无解
import math


def quadratic(a, b, c):
    if not isinstance(a, (int, )):
        raise TypeError('bad operand type a')
    elif not isinstance(b, (int, )):
        raise TypeError('bad operand type b')
    elif not isinstance(c, (int,)):
        raise TypeError('bad operand type c')
    elif b ** 2 - 4 * a * c <= 0:
        return '无解'
    else:
        x1, x2 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)), \
                 ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        return x1, x2


print(quadratic(2, 25, 7))
