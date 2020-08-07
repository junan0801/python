class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


bart = student('jun', 99)
print(bart.score)