# Домашнее задание по теме "Простые Юнит-Тесты"
# Цель: приобрести навык создания простейших Юнит-тестов
import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test = Runner('runner1')
        for _ in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = Runner('runner2')
        for _ in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        test1 = Runner('runner3')
        test2 = Runner('runner4')
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance)

if __name__ == "__main__":
    unittest.main()
