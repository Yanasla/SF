draw_dict = {
	'Россия': 'A',
	'Португалия': 'B',
	'Франция': 'C',
	'Дания': 'C',
	'Египет': 'A'
}
draw_new = {}
for country, position in draw_dict.items(): #фильтр с items
    if position == 'A':
            draw_new[country] = position
print(draw_new)
