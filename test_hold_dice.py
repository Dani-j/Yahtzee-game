from unittest import TestCase
from unittest.mock import patch
from yahtzee import hold_dice


class TestHoldDice(TestCase):

    @patch('builtins.input', return_value="1")
    def test_hold_dice_part_table_dice_no_space(self, mock_input):
        table_dice = ["1", "3"]
        kept_dice = ["1", "3", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "1"], ["3"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1 3")
    def test_hold_dice_part_table_dice_with_space(self, mock_input):
        table_dice = ["1", "3", "4"]
        kept_dice = ["1", "3"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "1", "3"], ["4"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="16")
    def test_hold_dice_all_table_dice(self, mock_input):
        table_dice = ["1", "6"]
        kept_dice = ["1", "3", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "1", "6"], [])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="66666666")
    def test_hold_dice_more_than_table_dice(self, mock_input):
        table_dice = ["6"]
        kept_dice = ["1", "3", "5", "2"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "2", "6"], [])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="679089dfahi/")
    def test_hold_dice_not_in_table_dice(self, mock_input):
        table_dice = ["2", "3"]
        kept_dice = ["1", "4", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "4", "5"], ["2", "3"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="666665gs909087j")
    def test_hold_dice_both_in_table_dice_and_not_in_table_dice(self, mock_input):
        table_dice = ["5", "3", "6", "6"]
        kept_dice = ["1"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "6", "6", "5"], ["3"])
        self.assertEqual(expected, actual)
