immutable_var = (['a', 'b'], 'str', (True))
print (immutable_var)
immutable_var[0][1] = 'c'
print(immutable_var)
#immutable_var[2] = False       объект не поддерживает изменение элементов
#immutable_var[0] = 2           объект не поддерживает изменение элементов

mutable_list = [1, 2, 3, 4, 5]
print(mutable_list)
mutable_list = [6, 7, 8, 9, 10]
print(mutable_list)
mutable_list[4] = False
print(mutable_list)
mutable_list.append(100)
print(mutable_list)

