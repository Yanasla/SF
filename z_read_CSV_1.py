math = []

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    else:
        mark = int(info[5][1:-1])
        math.append(mark)
math_avg = sum(math)/len(math) #средний бал по математике
above_avg = 0
for mark in math:
    if mark > math_avg:
        above_avg += 1
print(above_avg / 1000) #долю абитуриентов, показавших результат выше среднего