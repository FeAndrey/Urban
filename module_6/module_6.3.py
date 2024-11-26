import random

# Animal - класс описывающий животных.
class Animal:
    live = True
    sound = None                # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0       # степень опасности существа

    # _cords = [0, 0, 0] - координаты в пространстве.
    # speed = ... - скорость передвижения существа (определяется при создании объекта)
    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    # меняет соответствующие кооординаты в _cords на dx, dy и dz Если при попытке изменения координаты z в _cords
    # значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(", при этом изменения не вносяться.
    def move(self, dx, dy, dz):
        for i in range(len(self._cords)):
            if i == 0:
                self._cords[i] = dx * self.speed
            if i == 1:
                self._cords[i] = dy * self.speed
            if i == 2:
                if dz * self.speed < 0:
                    print("It's too deep, i can't dive :(")
                else:
                    self._cords[i] = dz * self.speed

    # выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    # выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0",
    # если равно или больше.
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # выводит строку со звуком sound
    def speak(self):
        print(self.sound)



# Bird - класс описывающий птиц. Наследуется от Animal.
class Bird(Animal):
    beak = True                 # наличие клюва

    # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
    def lay_eggs(self):
        print('Here are(is) ', random.randint(1, 4) , 'eggs for you')



# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3       # степень опасности существа

    # dz изменение координаты z в _cords
    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * (self.speed / 2))


# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8       # степень опасности существа



# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed, sound = "Click-click-click"):      # звук, который издаёт утконос
        self.sound = sound
        super().__init__(speed)



if __name__ == "__main__":
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()
