def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            if isinstance(i, str) == True:
                print(f'Некорректный тип данных для подсчёта суммы: {i}')
                incorrect_data += 1
    list_result= [result, incorrect_data]
    return list_result

def calculate_average(numbers):
    try:
        personal_sum_result = personal_sum(numbers)
        sum_ = personal_sum_result[0] / (len(numbers) - personal_sum_result[1])
    except SyntaxError as exc:
        print(f'Синтаксичская ошибка {exc}')
    except (TypeError, ZeroDivisionError):
        if isinstance(numbers, str) == True:
            print(f'В numbers записан строка - {type(numbers)}')
            return 0
        if isinstance(numbers, list) == False:
            print(f'В numbers записан некорректный тип данных - {type(numbers)}')
    else:
         return sum_

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать