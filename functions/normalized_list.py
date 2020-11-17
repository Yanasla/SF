#Если вы обратили внимание, в предыдущих частях модуля у вас было несколько заданий с функцией normalize. 
# Нормализацию часто применяют в машинном обучении, приводят данные к виду, когда среднее значение равно 0, а стандартное отклонение — 1.
#Определите функцию normalize с тремя аргументами:
#numbers — список чисел;
#mean — число, необязательный аргумент, по умолчанию 0;
#std — число, необязательный аргумент, по умолчанию 1.
#Функция должна для каждого числа из numbers вычитать mean и полученный результат делить на std. На выходе ожидается список из этих новых чисел.
#normalize([10, 20])
#=> [10, 20]
#normalize([10, 20], std=2)
#=> [5, 10]
#normalize([10, 20], mean=15)
#=> [-5, 5]


def normalize(numbers, mean = 0, std = 1):
    new_numbers = []
    for element in numbers:
        result = (element - mean)/std
        new_numbers.append(result)
    return new_numbers

print(normalize([10, 20]))

print(normalize([10, 20], std=2))

print(normalize([10, 20], mean=15))