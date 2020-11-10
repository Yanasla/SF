proverb = 'Хорошо написанная программа - это программа, написанная 2 раза'
while True:
    index = proverb.find('программа')
    print(index)
    if index == -1:
        break
    secret = proverb[:index].split()[-1]
    proverb = proverb[index+9:] 
print(secret)
print(proverb)

email = 'VeryBigBoss@skillfactory.ru'
pos = email.find('@')
domain = email[pos+1:]

string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
secret = string[24:30]
new_string = string.replace(secret.lower(), secret.upper()) 
print(new_string)
food = str(input())
if food.lower() == 'овсянка': print('Да Вы гурман!')
string = 'properties'
string.replace(string[0], string[0].upper())
print(string)
string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
s_lst='.,:-!?'
marks=':)'
for letter in string:
    if letter in s_lst:
        string=string.replace(letter,marks)
print(string)