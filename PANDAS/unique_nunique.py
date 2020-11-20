import pandas as pd

df = pd.read_csv('data_sf.xls')

small_df = df[df.columns[0:7]].head(25)
print(small_df)

#Функции unique и nunique и преобразование серии value_counts в датафрейм
s = small_df['Nationality'].value_counts()
print(s.index)
print(len(s.index))

print(small_df['Nationality'].unique())
print(len(small_df['Nationality'].unique()))

print(small_df['Nationality'].nunique()) #количество уникальных значений в серии, то мы можем поступить ещё проще

#Преобразование серии value_counts в датафрейм

s = small_df['Nationality'].value_counts()
s_df = s.reset_index()
print(s_df)
s_df.columns = ['Nationality','Players Count']
print(s_df)