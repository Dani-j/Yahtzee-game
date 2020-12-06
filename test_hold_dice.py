from unittest import TestCase
from unittest.mock import patch
from yahtzee import hold_dice


class Test(TestCase):

    @patch('builtins.input', side_effect="1")
    def test_hold_dice_hold_part_on_table_no_space(self, mock_input):
        table_dice = ["1", "3"]
        kept_dice = ["1", "3", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "1"], ["3"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="1 3")
    def test_hold_dice_hold_part_on_table_with_space(self, mock_input):
        table_dice = ["1", "3", "4"]
        kept_dice = ["1", "3"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "3", "4"], ["4"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="16")
    def test_hold_dice_hold_all_on_table(self, mock_input):
        table_dice = ["1", "6"]
        kept_dice = ["1", "3", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "1", "6"], [])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="66666666")
    def test_hold_dice_hold_more_than_on_table(self, mock_input):
        table_dice = ["6"]
        kept_dice = ["1", "3", "5", "2"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "3", "5", "2", "6"], [])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="679089dfahi/")
    def test_hold_dice_hold_not_on_table(self, mock_input):
        table_dice = ["2", "3"]
        kept_dice = ["1", "4", "5"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "4", "5"], ["2", "3"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="666665gs909087j")
    def test_hold_dice_hold_on_table_and_not_on_table(self, mock_input):
        table_dice = ["5", "3", "6", "6"]
        kept_dice = ["1"]
        actual = hold_dice(table_dice, kept_dice)
        expected = (["1", "6", "6", "5"], ["3"])
        self.assertEqual(expected, actual)
