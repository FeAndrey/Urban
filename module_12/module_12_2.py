# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
from operator import attrgetter
from pprint import pprint
from unittest import TestCase
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        self.participants = sorted(self.participants, key=attrgetter('speed'), reverse=True) #***<---
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break #***<---
        return finishers

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls. all_results = {}  # результаты всех тестов.
        return cls.all_results

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 44)
        self.run3 = Runner('Ник', 3)
        self.run4 = Runner('Дэн', 21)
        self.run5 = Runner('Джон', 2)

    def test1(self):
        test = Tournament(150, self.run1, self.run3)
        self.all_results.update(test.start())
        self.assertEqual(self.all_results.get(max(self.all_results)), self.run3.name)

    def test2(self):
        test = Tournament(50, self.run2, self.run3)
        self.all_results.update(test.start())
        self.assertTrue(self.all_results.get(max(self.all_results)), self.run3.name)

    def test3(self):
        test = Tournament(6, self.run1, self.run2, self.run3)
        self.all_results={**self.all_results,**test.start()}
        self.assertEqual(self.all_results.get(max(self.all_results)), self.run3.name)

    def test4(self):
        test = Tournament(3, self.run3, self.run2, self.run1, self.run4, self.run5)
        self.all_results={**self.all_results,**test.start()}
        self.assertEqual(self.all_results.get(max(self.all_results)), self.run5.name)

    # В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
    # (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
    # ***<--- Вот здесь вообще не понял, assertTrue проверяет утверждение на ложь/истина, он не может сравнивать
    # что-либо, поэтому его не делал, а тесты сделаны через assertEqual.

    def tearDown(self):
        print('test:')
        for key, value in self.all_results.items():
            print("{0}: {1}".format(key, value))

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    # ***<--- через tearDownClass не получается вывести all_results, т.к. ключи в all_results постоянно перезаписываются
    # после каждого нового теста, поэтому реализовал выше, через tearDown (вызов метода после каждого теста)
    # @classmethod
    # def tearDownClass(cls):
    #     for key, value in cls.all_results.items():
    #         print("{0}: {1}".format(key, value))

if __name__ == "__main__":
    unittest.main()