spisok = ['лебедь','рак','щука']
print('рак' in spisok)
a = spisok.pop(2) #извлечение элемента из списка
print(a)
print(spisok)
stroka = 'Basic;<fdf>;PHP;<ggh>;Python;<sdfsdf>;Java;<ooljsf>;C++'
print(stroka.split(';')[::2])



mixed = ['греча', 'банан', 'фасоль', 'рис', 'апельсин', 'банан']
for index, value in enumerate(mixed):
    if value == 'банан':
        print(index)
        
mixed = ['греча', 'банан', 'фасоль', 'рис', 'апельсин', 'банан']

b = list(enumerate(mixed))
n = list(enumerate(mixed))[1][1]
print(b)
print(n)
array_of_arrays = [[1, 2, 3], [4, 5 ,6], [71, 2, 5]]
print(array_of_arrays[-1][-1])


lst = [i for i in range(10)]
print(lst)

sq = [x ** 2 for x in lst]
print(sq)