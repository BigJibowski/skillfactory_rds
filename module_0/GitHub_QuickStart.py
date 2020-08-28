def game_core(number):
    count = 0
    start = 1
    end = 100
    while start < end:
        count += 1
        mean = (start+end)//2
        if mean == number: 
            break
        if number < mean:
            end = mean
        else:
            start = mean
    return(count)
    
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core)