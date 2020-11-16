import random

user_db = [{'orders': 12}, {'orders': 30}, {'orders': 45}]

def avg_orders(lst):
    order_sum = sum([user['orders'] for user in user_db])
    result = order_sum/len(user_db)
    return result

print(avg_orders(user_db))



import random
# добавьте функцию get_euro_rate

def get_euro_rate():
    n = random.randint(65, 85)
    return n

print(get_euro_rate())

# используйте get_euro_rate в следующей функции
def to_euro(price):  
    exchange_rate = get_euro_rate()  
    rounded = round(price/exchange_rate, 2)  
    return '€' + str(rounded)

print(to_euro(70))