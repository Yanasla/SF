#У какого процента испанских футболистов (Nationality = 'Spain') зарплата (Wage) находится в пределах 25% минимума 
# от наблюдаемого уровня зарплат среди испанских игроков? Ответ дайте в виде целого числа (округлите полученный результат) без знака %.
#Подсказка: Для решения задачи используйте value_counts() с параметром bins = 4.

import pandas as pd

df = pd.read_csv('data_sf.xls')

s_spain = df[df.Nationality == 'Spain']
print(s_spain)
s_ws = s_spain['Wage'].value_counts(bins=4,normalize=True)
print(s_ws)

#Укажите количество уникальных сборных (Nationality), к которым относятся футболисты, выступающие за клуб (Club) "Manchester United".

s_MU = df[df.Club == 'Manchester United']
print(s_MU)
print(s_MU['Nationality'].nunique()) #количество уникальных значений в серии сборных (Nationality), к которым относятся футболисты, выступающие за клуб (Club) "Manchester United"

#С помощью функции unique определите двух футболистов из Бразилии (Nationality = 'Brazil'), 
# выступающих за клуб (Club) 'Juventus'. Перечислите их имена (Name, как в датафрейме) через запятую в алфавитном порядке.

s_Uv = df[(df.Club == 'Juventus')&(df.Nationality == 'Brazil')]
print(s_Uv)

#Укажите, какой из клубов (Club) насчитывает большее количество футболистов возрастом (Age) старше 35 лет.

s_35 = df[df.Age >35]
print(s_35)
s_club35 = s_35['Club'].value_counts()
print(s_club35)

#С помощью функции value_counts с параметром bins разбейте всех футболистов родом из Аргентины (Nationality = 'Argentina') 
#на 4 равные группы по возрасту. Сколько футболистов в возрасте от 34,75 до 41 года в сборной Аргентины?

s_Ar = df[df.Nationality == 'Argentina']
print(s_Ar)
n = s_Ar['Age'].value_counts(bins=4)
print(n)

#Сколько процентов футболистов из Испании (Nationality = 'Spain') имеют возраст (Age) 21 год? Введите с точностью до 2 знаков после запятой без указания знака % (например, 12.35).
s_SP = df[df.Nationality == 'Spain']
print(s_SP)
s_SP21 = s_SP['Age'].value_counts(normalize=True)
print(s_SP21)