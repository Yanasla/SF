# => Определим функцию polite_name, которая делает вежливым одно имя 

def polite_name(name):  
    return 'Mr. ' + name   
  
guests = ["Boris", "Ivan", "Bob"]
guest_iterator = list(map(polite_name, guests))  # здесь мы применили polite_name к каждому имени  

list(guest_iterator)  # вывoд  
# => ['Mr. Boris', 'Mr. Ivan', 'Mr. Bob']  
print(guest_iterator)

num_strings = ["10", "1", "4.2", "0.73"]  
n = list(map(float, num_strings)) 
print(n)
# => [10.0, 1.0, 4.2, 0.73]  

t = list(map(abs, [10,  -1, 42, -73]))[3]
print(t)

#Пусть у нас есть список слов, и мы хотим получить длину каждого слова. 
# Например, из списка ["All", "my", "troubles", "seemed", "so", "far", "away"] мы ожидаем получить список [3, 2, 8, 6, 2, 3, 4]
# Что нам поставить на месте пропуска, чтобы выполнялась эта операция?

word_sizes = list(map(len, ["all", "you", "need", "is", "map"]))
print(word_sizes)