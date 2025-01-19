# Создать персональную функции для подробной интроспекции объекта.

import inspect, sys

class Car():
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers

        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        if isinstance(self.__vin, int) == False:
            raise  IncorrectVinNumber('Некорректный тип vin номер')
        if 1000000 <= self.__vin and self.__vin <= 9999999:
            return True
        else:
            raise  IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self):
        if isinstance(self.__numbers, str) == False:
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров')
        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True
class IncorrectVinNumber(Exception):
    def __init__(self, message): # атрибут message - сообщение, которое будет выводиться при выбрасывании исключения.
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):  # атрибут message - сообщение, которое будет выводиться при выбрасывании исключения.
        self.message = message

def introspection_info(obj):
    attr = {}
    if (isinstance(obj, int) or isinstance(obj, float) or isinstance(obj, str) or isinstance(obj, list)
            or isinstance(obj, tuple) or isinstance(obj, dict)):
        attr["type"] = type(obj).__name__
        attr["methods"] = [methods for methods in dir(obj) if not methods.startswith("__")]
    else:
        attr["type"] = type(obj).__name__
        attr["attributes"] = [attr for attr in obj.__dict__.keys()]
        attr["methods"] = [methods for methods in dir(obj) if callable(getattr(obj, methods))
                           and not methods.startswith("__")]
        attr["classes"] = [name for name, obj in sys.modules[__name__].__dict__.items()
         if isinstance(obj, type)]
    return attr

if __name__ == "__main__":
# Пример работы:
    first = Car('Model1', 1000000, 'f123dj')
    number_info = introspection_info(85)
    print(number_info)
    number_info = introspection_info(2.5)
    print(number_info)
    number_info = introspection_info("{1:6, 5:5}")
    print(number_info)
    number_info = introspection_info([4,4,5,6])
    print(number_info)
    number_info = introspection_info((1,5,74,5))
    print(number_info)
    number_info = introspection_info({1:6, 5:"456", 5:5})
    print(number_info)
    number_info = introspection_info(first)
    print(number_info)