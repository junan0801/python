"""
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
所以，我们创建了一个generator后，基本上永远不会调用next()，
而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
"""
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for n in g:
    print(n)
