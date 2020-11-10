employee_base = {
'Мария Никитина': 'менеджер',
'Егор Савичев': 'разработчик', 
'Александр Пахомов': 'дизайнер',
'Алина Егорова': 'разработчик', 
'Руслан Башаров': 'верстальщик'
}
for position in employee_base.values(): #перебор значений словаря
    print(position)

for employee in employee_base: #перебор ключей словаря
    print(employee)

for employee in employee_base.keys(): #перебор ключей словаря методом keys
    print(employee)

for employee in employee_base: #вывод ключа и значения
    print(employee, employee_base[employee])

for employee in employee_base: #фильтр по ключу
    if employee_base[employee] == 'разработчик':
        print(employee)

for position in employee_base.values(): #перебор значений словаря методом value
    print(position)

# заводим переменную-счетчик

count = 0
for position in employee_base.values():
    if position == 'разработчик':
        # увеличиваем счетчик на 1
        count+=1
print(count)
# выводим значение счетчика на экран

for employee, position in employee_base.items(): #items
    #универсальным способом является перебор ключей и значений одновременно
    print(employee, position)

for employee, position in employee_base.items(): #фильтр с items
    if position == 'разработчик':
        print(employee)

