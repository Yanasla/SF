# Определим функцию, которая печатает "привет"  
def say_hello():  
    print("Hello")  
  
# Мы можем положить её в другую переменную  
greetings = say_hello  
  
# И она сработает так же, как исходная say_hello  
greetings()  
# => Hello  

def apply_the_operation(operation, argument):  
    print("I'm using", operation)  
    return operation(argument)  
  
  
def double_string(string):  
    return string*2  
  
# передаём функцию double_string в apply_the_operation  
apply_the_operation(double_string, 'hello')  
# => I'm using <function double_string at 0x7f4c34265378>  
# 'hellohello' 

 
all_the = sum
magic = range
print(all_the(magic(5)))