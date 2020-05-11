import unittest
from scripts import main
import unittest.mock


class TestMain(unittest.TestCase):
    def test_get_move_valid_numbers(self):
        cases = (("1", 0), ("2", 1), ("3", 2), ("4", 3), ("5", 4), ("6", 5), ("7", 6), ("8", 7), ("9", 8))
        game = main.Game(1)
        for case in cases:
            with self.subTest(case=case):
                with unittest.mock.patch("builtins.input", return_value=case[0]):
                    self.assertEqual(game.get_move(), case[1])

    def test_get_move_invalid_numbers(self):
        cases = ("0", "10", "0.5")
        game = main.Game(1)
        for case in cases:
            with self.subTest(case=case):
                with unittest.mock.patch("builtins.input", return_value=case):
                    with self.assertRaises(ValueError):
                        game.get_move()

    def test_get_move_valid_words(self):
        cases = (("top left", 0), ("top middle", 1), ("top right", 2),
                 ("middle left", 3), ("centre", 4), ("middle right", 5),
                 ("bottom left", 6), ("bottom middle", 7), ("bottom right", 8))
        game = main.Game(1)
        for case in cases:
            with self.subTest(case=case):
                with unittest.mock.patch("builtins.input", return_value=case[0]):
                    self.assertEqual(game.get_move(), case[1])

    def test_get_move_invalid_words(self):
        cases = ("top", "bottom", "left", "right")
        game = main.Game(1)
        for case in cases:
            with self.subTest(case=case):
                with unittest.mock.patch("builtins.input", return_value=case):
                    with self.assertRaises(ValueError):
                        game.get_move()


if __name__ == '__main__':
    unittest.main()
