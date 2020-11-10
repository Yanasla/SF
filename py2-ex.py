dict = {'2019-04-01':2504, '2019-04-02':4994, '2019-04-03':6343}
expenses = 0
for expense in dict.values(): #перебор ключей словаря методом keys
    expenses = expenses + expense
print(expenses)