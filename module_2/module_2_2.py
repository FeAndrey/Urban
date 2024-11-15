first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Все числа равны -', 3)
elif first == second or second == third or third == first:
     print('Два числа равны -', 2)
elif first != second  and second != third and third != first:
        print('Все числа не равны -', 0)
else: # для данных условин не актуально, но если чисель и условий будет больше, то актуально
    print('Непредвиденное условие')
