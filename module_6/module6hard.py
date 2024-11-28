import math

class Figure:
    sides_count = 0

    # __sides(список сторон (целые числа)), __color(список цветов в формате RGB), filled(закрашенный, bool)
    def __init__(self,  __color = [], __sides = [],  filled=True):

        # если в __sides передается число int или float, а не список, то число преобразуется в список
        if isinstance(__sides, int) or isinstance(__sides, float):
            side_ = []
            side_.append(__sides)
            __sides=side_

        # если тип Circle, то условия сторон для круга
        if isinstance(self, Circle):
            # если передано 1 сторона и она не <0 и не float, то создаем круг
            if len(__sides) == self.sides_count and self.__is_valid_sides(*__sides):
                self.__sides = list(__sides)
            else:
                self.__sides = [1]  # создается круг с единичной стороной

        # если тип Cube, то условия сторон для куба
        if isinstance(self, Cube):
            # если передана одна сторона и она не <0 и не float, то множим сторону на 12
            if len(__sides) == 1 and self.__is_valid_sides(*__sides):
                __sides = [__sides[0]] * self.sides_count
                self.__sides = list(__sides)
            # если передано 12 сторон и все стороны одинаковые и стороны не <0 и не float, то создаем куб
            if len(__sides) == 12 and __sides.count(__sides[0]) == len(__sides) and self.__is_valid_sides(*__sides):
                self.__sides = list(__sides)
            else:
                self.__sides = [1] * Cube.sides_count       # создается куб с единичными сторонами

        # если тип Triangle, то условия сторон для треугольника
        if isinstance(self, Triangle):
            # если передано 3 стороны и треугольник с такими сторонами может существовать и стороны не <0 и не float
            if len(__sides) == self.sides_count and self.triangle_life(__sides) and self.__is_valid_sides(*__sides):
                self.__sides = list(__sides)
            else:
                self.__sides = [1, 1, 1]                # создается треугольник с единичными сторонами

        self.__color = list(__color)
        self.filled = bool(filled)

    # Метод служебный, принимает параметры r, g, b, который проверяет корректность переданных
    # значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
    # от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return r, g, b
        else:
            return [None]

    # Метод принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
    # проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        color_list = list(self.__is_valid_color(r, g, b))
        if color_list != [None]:
            self.__color = color_list

    #
    def get_color(self):
        return self.__color

    # +Метод служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
    # положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *args):
        for i in range(len(args)):
            s = args[i]
            if args[i]<0 or  isinstance(args[i], float):
                return False
        return True

    # Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    # то не изменять, в противном случае - менять. + доп условия на правильность сторон, отрицательное значение сторон,
    # float сторон и расчет периметра для __len__
    def set_sides(self, *new_sides):
        if isinstance(self, Cube):
            if len(new_sides) == 1 and self.__is_valid_sides(*new_sides): # если передана одна сторона, то множим на 12
                self.__sides = [new_sides[0]] * self.sides_count
            if len(new_sides) == 12 and new_sides.count(new_sides[0]) == len(new_sides):    # 12 одинаковых сторон
                if self.__is_valid_sides(*new_sides): # проверка на отрицательные стороны
                    self.__sides = list(new_sides)
                    return self.__sides[11] * self.sides_count   # подсчет периметра для куба, берется любая сторона
        if isinstance(self, Triangle):
            if len(new_sides) == self.sides_count and self.triangle_life(new_sides):    # условия на треугольник
                if self.__is_valid_sides(*new_sides) and len(new_sides) == self.sides_count:
                    self.__sides = list(new_sides)
                    return sum(self.__sides)    # подсчет периметра
        if isinstance(self, Circle):
            if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides): # если 1 сторона->создаем круг
                self.__sides = list(new_sides)
                return  self.__sides[0] # подсчет периметра

    # возвращение значение я атрибута __sides.
    def get_sides(self):
        return self.__sides

    # реализация через метод set_sides
    def __len__(self):      # возвращение периметр фигур.
        return self.set_sides(*self.__sides)




class Circle(Figure):
    sides_count = 1

    # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
    def __init__(self, __color = [], __sides = [],  filled=True):
        super().__init__(__color, __sides, filled)
        side_ = self.get_sides()
        radius = side_[0] / (2 * math.pi)       # вычисление радиуса
        self.radius = radius                    # создаем атрибут radius для Circle

    # Метод get_square возвращает площадь круга
    def get_square(self):
        return 2 * math.pi * (self.radius**2)



class Triangle (Figure):
    sides_count = 3

    # Метод get_square возвращает площадь треугольника.
    def get_square(self):
        side_ = self.get_sides()
        p = sum(side_) / 2
        return math.sqrt(p * (p - side_[0]) * (p - side_[1]) * (p - side_[2]))

    # Метод triangle_life определяет существование треугольника по его сторонам
    def triangle_life(self, side_):
        if side_[0] + side_[1] > side_[2] and side_[1] + side_[2] > side_[0] and side_[2] + side_[0] > side_[1]:
            return True
        else:
            return False



class Cube (Figure):
    sides_count = 12

    # +Метод get_volume, возвращает объём куба.
    def get_volume(self):
        side_ = self.get_sides()
        return side_[0]**3



if __name__ == "__main__":

    circle1 = Circle((200, 200, 100), 12)
    cube1 = Cube((222, 35, 130), 6)
    triangle1 = Triangle((125, 5, 55), (5, 4, 8))

    circle2 = Circle((200, 200, 100), [21.3, 15])               # не проходит условия инициализации
    circle3 = Circle((200, 200, 100), 1.6)                      # не проходит условия инициализации
    cube2 = Cube((222, 35, 130), (1,5,6,4,5,5,5,5,5,5,5,5))     # не проходит условия инициализации
    cube3 = Cube((222, 35, 130), (7, 7, 7, 7, 7, 7, -7, 7, 7, 7, 7, 7))# не проходит условия инициализации
    triangle2 = Triangle((125, 5, 55), (5, 4, 1))               # не проходит условия инициализации
    triangle3 = Triangle((125, 5, 55), (5.3, 4, 8.5))           # не проходит условия инициализации

    print('Вывод списка сторон (круг, куб, треугольник):')
    print(circle1.get_sides())
    print(cube1.get_sides())
    print(triangle1.get_sides())
    print('------------------------------------')
    print(circle2.get_sides())
    print(circle3.get_sides())
    print(cube2.get_sides())
    print(cube3.get_sides())
    print(triangle2.get_sides())
    print(triangle3.get_sides())

    print('\nПроверка на изменение цветов:')
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    triangle1.set_color(11,11,11)   # Изменится
    print(triangle1.get_color())

    print('\nПроверка на изменение сторон (круг, куб, треугольник):')
    circle1.set_sides(-16, 5)  # Не изменится, тк отрицательная сторона, и в списке две стороны
    print(circle1.get_sides())
    cube1.set_sides(4,6,5,4,7,8,9,1,2,3,4,4)  # Не изменится, тк куба с такими сторонами не существует
    print(cube1.get_sides())
    triangle1.set_sides(1,2,3)   # Не изменится, тк треугольника с такими сторонами не существует
    print(triangle1.get_sides())

    print('\nПроверка периметра (круг, куб, треугольник):')
    print(len(circle1))
    print(len(cube1))
    print(len(triangle1))

    print('\nПроверка радиуса и площади круга')
    print(circle1.radius)
    print(circle1.get_square())

    print('\nПроверка объёма (куба):')
    print(cube1.get_volume())

    print('\nПроверка площади треугольника:')
    print(triangle1.get_square())