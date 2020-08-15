import numpy as np
a,b=1,101
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")


def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    a,b=1,101
    predict = (a+b)//2
    
    while number != predict:
        count+=1
        if number > predict: 
            a = predict
        elif number < predict: 
            b = predict
        predict = (a+b)//2
    return(count) # выход из цикла, если угадали
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)
