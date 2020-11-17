#Определите функцию count_letters(sentence, average), которая считает количество букв в строке без учёта пробелов. 
# У функции должен быть необязательный булевый аргумент average, который по умолчанию равен False. 
# Если он равен True, то функция должна возвращать количество букв в среднем на слово.
#Словом считается любая последовательность символов, отделённая пробелами или границами предложения. Cреднюю длину слова можно не округлять



def count_letters(sentence, average = False):
    lenth = 0
    for с in sentence:
        if average == True:
            c_count = 1
            if с != ' ':
                c_count += 1
                lenth1 += 1
                lenth = lenth1/c_count
        elif с != ' ':
            lenth += 1
    return lenth



print(count_letters("Beep boop")) # => 8
print(count_letters("Beep boop", average=True)) # => 4
print(count_letters("I will build my own theme park")) # => 24
print(count_letters("I will build my own theme park", average=True)) # => 3.429