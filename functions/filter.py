nums = [1, 20, 30, 33, 16, 5]  
  
# оставим числа меньшее 30  
print(list(filter(lambda x: x < 30, nums)))
# => [1, 20, 16, 5]  
  
# оставим только нечётные числа  
print(list(filter(lambda x: x % 2 == 1, nums)))
# => [1, 33, 5] 


#Для заданных чисел values и среднего значения mean напишите такой filter, который оставляет только элементы больше среднего значения.

values = [4, 8, 15, 16, 23, 42]
mean = 18

result = list(filter(lambda x: x > mean, values)) # ваш код здесь
print(result)