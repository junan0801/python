# '''  ''' """ """都可以表示多行注释(如果注释里含有''必须用""表示多行注释)
# 注释中无''，用单引号双引号均可
"""
如果字符串内部有很多换行，用\n写在一行里不好阅读，
为了简化，Python允许用的格式表示多行内容
"""
# 注释中含有''，只能用双引号
"""
如果字符串内部有很多换行，用\n写在一行里不好阅读，
为了简化，Python允许用'''...'''的格式表示多行内容
"""
print('\\\t\\')
# r''表示引号引用的内容不被转义
print(r'\\\t\\')
# print 中使用''''''表示多行内容，如果内容中出现了不能被转义的字符，在前面加r表示不被转义
print('''Hello,\n 
world''')
print(r'''Hello,\n 
world''')
# 布尔运算
# and运算是与运算，只有所有都为True，and运算结果才是True
print('''布尔运算
and运算是与运算，只有所有都为True，and运算结果才是True''')
print('**************************')
print('True and False=', True and False)
print('True and True=', True and True)
print('False and True=', False and True)
print('False and False=', False and False)
print('**************************')
# or运算是或运算，只要其中有一个为True，or运算结果就是True
print('or运算是或运算，只要其中有一个为True，or运算结果就是True')
print('**************************')
print('True or False=', True or False)
print('True or True=', True or True)
print('False or True=', False or True)
print('False or False=', False or False)
print('**************************')
# not运算是非运算，它是一个单目运算符
print('not运算是非运算，它是一个单目运算符')
print('**************************')
print('not True =', not True)
print('not False=', not False)
print('**************************')
'''
空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到
'''
print('''空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
此外，Python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，我们后面会继续讲到''')
a = 123
print(a)
a = 'abcd'
print(a)
# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向
print('对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向')
a = 'ABC'
b = a
a = 'XYZ'
print(b)
# 练习题
"""
请打印出以下变量的值：
# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
"""

print('方法一')
print('n = \'123\'', '\n'  'f = \'456.789\'', '\n' 's1 = Hello,World', '\n' 's2 =', r'Hello,\'Adam \'',

                                                                                    """
s3 = r'Hello,"Bart"'
s4 = r'''Hello,
Lisa!'''
""")
print('方法二')
print('n =  \'123\'', '\n' 'f = \'456.789\'', '\n' 's1 = Hello,World', '\n'"s2 = r\'Hello,\\'Admin\\'\'",
      "s3 = r\'Hello\"Bart\"\'" '\n' "s4 = r\'\'\'Hello,\nLisa! \'\'\'")
