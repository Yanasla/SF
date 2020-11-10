phones = {
	'Гордиенко Виктория': 5140,
	'Анисимов Кирилл': 5145,
	'Кузнецова Дарья': 5142
}
if phones['Кузнецова Дарья'] == 5142:
	print('Номер верен')

for name, phone in phones.items():
	if name == 'Кузнецова Дарья' and phone == 5142:
		print('Номер верен')

for record in phones:
	if record == 'Кузнецова Дарья' and phones[record] == 5142:
		print('Номер верен')