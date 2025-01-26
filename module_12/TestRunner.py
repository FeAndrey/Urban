# Домашнее задание по теме "Простые Юнит-Тесты"
# Цель: приобрести навык создания простейших Юнит-тестов
import logging
import unittest
import TestsLogging_12_4 as Runner

logging.basicConfig(level=logging.INFO, filemode="w", encoding='utf-8', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = False

    # test_walk:
    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте отрицательное значение в speed.
    # В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    # "Неверная скорость для Runner".
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test = Runner.Runner('runner1', -5)
            if test.speed > 0:
                logging.info('"test_walk" выполнен успешно')
                for _ in range(10):
                    test.walk()
                self.assertEqual(test.distance, 50)
        except ValueError:
                logging.warning('Неверная скорость для Runner', exc_info=True)

    # test_run:
    # Оберните основной код конструкцией try-except.
    # При создании объекта Runner передавайте что-то кроме строки в name.
    # В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    # В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением
    # "Неверный тип данных для объекта Runner".
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test = Runner.Runner(5)
            if isinstance(test.name, str):
                logging.info('"test_run" выполнен успешно')
                for _ in range(10):
                    test.run()
                self.assertEqual(test.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = Runner.Runner('runner3',)
        test2 = Runner.Runner('runner4',)
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance)

if __name__ == "__main__":
    unittest.main()
