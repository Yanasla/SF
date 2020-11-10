#f = open('StudentsPerformance.csv') 
#for line in f:
         #print(line)
#f.close()
f = open('StudentsPerformance.csv')
'''males = 0
females = 0
for line in f:
    info = line.split(',')
    gender = info[0][1:-1]
    if gender == 'female':
        females += 1
    elif gender == 'male':
        males +=1
print('Мальчиков: {}, девочек: {}'.format(males, females))'''

'''res_list = []
for line in f:
    info = line.split(',')
    pe = info[2][1:-1]
    if pe not in res_list: 
        res_list.append(pe)
print("Unique elements of the list using append():n")    
for item in res_list: 
    print(item)
print(len(res_list)-1)'''

'''LS = 0
S = 0
for line in f:
    info = line.split(',')
    lunch = info[3][1:-1]
    if lunch == 'standard':
        LS += 1
    elif lunch == 'free/reduced':
        S += 1

print('Полноценный обед получили: {}'.format(LS))
print(LS/(LS + S))'''

'''c = 0
for line in f:
    info = line.split(',')
    ethno = info[1][1:-1]
    if ethno == 'group C':
        c += 1
print('Этническая группа С": {}'.format(c))
print(c)'''

res_list = []
for line in f:
    info = line.split(',')
    eg = info[1][1:-1]
    if eg not in res_list: 
        res_list.append(eg)
print("Unique elements of the list using append():n")    
for item in res_list: 
    print(item)
print(len(res_list)-1)