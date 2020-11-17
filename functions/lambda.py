# создадим простую функцию с помощью lambda и положим её в переменную func
func = lambda x, y: x + y  
  
# после этого мы можем использовать func как обычную функцию  
print(func(1, 2))
# => 3  
print(func('a', 'b'))  
# => 'ab'  
  
# мы даже можем не давать функции имя, а сразу вызывать  
a = (lambda x: x**2)(8)  
# => 64  
print(a)


#Lambda + map
# исходная версия была такой  
def polite_name(name):  
    return 'Mr. ' + name   
  
guests = ["Boris", "Ivan", "Bob"]  
guest_iterator = map(polite_name, guests)   
  
# Теперь перепишем с лямбда функцией  
guests = ["Boris", "Ivan", "Bob"]  
list(map(lambda name: "Mr. " + name, guests))  


