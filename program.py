'''
Все написано в vim.

Параметры ПК (кому интересно):
    CPU: Intel Celeron 3.06GHz
    RAM: 512Mib
    Все остальное от intel, 2005 года выпуска 
'''

import pandas as pd
import matplotlib.pyplot as plt


try:
    data = pd.read_excel('Мск_5лет.xls', skiprows=6)
    data['usadate'] = pd.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst=True)
    data = data.sort_values('usadate')
    data = data.fillna(0.01)
    data = data.reset_index()
except:
    print("Ошибка: Проверьте наличие файла Мск_5лет.xls.\nОн должен находится в той же директории что и исполняемый файл.\nВ нем должны находится столбцы в изначальной конфигурации\nЕсли не помогло - то обращайтесь ко мне в телеграм.")
else:
    commandToKey = {"ТемпВоздуха": "T", "АтмосДавление": "P", "БарическаяТенд": "Pa",
                    "ОтносительнаяВлажн": "U", "МинТемпВоздуха": "Tn",
                    "МаксТемпВоздуха": "Tx", "ГоризДальнВидимости(км)": "VV"}


    def testDate(date: str):
        ret = False
        
        if date[0] == 'None':
            return True

        if len(date) != 3:
            print("Ошибка: Неверная форма даты (вероятно вы неправильно рассавили точки)")
        else:          

            try:
                arg = int(date[0])
                arg = int(date[1])
                arg = int(date[2])
            except ValueError:
                print("Ошибка: Неверная форма даты (в дате должны быть только цифры)")
                ret = False
            else:
                if len(date[0]) != 4 or len(date[1]) != 2 or len(date[2]) != 2:
                    print("Ошибка: Неверная форма даты (вы неправильно сконфигурировали дату, сначала год(4 цифры), потом день(2 цифры), потом месяц(2 цифры))")
                elif int(date[2]) > 12 or int(date[1]) > 31:
                    print("Ошибка: Неверная форма даты (месяц не может быть больше 12, а день 31)")
                elif int(date[0]) < 1970 or int(date[1]) <= 0 or int(date[2]) <= 0:
                    print("Ошибка: Неверная форма даты (год не может быть меньше 1970, а день и месяц не могут быть равны нулю)")
                elif int(date[0]) > 2050:
                    print("Ошибка: Неверная форма даты (год не может быть больше 2050)")
                else:
                    ret = True
    
        return ret

    print("Чтобы узнать список комманд введите help.\nЧтобы выйти введите exit\n")

    while True:

        cmd = input("Введите команду: ")
        if cmd == 'exit':
            break
        elif cmd == 'help':
            for ctk in commandToKey.keys(): print(ctk)
            continue

        try:
            key = commandToKey[cmd]
        except KeyError:
            print("Ошибка: Введена неверная команда.")
        else:
            while True:

                start_date = input("Введите начальную дату YYYY.DD.MM (или None если хотите с самой старой даты): ").split('.')
                if testDate(start_date):
                    break

            while True:

                end_date = input("Введите конечную дату YYYY.DD.MM (или None если хотите до самой новой даты): ").split('.')
                if testDate(end_date):
                    break

            predate = data.head(1)['usadate'].item()
            if start_date[0] != 'None':
                start_date = pd.Timestamp(year=int(start_date[0]), day=int(start_date[1]), month=int(start_date[2]))
                if start_date < predate:
                    start_date = predate
                    print("Начальная дата слишком ранняя. Она была заменена на самую раннюю возможную")
            else:
                start_date = predate

            predate = data.tail(1)['usadate'].item()
            if end_date[0] != 'None':
                end_date = pd.Timestamp(year=int(end_date[0]), day=int(end_date[1]), month=int(end_date[2]))
                if end_date > predate:
                    end_date = predate
                    print("Конечная дата слишком длинная. Она была заменена на самую дальнюю возможную")

            else:
                end_date = predate

            condi = data['usadate'] > start_date
            tion = data['usadate'] < end_date
            condition = condi == tion
            data_short = data[condition]
            x = data_short['usadate']
            y = data_short[key]
            plt.figure(figsize=(15, 5))
            plt.xlabel('Дата')
            plt.ylabel(cmd)
            print('Все NaN были заменены 0.01')
            plt.plot(x, y)
            plt.show()

