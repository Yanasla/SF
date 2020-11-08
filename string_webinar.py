string = "Семь бед - один reset"
a=string.split()[0].lower()

print(a)
print(string.split()[-1])
print(string.split()[3])
print(string.split()[-1][::-1])
for letter in string:
    print(letter)
for letter in string:
    print(letter, end = '*')

print(string[::-1])

for i in range(1, len(string)+1):
    print(string[-i], end = '')
info = 'Фамилия: Иванова, имя: Агафья, e-mail: agafiya@ivanova.me'