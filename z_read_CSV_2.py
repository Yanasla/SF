rus = []
below = 0

f = open('StudentsPerformance.csv')

for line in f:
    info = line.split(',')
    if info[0] == '"gender"':
        continue
    elif info[3] == '"standard"':
        mark = int(info[7][1:-2])
        rus.append(mark)
print(rus)
rus_avg = sum(rus)/(len(rus)) #средний бал по по русскому чтению

for mark in rus:
    if mark > 90:
        below += 1
m = below/68
print(m)
print(len(rus))
print(below) #долю абитуриентов, показавших результат > 90
print(rus_avg)