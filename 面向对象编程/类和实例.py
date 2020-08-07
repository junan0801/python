class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = student('jun', 99)
print(bart.score)


def print_score(std):
    print('%s:%s' % (std.name, std.score))


print_score(bart)

class student(object):
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = student('lisa', 99)
test = student('bart', 69)
bart = student('bart', 59)
print('==================')
print(lisa.name, lisa.get_grade())
print(test.name, test.get_grade())
print(bart.name, bart.get_grade())
