import pandas as pd

df = pd.read_csv('data_sf.xls')

small_df = df[df.columns[0:7]].head(25)
print(small_df)

#Функция value_counts возвращает серию. 
s = small_df['Nationality'].value_counts() 

print(s)
print(s.index)

#Обратите внимание, что в индексе названия сборных идут так же, как в серии, то есть по убыванию числа футболистов. 
# Значит, вызвав первый элемент индекса, мы получим название сборной, у которой больше всего футболистов в рамках нашего небольшого датафрейма:
print(s[0])
print(max(s))
#количество национальностей, которые встречаются в датафрейме small_df
print(len(s.index))
#обратиться по нужному индексу к элементу серии:
print(s['Germany'])
#такие сборные, в которых больше 1 футболиста:
print(s.loc[s > 1])
#Можно посчитать количество футболистов не в абсолютных числах, а в процентах от общего числа в датасете
s = small_df['Nationality'].value_counts(normalize=True)
print(s)

#датасет футбольных клубов
s1 = df['Club'].value_counts() 
print(s1)
#Сколько футбольных клубов представлено в датасете?
print(len(s1.index))

#Данные об игроках каких позиций (Position) занимают более 10% датасета?
s2 = df['Position'].value_counts(normalize=True) 
print(s2)

#Подсчет количества значений по численным признакам
s3 = small_df['Age'].value_counts()
print(s3)
s4 = small_df['Wage'].value_counts()
print(s4)
s5 = small_df['Wage'].value_counts(bins=4)
print(s5)
s6 = small_df.loc[(small_df['Wage'] > s5.index[3].left) & (small_df['Wage'] <= s5.index[3].right)]
print(s6)
print(s5.index[3].left)

#В каких пределах находятся худшие 20% показателей точности ударов ногой (FKAccuracy)?
s7 = df['FKAccuracy'].value_counts(bins=5)
print(s7)

#Функции unique и nunique и преобразование серии value_counts в датафрейм

