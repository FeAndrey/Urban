#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = []
primes = []
not_primes = []
is_prime = True

for i in range(99):     #заполнение по длина списка
     numbers.append(i+1)

# первый вариант, нахождение простого по кол-ву делителей
# for i in range(1, len(numbers)):
#      temp = 0
#      for j in range(1, numbers[i]+1):
#         if numbers[i] % j == 0:
#             temp +=1
#      if temp == 2:
#         primes.append(numbers[i])
#      else:
#         not_primes.append(numbers[i])

for i in range(1, len(numbers)):
     is_prime = True
     for j in range(2, int(numbers[i]**0.5 + 1)):
        if numbers[i] % j == 0:
            is_prime = False
            break
     if is_prime == True:
        primes.append(numbers[i])
     else:
        not_primes.append(numbers[i])

print('Список чисел ', numbers)
print('---------------------------')
print('Простые числа ', primes)
print('Не простые числа ', not_primes)