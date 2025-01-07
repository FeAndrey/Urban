# Домашнее задание по теме "Потоки на классах"
import threading
import time

class Knight (threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        day = 0
        self.day = day
        enemy = 100
        self.enemy = enemy

    def war(self, name, power):
        while self.enemy != 0:
            self.enemy = self.enemy - self.power
            time.sleep(1)
            self.day += 1
            print(f'{self.name} сражается {self.day} дней(дня), осталось {self.enemy} воинов ')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.war(self.name, self.power)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)! ')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()