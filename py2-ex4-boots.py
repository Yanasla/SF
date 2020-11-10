csv_dict = [
    {'id': '100412', 'position': 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 'count': 9},
    {'id': '100728', 'position': 'Скейтборд Jdbug RT03', 'count': 32},
    {'id': '100732', 'position': 'Роллерсерф Razor RipStik Bright', 'count': 11},
    {'id': '100803', 'position': 'Ботинки для сноуборда DC Tucknee', 'count': 20},
    {'id': '100898', 'position': 'Шагомер Omron HJA-306', 'count': 2},
    {'id': '100934', 'position': 'Пульсометр Beurer PM62', 'count': 17},
]
csv_dict_boots = []

csv_dict_boots = []
for item in csv_dict:
    if 'Ботинки' in item['position']:
        csv_dict_boots.append(item)
print(csv_dict_boots)



