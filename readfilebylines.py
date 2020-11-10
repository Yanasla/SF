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

LS = 0
for line in f:
    info = line.split(',')
    lunch = info[3][1:-1]
    if lunch == 'standart':
        LS += 1
    
print('Полноценный обед получили: {}.format(LS)')

