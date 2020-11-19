import pandas as pd

data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
                 index = ['Первый', "Второй", "Третий", "Четвёртый"])


print(data)
print(data.loc["Первый"])

print(data.loc[["Первый", "Третий"]])

data = pd.Series(list(range(10, 1001)))
print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])
print(data)