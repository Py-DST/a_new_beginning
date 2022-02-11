import numpy as np

def half_sequence(number: int=1) ->int:

    count = 0
    number = np.random.randint(1,100)

    #print(f"Загаданное число: {number}")
    
    min = 1
    max = 100
    predict_number = max / 2
    
    while number != predict_number:
        count+=1
    #рамки поиска
        if number > predict_number:
            min = predict_number + 1    
        
        elif number < predict_number: 
            max = predict_number - 1
            
        predict_number = round((max + min ) / 2) # разбиваем по полам новые рамки поиска
    #print(f'Число попыток: {count}')
    return count     
     
#half_sequence()

def score_game(half_sequence) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    
    for number in random_array:
        count_ls.append(half_sequence(number))
        
    score =int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
   score_game(half_sequence)