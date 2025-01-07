# Домашнее задание по теме "Создание потоков"

import threading
import time
from threading import Thread

def  wite_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.writelines(['Какое-то слово №', str(i+1), '\n'])
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    return False

time_start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
print(f'*** Работа основного потока {time.time() - time_start}\n')

time_start = time.time()
Thread1 = threading.Thread(target=wite_words, args = (10, 'example5.txt'))
Thread2 = threading.Thread(target=wite_words, args = (30, 'example6.txt'))
Thread3 = threading.Thread(target=wite_words, args = (200, 'example7.txt'))
Thread4 = threading.Thread(target=wite_words, args = (100, 'example8.txt'))

Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

Thread1.join()
Thread2.join()
Thread2.join()
Thread3.join()

if Thread1.is_alive() and  Thread2.is_alive() and Thread3.is_alive() and Thread4.is_alive():
    pass
else:
    print(f'*** Работа вспомогательных потоков {time.time() - time_start}')