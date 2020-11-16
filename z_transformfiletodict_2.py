#Сколько мальчиков хорошо пообедали перед экзаменом (lunch = standard)?

students = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        sex = info[0][1:-1]
        lunch = info[3][1:-1]
      
        if sex in students:
            if lunch in students[sex]:
                students[sex][lunch] += 1
            else:
                students[sex][lunch] = 1
        else:
            students[sex] = {}
            students[sex][lunch] = 1
print(students)
print(students['male']['standard'])

#Сколько мальчиков закончили подготовительные курсы (test preparation course = completed)?

students_pre = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        sex = info[0][1:-1]
        tpc = info[4][1:-1]
      
        if sex in students_pre:
            if tpc in students_pre[sex]:
                students_pre[sex][tpc] += 1
            else:
                students_pre[sex][tpc] = 1
        else:
            students_pre[sex] = {}
            students_pre[sex][tpc] = 1
print(students_pre)
print(students_pre['male']['completed'])

#У скольких девочек родители имеют степень магистра (parental level of education = master's degree)?

students_pm = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        sex = info[0][1:-1]
        ple = info[2][1:-10]
      
        if sex in students_pm:
            if ple in students_pm[sex]:
                students_pm[sex][ple] += 1
            else:
                students_pm[sex][ple] = 1
        else:
            students_pm[sex] = {}
            students_pm[sex][ple] = 1
print(students_pm)
print(students_pm['female']['master'])

#Сколько абитуриентов, относящихся к этнической группе С, закончили подготовительные курсы?

students_ec = {}

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        ec = info[1][1:-1]
        pre = info[4][1:-1]
      
        if ec in students_ec:
            if pre in students_ec[ec]:
                students_ec[ec][pre] += 1
            else:
                students_ec[ec][pre] = 1
        else:
            students_ec[ec] = {}
            students_ec[ec][pre] = 1
print(students_ec)
print(students_ec['group C']['completed'])

