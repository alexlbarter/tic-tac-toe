import unittest
from scripts import main
import unittest.mock


class TestMain(unittest.TestCase):
    def test_get_move_valid_numbers(self):
        cases = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9))
        game = main.Game(1)
        for case in cases:
            with unittest.mock.patch("builtins.input", return_value=case[0]):
                self.assertEqual(game.get_move(), case[1])


if __name__ == '__main__':
    unittest.main()