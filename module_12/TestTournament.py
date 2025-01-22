# Домашнее задание по теме "Методы Юнит-тестирования"
# Цель: освоить методы, которые содержит класс TestCase.
from unittest import TestCase
import unittest
import Runner

class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls. all_results = {}  # результаты всех тестов.
        return cls.all_results

    def setUp(self):
        self.run1 = Runner.Runner('Усэйн', 10)
        self.run2 = Runner.Runner('Андрей', 44)
        self.run3 = Runner.Runner('Ник', 3)
        self.run4 = Runner.Runner('Дэн', 21)
        self.run5 = Runner.Runner('Джон', 2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test1(self):
        test = Runner.Tournament(150, self.run1, self.run3)
        self.all_results.update(test.start())
        self.assertEqual(self.all_results.get(max(self.all_results)), self.run3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test2(self):
        test = Runner.Tournament(50, self.run2, self.run3)
        self.all_results.update(test.start())
        self.assertTrue(self.all_results.get(max(self.all_results)), self.run3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test3(self):
        test = Runner.Tournament(6, self.run1, self.run2, self.run3)
        self.all_results={**self.all_results,**test.start()}
        self.assertEqual(self.all_results.get(max(self.all_results)), self.run3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test4(self):
        test = Runner.Tournament(3, self.run3, self.run2, self.run1, self.run4, self.run5)
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