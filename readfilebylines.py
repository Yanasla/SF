f = open('StudentsPerformance.csv')
#males = 0
#females = 0
c_ple = 0
#for line in f:
    #info = line.split(',')
    #gender = info[0][1:-1]
    #if gender == 'female':
        #females += 1
    #elif gender == 'male':
        #males +=1
#print('Мальчиков: {}, девочек: {}'.format(males, females))
for line in f:
    info = line.split(',')
    ple = info[2][1:-1]
    if ple == "bachelor's degree":
        c_ple += 1
print('У {} абитуриентов родители имеют диплом бакалавра'.format(c_ple))

