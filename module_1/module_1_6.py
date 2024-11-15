my_dict = {'admin': 123, 'user_': 456, 'user_2': 789}
print('Dict: ', my_dict)

print('admin pass: ', my_dict['admin'])

print('Not existing value: ', my_dict.get('user_3'))

my_dict['user_3'] = 333
my_dict['user_4'] = 444
my_dict.update({'user5': 555,
                'user6': 666})
print('add: ', my_dict)

del my_dict['user_4']
print('del: ', my_dict)

a = my_dict.pop('user6')
print('user_6 value: ', a)
print('pop: ', my_dict)

print('*************************************')

my_set = {1,1,2,3,4,4,5,'admin','user_', 'user_', 'user_1', 'user_2', 'user_1'}
print('set: ', my_set)

my_set.add('user_3')
my_set.add('user_4')
print('add set: ', my_set)

my_set.remove('admin')
print('Remove set: ', my_set)


