import re

with open('info.txt', encoding = 'ansi') as f:
    for line in f: 
        print(line, end = '')
#new_staff = {'Россия':0, 'Казахстан':0, 'Дальнее зарубежье':0}
#pattern = re.compile('\+\d+ \(\d')

phone = re.compile(r'\d{3}-\d{2}-\d{2}')
mo = phone.search('321-75-68 is a phone number:')
print(mo.group())


text = '''Разработка языка Python была начата в конце 1980-х годов сотрудником голландского института CWI Гвидо ван Россумом. 
Для распределённой ОС Amoeba требовался расширяемый скриптовый язык, и Гвидо начал писать Python на досуге, позаимствовав некоторые 
наработки для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). 
В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. Название языка произошло вовсе не от вида пресмыкающихся. 
Автор назвал язык в честь популярного британского комедийного телешоу 1970-х "Летающий цирк Монти Пайтона".'''

pattern1 = re.compile(r'\d+')       #все цифры от 1 и более 
pattern2 = re.compile(r'[A-Za-z]+') #все слова на английском
pattern3 = re.compile(r'[А-Яа-я]+ка') #все слова, содержащие "ка" в любой части, кроме начала слова
pattern4 = re.compile(r'а[А-Яа-я]{2}и+')
pattern5 = re.compile(r'[ауоыиэяюе]')
result1 = pattern1.findall(text)
result2 = pattern2.findall(text)
result3 = pattern3.findall(text)
result4 = pattern4.findall(text)
print(result1, result2, result3, result4)

