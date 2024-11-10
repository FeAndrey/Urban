s=0

def calculate_structure_sum (data):
    global s                                    #сумма
    for i in range(len(data)):
        if i == len(data):                      #выход из рекурсии
            break
        if isinstance(data[i], tuple) == True:  #проверка на кортеж
            calculate_structure_sum(data[i])    #рекурсия (распаковка кортежа)

        if isinstance(data[i], dict) == True:   #проверка на словарь
            s += sum(data[i].values())          #сложение значений словаря
            list_dict = list(data[i])           #ключи словаря -> в список
            calculate_structure_sum(list_dict)  #рекурсия (подсчет списка ключей словаря)

        if isinstance(data[i], set) == True:    #проверка на множество
            list_set = list(data[i])            #множество -> в список
            calculate_structure_sum(list_set)   #рекурсия (подсчет списка множества)

        if isinstance(data[i], list) == True:   #проверка на список
            calculate_structure_sum(data[i])    #рекурсия (подсчет элементов списка)

        if isinstance(data[i], str) == True:    #если строка
            s += len(data[i])                   #подсчет символов в строке
        if isinstance(data[i], int) == True:    #если число
            s += data[i]                        #счет чисел
    return s

#можно менять любые данные (строка на символ, символ на строку), единственное, что нельзя, это менять
# int значения в словаре на str.
#data_structure = [['str', 2, 3], {0: 4, 21: 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 22, ('Urban2', 'Urban3'))}])]

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


result = calculate_structure_sum(data_structure)

print(result)
