print("Price: ", 10)  
# => Price: 10  
  
print("Soft", "sweat", 10, 12, sep=", ")  
# => Soft, sweat, 10, 12  

#Для этого при определении функции для такого аргумента указывается значение по умолчанию.

def hello(name="Alice"):  
    print("Hello,", name)  
  
print(hello())  
# => Hello, Alice  
  
print(hello("Bob"))  
# => Hello, Bob  
  
print(hello(name='Bob'))  
# => Hello, Bob  

#Вы можете использовать в одной функции и обязательные, и необязательные аргументы, но тогда первыми должны идти обязательные аргументы.

# Так хорошо  
def say_something(word, times=5):  
    print(word*times)  
      
# А так не сработает  
#def say_hello(word='hello', times):  
    #print(word*times)  

def resize_image(image, target_size=(128, 128), channels=3, channel_order='rgb', anti_aliasing=True):  
    resized_image = image # мы как-то реализуем изменение размера, сейчас не важны детали   
    return resized_image  
    