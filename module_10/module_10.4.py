# Домашнее задание по теме "Очереди для обмена данными между потоками."
import random
import threading
import time
from queue import Queue



class Table:
    def __init__(self, number):
        guest = None
        self.number = number
        self.guest = guest



class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = str(name)
    def run(self):
        time.sleep(random.randint(3, 10))



class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for i in range(len(guests)):
            for j in range(len(tables)):
                if tables[j].guest is None:
                    tables[j].guest = guests[i]
                    print(f'{guests[i].name} сел(-а) за стол номер {tables[j].number}')
                    break
            if i >= len(tables):
                self.queue.put(guests[i])
                print(f'{guests[i].name} в очереди')

    def discuss_guests(self):
        tabl_empty = False
        while not self.queue.empty() or tabl_empty == False:
            for i in range(len(tables)):
                if tables[i].guest is not None and tables[i].guest.is_alive() == False:
                    print(f'{tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {tables[i].number} свободен')
                    tables[i].guest = None
                if tables[i].guest is None and self.queue.empty() == False:
                    tables[i].guest = self.queue.get()
                    print(f'{tables[i].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tables[i].number}')
                    tables[i].guest.start()
                for j in range(len(tables)):
                    if tables[j].guest is None:
                        tabl_empty = True
                    else:
                        tabl_empty = False
                        break

# Выполняемый код:
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
print('\n')
cafe.discuss_guests()

print('\n')
print('***Заведение закрыто***')