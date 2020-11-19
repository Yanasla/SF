import pandas as pd

df = pd.read_csv('data_sf.xls')

print(df)

df1 = pd.read_csv('data_sf.xls', sep = ';')