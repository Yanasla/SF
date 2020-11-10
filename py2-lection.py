csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]

print(csv_file[4])

print(csv_file[4][2])

#проход по вложенному списку

for record in csv_file:
    print(record)

for record in csv_file:
    if record[1] == 'Шагомер Omron HJA-306':
        print('Количество шагомеров на складе - {}шт'.format(record[2]))
