from unittest import TestCase
from unittest.mock import patch
from yahtzee import remove_dice


class TestRemoveDice(TestCase):

    @patch('builtins.input', return_value="1")
    def test_remove_dice_part_kept_dice_no_space(self, mock_input):
        kept_dice = ["1", "3"]
        table_dice = ["1", "3", "5"]
        actual = remove_dice(table_dice, kept_dice)
        expected = (["3"], ["1", "3", "5", "1"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1 3")
    def test_remove_dice_part_kept_dice_with_space(self, mock_input):
        kept_dice = ["1", "3", "4"]
        table_dice = ["1", "3"]
        actual = remove_dice(table_dice, kept_dice)
        expected = (["4"], ["1", "3", "1", "3"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="16")
    def test_remove_dice_all_kept_dice(self, mock_input):
        kept_dice = ["1", "6"]
        table_dice = ["1", "3", "5"]
        actual = remove_dice(table_dice, kept_dice)
        expected = ([], ["1", "3", "5", "1", "6"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="66666666")
    def test_remove_dice_more_than_kept_dice(self, mock_input):
        kept_dice = ["6"]
        table_dice = ["1", "3", "5", "2"]
        actual = remove_dice(table_dice, kept_dice)
        expected = ([], ["1", "3", "5", "2", "6"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="679089dfahi/")
    def test_remove_dice_not_in_kept_dice(self, mock_input):
        kept_dice = ["2", "3"]
        table_dice = ["1", "4", "5"]
        actual = remove_dice(table_dice, kept_dice)
        expected = (["2", "3"], ["1", "4", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="666665gs909087j")
    def test_remove_dice_both_in_kept_dice_and_not_in_kept_dice(self, mock_input):
        kept_dice = ["5", "3", "6", "6"]
        table_dice = ["1"]
        actual = remove_dice(table_dice, kept_dice)
        expected = (["3"], ["1", "6", "6", "5"])
        self.assertEqual(expected, actual)