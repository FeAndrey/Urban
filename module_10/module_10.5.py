# Домашнее задание по теме "Многопроцессное программирование"

import time
from multiprocessing import Pool, current_process

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(file.readline().replace('\n', ''))
    print('WORKER FUNC() => ', current_process().name)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    time_start = time.time()
    for filename in filenames:
        read_info(filename)
    elapsed_seconds = time.time() - time_start
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_seconds))
    print(f'Время на Линейный вызов: {formatted_time}.{round((time.time()-time_start)*1000000)}\n')

    # Многопроцессный с классом Pool()
    time_start = time.time()
    with Pool(processes=4) as pool:
        res = pool.map(read_info, filenames)
    elapsed_seconds = time.time() - time_start
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_seconds))
    print(f'Время на Многопроцессный с классом Pool(): {formatted_time}.{round((time.time() - time_start) * 1000000)}\n')


