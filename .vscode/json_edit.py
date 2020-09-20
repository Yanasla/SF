import json
with open('data.json', 'rb') as infile: #код открывает файл 'data.json'
    data = json.load(infile) #затем преобразует JSON в в словари и списки
print(data.keys()) #посмотрим ключи словаря 
print(data['events_data']) #В нашем словаре-один ключ 'events_data',посмотрим значение доступное по этому ключу:
data_list = data['events_data'] #список в новую переменную data_list, 
#чтобы нам не приходилось каждый раз обращаться к одному и тому же ключу 'events_data' в словаре data.
print(len(data_list)) #длину получившегося списка
print(data_list)
print(type(data_list))
categories = []
for item in data_list:#пройдемся циклом по всем событиям и 
#запишем в новый список все встречающиеся категории (ключ 'category')
    category = item['category']
    categories.append(category)
print(categories)
import collections #подсчитаем частоту встречаемости каждого из событий
c = collections.Counter()
for category in categories:
    c[category] += 1
print (c)

table_clients = [] #какие клиенты совершают события table
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'table':
        table_clients.append(client_id)
print(table_clients)
c = collections.Counter()#посчитать, 
#кто из клиентов чаще всего совершал действие 'table'
for table_client in table_clients:
    c[table_client] += 1
print(c)
print (len(c.keys())) #посчитать количество пользователей