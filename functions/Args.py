
#Теперь немного практики для закрепления. Определите функцию sum_args, которая суммирует все свои аргументы. 
# Например, sum_args(10, 15, -4) должна возвращать 21 

def sum_args(*args):  
    summ = 0  
    for element in args:  
        summ += element  #summ = summ + element
        return summ   

print(sum_args(10, 15, -4))

#Переменное число аргументов

def multiply(*args):  
    product = 1  
    for num in args:  
        product *= num  #product = product * num
        return product   
  
print(multiply(2))  
# => 2  
print(multiply(8, 3, 4))  
# => 96  
print(multiply(1, 2, 3, 4, 5, 6))  
# => 720 
