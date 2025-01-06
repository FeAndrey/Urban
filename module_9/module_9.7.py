# Домашнее задание по теме "Декораторы"

def is_prime(func):
    def prime(num): # функция проверки числа
        prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
        i = 5; d = 2;
        while prime and i * i <= num:
            prime = num % i != 0
            i += d
            d = 6 - d
        return prime
    def wrapper(*args): # расширение функционала декоратора
        s = func(*args)
        if prime(s):
            print("Простое")
            return s
        print("Составное")
        return s
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

# Пример:
result = sum_three(2, 3, 6)
print(result)