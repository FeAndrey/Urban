# Домашнее задание по теме "Блокировки и обработка ошибок"

import random
import threading
import time

class Bank:
    def __init__(self):
        balance = 0
        lock = threading.Lock()
        deposit_finish = False # Метка, если deposit уже завершил 100 проходов, а take еще нет. Иначе выполнение
        # программы зависает
        self.balance =balance
        self.lock = lock
        self.deposit_finish = deposit_finish

    def deposit(self):
        for i in range(100):
            rand = random.randint(50, 500)
            self.balance += rand
            print(f'Пополнение на: {rand}. Баланс: {self.balance}')
            time.sleep(0.001)
        if self.balance >= 500 and self.lock.locked() == True:
            self.lock.release()
        self.deposit_finish = True # метод завершил свою работу

    def take(self):
        for i in range(100):
            rand = random.randint(50, 500)
            print(f'Запрос на сняте: {rand}')
            if rand <= self.balance:
                self.balance -= rand
                print(f'Снятие: {rand}. Баланс: {self.balance}')
                time.sleep(0.001)
            # Если deposit завершил свою работу, и баланс меньше генерируемого числа, то break что бы не завис цикл for
            if self.deposit_finish == True and rand > self.balance:
                break
            if rand > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')