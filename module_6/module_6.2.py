class Vehicle:  # Vehicle - это любой транспорт
    __COLOR_VARIANTS = list (['black', 'white', 'red', 'blue', 'Pink', 'green'])
    def __init__(self, owner, __model,__color, __engine_power):
        self.owner = str(owner)                     # владелец транспорта
        self.__model = str(__model)                 # модель (марка) транспорта
        self.__engine_power = int(__engine_power)   # мощность двигателя
        self.__color = str(__color)                 # название цвета
    def get_model(self):
        return f'Модедь: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print (self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}' )
    def set_color(self,  new_color):                # смена цвета из списка
        if str(new_color.lower()) in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):                               # Sedan(седан) - наследник класса Vehicle.
    __PASSENGERS_LIMIT = 5                          # в седан может поместиться только 5 пассажиров



if __name__ == "__main__":

    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()
    print('\n')

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'
    print('\n')

    # Проверяем что поменялось
    vehicle1.print_info()
