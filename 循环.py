classmate = ['liming', 'tom', 'lilei']
for i in classmate:
    print(i)

sum1 = 0
for i in range(101):
    sum1 = sum1 + i
    print(sum1)
print('*****************')
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
    print(sum2)

print('*********')
L = ['Bart', 'Lisa', 'Adam']
for i in list(range(3)):
    print('Hello,', L[i])
print('*****len(L)*****')
L = ['Bart', 'Lisa', 'Adam']
n = 0
while n < len(L):
    print('Hello,', L[n])
    n =n + 1
print('**********')
# while
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
print('****break****')
# break 的作用是提前结束循环。
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
print('****continue****')
# continue 跳过当前的这次循环，直接开始下一次循环
n = 1
while n <= 100:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)
print('END')

"""
小结
循环是让计算机做重复任务的有效的方法。

break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句
"""



