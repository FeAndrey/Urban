class StepValueError(ValueError):
    pass
class Iterator:
    # __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага. В этом методе в
    # первую очередь проверяется step на равенство 0. Если равно, то выбрасывается исключение StepValueError
    # ('шаг не может быть равен 0')
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError
        else:
            self.step = step
        self.pointer = self.start

    # __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self

    # __next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация завершится
    # либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
    def __next__(self):
        if self.start > self.stop and self.step > 0: # если старт>стоп и шаг >0 (условие для отрицательного шага)
            raise StopIteration
        if self.step < 0:   # если шаг меньше 0
            while self.pointer >= self.stop:
                s = self.pointer
                self.pointer += self.step
                return s
            if self.pointer == self.stop-1 or self.start< self.stop: # при (-55, -20, -1) (не будет работать)
                raise StopIteration
        else:
            while self.pointer <= self.stop:
                s = self.pointer
                self.pointer += self.step
                return s
            if self.pointer > self.stop:
                raise StopIteration

# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно', end=' ')

print()

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()