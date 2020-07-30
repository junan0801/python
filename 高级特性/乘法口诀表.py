for x in range(1, 10):
    for y in range(1, 10):
        if x >= y:
            print(x, '*', y, '=', x * y, end='\t')
    print()


print('*' * 110)


for x in range(1, 10):
    for y in range(1, 10):
        if x >= y:
            print('{} * {} = {}'.format(x, y, x * y), end='\t')
    print()


print('*' * 110)


for x in range(1, 10):
    for y in range(1, 10):
        if x >= y:
            print('{0} * {2} = {1}'.format(x, x * y, y), end='\t')
    print()
