#f = open('StudentsPerformance.csv') 
#for line in f:
         #print(line)
#f.close()
f = open('StudentsPerformance.csv')
males = 0
females = 0
for line in f:
    info = line.split(',')
    gender = info[0][1:-1]
    if gender == 'female':
        females += 1
    elif gender == 'male':
        males +=1
print('Мальчиков: {}, девочек: {}'.format(males, females))

