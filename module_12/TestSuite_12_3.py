# Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest
import TestRunner
import TestTournament

test_runner = unittest.TestSuite()
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(TestRunner.RunnerTest))
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTournament.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_runner)