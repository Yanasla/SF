import pandas as pd

football = pd.read_csv('data_sf.xls')
print(football.describe())

print(football.describe(include = ['object']))

#fullinfo

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(football.describe()) 

df = pd.DataFrame([[i,i+1.2,i+2, 'hi'] 
    for i in range(10)],
        columns = ['foo', 'bar', 'baz', 'foobar'])
print(df)

print(df.mean())

print(df['foo'])
print(df.bar)

print(df.bar.mean())