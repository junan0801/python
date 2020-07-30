#f = open(r'C:\Users\mx-0123\Desktop\zican.txt', 'r')
#line = f.readline()
#while line:
#    print(line)
#    print('=====')
#    fw = open(r'C:\Users\mx-0123\Desktop\sn.txt', 'a')
#    fw.write(line)
#    fw.close()
#    line = f.readline()
#f.close()
ms =open(r'C:\Users\mx-0123\Desktop\zican.txt', 'r')
for line in ms.readlines():
    with open(r'C:\Users\mx-0123\Desktop\sn.txt', 'a') as mon:
        mon.write(line)