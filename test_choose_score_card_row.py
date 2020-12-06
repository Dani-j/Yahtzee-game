from unittest import TestCase
from yahtzee import choose_score_card_row
from unittest.mock import patch


class Test(TestCase):
    """
    Because it is a while loop, loop until user input valid input, I'm only testing valid input there.
    """

    @patch('builtins.input', side_effect='A')
    def test_choose_score_card_row_valid_input(self, mock_input):
        available_row_options = ["A", "B", "C"]
        actual = choose_score_card_row(available_row_options)
        expected = "A"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect='D')
    def test_choose_score_card_row_another_valid_input(self, mock_input):
        available_row_options = ["A", "B", "C", "D"]
        actual = choose_score_card_row(available_row_options)
        expected = "D"
        self.assertEqual(expected, actual)
