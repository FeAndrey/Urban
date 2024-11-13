class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(self.new_floor):
            if 0 <= self.new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                break
            else:
                print(i+1, ' этаж')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)