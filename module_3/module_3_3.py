def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('Первое Задание:')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print('\nВторое Задание:')
values_list = ['Строка', True, 25]
values_dict = {'a': 25, 'b': True, 'c': 'Строка'}
print_params(*values_list)
print_params(**values_dict)
print_params(values_list, values_dict, c=99)    # добавление в функцию без распаковки

print('\nТретье Задание:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)