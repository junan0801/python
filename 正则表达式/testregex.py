import re
test = input('请输入需要检测的正则表达式:')
if re.search(r'(\w{7}\@gmail.com) | (\w{9}\@microsoft.com)', test):
    print('ok')
else:
    print('failed')








