class Student:
    def __init__(self,name,age,score=0):
        self.name = name
        self.age = age
        self.score = score
    def set_score(self,score):
        del self.score
        self.score = score
    def show_info(self):
        print('姓名:',self.name,'年龄：',self.age,'成绩：',self.score)

l = []
while True:
    name = input('请输入学生姓名：')
    if name == '':
        break
    age = input('请输入学生年龄：')
    score = input('请输入学生成绩：')
    l.append(Student(name,age,score))
for abj in l:
    abj.show_info()