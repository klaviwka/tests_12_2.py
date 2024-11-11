import unittest
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # Выводим все результаты после завершения всех тестов
        for key, value in sorted(cls.all_results.items()):
            print(value)

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['test_race_usain_nik'] = {place: str(runner) for place, runner in results.items()}

    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['test_race_andrey_nik'] = {place: str(runner) for place, runner in results.items()}

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['test_race_usain_andrey_nik'] = {place: str(runner) for place, runner in results.items()}


if __name__ == '__main__':
    unittest.main()
