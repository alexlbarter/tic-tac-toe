import unittest
from scripts import console_display


class TestConsoleDisplay(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(console_display.generate_display_str([0, 0, 0, 0, 0, 0, 0, 0, 0]),
                         "   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   ")

    def test_all_same_symbol(self):
        self.assertEqual(console_display.generate_display_str([1, 1, 1, 1, 1, 1, 1, 1, 1]),
                         " O | O | O \n---+---+---\n O | O | O \n---+---+---\n O | O | O ")
        self.assertEqual(console_display.generate_display_str([2, 2, 2, 2, 2, 2, 2, 2, 2]),
                         " X | X | X \n---+---+---\n X | X | X \n---+---+---\n X | X | X ")

    def test_custom_symbols(self):
        self.assertEqual(console_display.generate_display_str([0, 0, 0, 0, 0, 0, 0, 0, 0], [" ", "*", "?"]),
                         "   |   |   \n---+---+---\n   |   |   \n---+---+---\n   |   |   ")
        self.assertEqual(console_display.generate_display_str([1, 1, 1, 1, 1, 1, 1, 1, 1], [" ", "*", "?"]),
                         " * | * | * \n---+---+---\n * | * | * \n---+---+---\n * | * | * ")
        self.assertEqual(console_display.generate_display_str([2, 2, 2, 2, 2, 2, 2, 2, 2], [" ", "*", "?"]),
                         " ? | ? | ? \n---+---+---\n ? | ? | ? \n---+---+---\n ? | ? | ? ")
        self.assertEqual(console_display.generate_display_str([1, 2, 1, 2, 1, 2, 1, 2, 1], [" ", "*", "?"]),
                         " * | ? | * \n---+---+---\n ? | * | ? \n---+---+---\n * | ? | * ")

    def test_custom_symbols_errors(self):
        with self.assertRaises(ValueError):
            console_display.display_game([0, 0, 0, 0, 0, 0, 0, 0, 0], ["", "G"])
            console_display.display_game([0, 0, 0, 0, 0, 0, 0, 0, 0], ["G", ""])
            console_display.display_game([0, 0, 0, 0, 0, 0, 0, 0, 0], ["", ""])
            console_display.display_game([0, 0, 0, 0, 0, 0, 0, 0, 0], [" G", "G "])
            console_display.display_game([0, 0, 0, 0, 0, 0, 0, 0, 0], ["G", "G"])


if __name__ == '__main__':
    unittest.main()
