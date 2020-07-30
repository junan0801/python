n = ord ('中')
print('ord(中)', n)
n1 = chr(20013)
print ('chr(20013)', n1)

print('%s 成绩提高了%.1f%%' % ('xiaoming', 18.76))
print('{} 成绩提高了{:.1f}%'.format('xiaoming', 18.76))
print('亲爱的 %s 你好:你的%s月话费为%.2f元' % ('xiaoming', 6, 39))
print('%2d-%02d' % (3, 1))
print('%.2f'%3.1415926)
s1 = 72
s2 = 85
s = (s2-s1)/s2 * 100
print('(85-72)/85*100=', s)
print('小明成绩提高了%.1f%%'% s)
print('小明成绩提高了{:.1f}%'.format(s))
