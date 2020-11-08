rainbow_list = 'каждый охотник желает знать где сидит фазан'.split()
for word in rainbow_list:
    print(word)
rainbow_dict = {'каждый': 'красный', 
                'охотник': 'оранжевый', 
                'желает': 'жёлтый', 
                'знать': 'зелёный', 
                'где': 'голубой', 
                'сидит': 'синий', 
                'фазан': 'фиолетовый'}

# Перебираем ключи
for word in rainbow_dict.keys():
    print(word)

# Перебираем значения
for color in rainbow_dict.values():
    print(color)

# Перебираем пары ключ-значение
for word, color in rainbow_dict.items():
    print(word, color)

string = 'Вы - самый крутой студент в SkillFactory'
for letter in string:
    print(letter)
    

proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
#Используя срез, напишите код, с помощью которого можно извлечь из строки proverb слово "Программист".
print(proverb[:11])
print(proverb[-13:-9])


new_proverb = list(proverb)
for i in range(len(new_proverb)-1):
    if i % 2 ==0:
        nch = new_proverb[i]
        ch = new_proverb[i+1]
        new_proverb[i] = ch
        new_proverb[i+1] = nch
print(''.join(new_proverb))

basic_word = 'мадам'
basic_word = 'программирование'
inverted_word = basic_word[::-1]
if basic_word == inverted_word:
  print('Слово','"',basic_word,'"','является палиндромом')
else:
  print('Слово','"',basic_word,'"','- это не палиндром')