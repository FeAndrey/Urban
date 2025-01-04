first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Добавлено условие - Если длина данных списков, одинаковая

# В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и
# second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
first_result = (len(list(x)[0])-len(list(x)[1]) for x in zip(first, second) if len(list(x)[0]) != len(list(x)[1])
                if len(first) == len(second))

# В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых
# позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first))
                 if len(first) == len(second))

# Пример выполнения кода:
print(list(first_result))
print(list(second_result))