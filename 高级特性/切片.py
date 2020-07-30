def trim(str1):
    if str1[0:1] == ' ':
        str1 = str1[1:]
        return trim(str1)
    elif str1[-1:] == ' ':
        str1 = str1[:-1]
        return trim(str1)
    else:
        return str1


print(trim('jun an   '))
