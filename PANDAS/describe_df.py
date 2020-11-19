import pandas as pd

football = pd.read_csv('data_sf.xls')
print(football.describe())

print(football.describe(include = ['object']))

#fullinfo

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(football.describe()) 