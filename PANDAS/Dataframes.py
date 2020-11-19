import pandas as pd

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

print(df)

df2 = pd.DataFrame([ [1,2,3], [2,3,4] ],
                  columns = ['foo', 'bar', 'baz'], 
                  index = ['foobar', 'foobaz'])
print(df2)