with open('info.txt') as f:
    for line in f:
        name = line.split('\t')[1]
        print(name)

staff = {'молодые':[], 'опытные':[]}
with open('info.txt') as f:
    for line in f:
        info = line.split('\t')
        age = 2019 - int(info[2][-4:])
        if age < 25:
            staff['молодые'].append('{} {}'.format(info[1], info[0]))
        else:
            staff['опытные'].append('{} {}'.format(info[1], info[0]))
            
for experience in staff:
    print(experience.upper())
    for person in staff[experience]:
        print(person)
    print()

import re
new_staff = {'Россия':0,'Казахстан':0,'Дальнее зарубежье':0}
pattern = re.compile('\+\d+ \(\d')
with open('info.txt') as f:
    for line in f:
        tel = pattern.findall(line)[0].split()
        if tel[0] == '+7':
            if tel[1] ==  '(7':
                new_staff['Казахстан'] += 1
            else:
                new_staff['Россия'] += 1
        else:
            new_staff['Дальнее зарубежье'] += 1
print(new_staff)
phoneNumRegex = re.compile(r'\d{3}-\d{2}-\d{2}')
mo = phoneNumRegex.search('321-66-13 is a phone number:')
print(mo.group())

phrase = 'Миша кинул Вове мяч, Миша его отбил'
reg = re.compile(r'Вове|Миша')
mo = reg.search(phrase)
print(mo.group())