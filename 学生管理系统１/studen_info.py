def add_student_message():
    l = []  #创建一个新的列表，用此列表准备保存学生信息。
    #录入学生信息。
    while True:
        d = {}
        name = input('请输入姓名：')
        if name == '': 
            break 
        age = input('请输入年龄：')
        score = input('请输入成绩：')
        #创建一个新的字典，把学生的信息存入字典中。 
        d['name'] = name
        d['age'] = age
        d['score'] = score
        l.append(d)  #把录入学生信息以字典为元素依次添加到列表。
    return l  #返回学生录入信息列表。


def show_student_message(l):    
    print('+---------------+----------+----------+')
    print('|     name      |   age    |   score  |')      
    print('+---------------+----------+----------+') #打印表头。　
    for dic in l:
        n = get_chinese_char_count(dic)
        print('|%s|%s|%s|' % (dic['name'].center(15 - n),
                          dic['age'].center(10),
                          dic['score'].center(10))) #按输入顺序打印学生信息。
        print('+---------------+----------+----------+') #分隔不同学生信息。
    
def del_student_message(l):
    while True:
        name = input('请输入您需要删除的信息的学生姓名：')
        if name == '':
            break
        for n in l:
            if n['name'] == name:
                l.remove(n)
    return l

def get_chinese_char_count(dic):    
    count = 0 #记中文个数  
    for char in dic['name']:
        if ord(char) > 127:
            count += 1
    return count

def revise_student_message(l):
    while True:
        oldname = input('请输入您想修改信息学生的姓名：')
        if oldname == '':
            break
        newname = input('请输入更改后学生姓名：')
        newage = input('请输入更改后学生年龄：')
        newscore = input('请输入更改后学生成绩：')
        for n in l:
            if n['name'] == oldname:
                n['name'] = newname
                n['age'] = newage
                n['score'] = newscore
    return l

def age_sorted_rule(*l):
    for a in l:
        return a.get('age')

def score_sorted_rule(*l):
    for a in l:
        return a.get('score')

def score_high_low(l):
    lis = sorted(l.copy(),key=score_sorted_rule,reverse=True)
    show_student_message(lis)

def score_low_high(l):
    lis = sorted(l.copy(),key=score_sorted_rule)
    show_student_message(lis)

def age_high_low(l):
    lis = sorted(l.copy(),key=age_sorted_rule,reverse=True)
    show_student_message(lis)

def age_low_high(l):
    lis = sorted(l.copy(),key=age_sorted_rule)
    show_student_message(lis)

def save_data(l):
    try:
        f = open('si.txt','a')
        for a in l:
            f.writelines([a['name'],',',a['age'],',',a['score']])
            f.write('\n')
        f.close()
    except OSError:
        print('存储失败')    

def read_message():
    l = []
    try:
        f = open('si.txt','r')
        for line in f:
            n, a, s = line.strip().split(',')     
            l.append({'name': n,'age': a, 'score': s })      

        f.close()
    except OSError:
        print("读取文件失败")

    return l
