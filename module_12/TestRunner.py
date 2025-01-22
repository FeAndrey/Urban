# Домашнее задание по теме "Простые Юнит-Тесты"
# Цель: приобрести навык создания простейших Юнит-тестов
import unittest
import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test = Runner.Runner('runner1')
        for _ in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = Runner.Runner('runner2')
        for _ in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = Runner.Runner('runner3')
        test2 = Runner.Runner('runner4')
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance)

if __name__ == "__main__":
    unittest.main()