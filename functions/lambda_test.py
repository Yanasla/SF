values1 = [1, 2, 3]
vectors = [(10, 3), (4, 5), (6, 7)]

map(lambda x: x+2, [1, 2, 3])
#map(values1, lambda x: x**0.5)
map(lambda vec: (vec[0]**2 + vec[1]**2)**0.5, vectors)
map(lambda x, y: x + y, values1)


#При анализе данных бывает полезно «подвинуть» числа так, чтобы среднее значение было нулевым: так удобнее анализировать их распределение.
#Напишите выражение c map, которое из каждого элемента values вычитает среднее значение mean. Результирующий список положите в переменную result.

values = [4, 8, 15, 16, 23, 42]
mean = 18

result = list(map(lambda x: x- mean, values)) # ваш код здесь

print(result)