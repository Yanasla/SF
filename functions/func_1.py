# Это определение функции, которая возводит число в квадрат    
def square(x):    
    return x**2    
    
# Это вызов функции. Мы возведём 5 в квадрат и положим 25 в переменную square_result    
square_result = square(5)    
    
    
# Определение стоимости в магазине всё по 60, где только яблоки стоят 30    
def count_cost(product):    
    if product == "apple":    
        cost = 30    
    else:    
        cost = 60    
    return cost    
    
# Попросим функцию посчитать стоимость апельсина    
orange_cost = count_cost("orange")

# Дополните аргументы и код функции
def sum_2(x, y):
    result = x + y
    return result

# Передайте аргументы 42 и 73 в функцию
print(sum_2(42, 73))


#Напишите функцию power, которая возводит первый аргумент в степень второго аргумента. Например, power(2, 3) должен вернуть 8, а power(4, 2) - 16
 
def power(x, y):
    result = x ** y
    return result

print(power(2,3))
print(power(4,2))


def get_median(lst): 
    n = len(lst)
    if n < 1: 
        return None 
    if n % 2 == 1: 
        return sorted(lst)[n//2] 
    else: 
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0
    
print(get_median([5, 2, 1, 3, 4]))  #3
print(get_median([3, 3, 7, 9]))     #5