import pandas as pd

fb = pd.read_csv('data_sf.xls')
print(fb.Age.mean())
print(fb.Composure.count())
print(fb.ShortPassing.std())
print(fb.Wage.sum())
print(fb.Value.min())
print(fb[fb.Age > 20])
print(fb[fb.Age > fb.Age.mean()])
print(fb[(fb.Age < fb.Age.mean())&
        (fb.Club == 'FC Barcelona')].Wage.mean()) #средняя годовая заработную плату футболистов из клуба FC Barcelona, возраст которых меньше среднего [возраста футболистов всех клубов
print(fb[(fb.Age < fb.Age.mean())|
        (fb.Club == 'FC Barcelona')].Wage.mean())

#Какова средняя скорость (SprintSpeed) футболистов, зарплата (Wage) которых ниже среднего? Ответ округлите до сотых.
print(fb[fb.Wage > fb.Wage.mean()].SprintSpeed.mean())
#Какую позицию (Position) занимает футболист с самой высокой зарплатой (Wage)?
print(fb[fb.Wage == fb.Wage.max()])
#Сколько пенальти (Penalties) забили бразильские (Nationality, Brazil) футболисты за период, данные о котором представлены в датасете?
print(fb[(fb.Nationality == 'Brazil')].Penalties.sum())

#Укажите средний возраст (Age) игроков, у которых точность удара головой (HeadingAccuracy) > 50. Ответ округлите до сотых.
print(fb[(fb.HeadingAccuracy > 50)].Age.mean())

#Укажите возраст (Age) самого молодого игрока, у которого хладнокровие (Composure) и реакция (Reactions) превышают 90% от максимального значения, представленного в датасете.
print(fb[(fb.Composure > 0.9*fb.Composure.max())&
        (fb.Reactions > 0.9*fb.Reactions.max())].Age.min())

#Определите, на сколько средняя реакция (Reactions) самых взрослых игроков (т.е. игроков, чей возраст (Age) равен максимальному) 
# больше средней реакции самых молодых игроков. Ответ округлите до сотых.

#средняя реакция самых молодых игроков
a = fb[fb.Age == fb.Age.max()].Reactions.mean()
b = fb[fb.Age == fb.Age.min()].Reactions.mean()

print(a-b)

#Из какой страны (Nationality) происходит больше всего игроков, чья стоимость (Value) превышает среднее значение?

print(((fb[fb.Value > fb.Value.mean()]).Nationality).describe())

# Определите, во сколько раз средняя зарплата (Wage) голкипера (Position, GK) с максимальным значением показателя 
# "Рефлексы" (GKReflexes) выше средней зарплаты голкипера с максимальным значением показателя "Владение мячом" (GKHandling).

x = fb[(fb.Position == 'GK')&(fb.GKReflexes == fb.GKReflexes.max())].Wage.mean()
y = fb[(fb.Position == 'GK')&(fb.GKHandling == fb.GKHandling.max())].Wage.mean()
print(x/y)

#Определите, во сколько раз средняя сила удара (ShotPower) самых агрессивных игроков 
# (игроков с максимальным значением показателя "Агрессивность" (Aggression)) выше 
# средней силы удара игроков с минимальной агрессией. Ответ округлите до сотых.

x1 = fb[fb.Aggression == fb.Aggression.max()].ShotPower.mean()
y1 = fb[fb.Aggression == fb.Aggression.min()].ShotPower.mean()
print(x1/y1)