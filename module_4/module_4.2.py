def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    return inner_function() # только так можно получить доступ к дочерней функции, может в будущем научимся как то еще

test_function()
