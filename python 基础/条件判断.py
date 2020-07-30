age = float(input('please input you age'))
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# BMI
height = float(input('please input you height:m'))
weight = int(input('please input you weight:kg'))
# bmi = weight/(height*height)  ** 表示乘方  3 ** 2 表示3 的2 次方

bmi = weight/(height ** 2)
print('your bmi:{:.1f}'.format(bmi))
if bmi > 32:
    print('严重肥胖')
elif 28 < bmi < 32:
    print('肥胖')
elif 25 < bmi < 28:
    print('过重')
elif 18.5 < bmi < 25:
    print('正常')
elif bmi < 18.5:
    print('过轻')


