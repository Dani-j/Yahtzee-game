from unittest import TestCase
from unittest.mock import patch
from yahtzee import remove_dice


class TestRemoveDice(TestCase):

    @patch('builtins.input', side_effect="1")
    def test_remove_dice_remove_part_on_hand_no_space(self, mock_input):
        kept_dice = ["1", "3"]
        table_dice = ["1", "3", "5"]
        actual = remove_dice(kept_dice, table_dice)
        expected = (["3"], ["1", "3", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="1 3")
    def test_remove_dice_remove_part_on_hand_with_space(self, mock_input):
        kept_dice = ["1", "3", "4"]
        table_dice = ["1", "3"]
        actual = remove_dice(kept_dice, table_dice)
        expected = (["4"], ["1", "3", "3", "4"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="16")
    def test_remove_dice_remove_all_on_hand(self, mock_input):
        kept_dice = ["1", "6"]
        table_dice = ["1", "3", "5"]
        actual = remove_dice(kept_dice, table_dice)
        expected = ([], ["1", "3", "5", "1", "6"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="66666666")
    def test_remove_dice_remove_more_than_on_hand(self, mock_input):
        kept_dice = ["6"]
        table_dice = ["1", "3", "5", "2"]
        actual = remove_dice(kept_dice, table_dice)
        expected = ([], ["1", "3", "5", "2", "6"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="679089dfahi/")
    def test_remove_dice_remove_not_on_hand(self, mock_input):
        kept_dice = ["2", "3"]
        table_dice = ["1", "4", "5"]
        actual = remove_dice(kept_dice, table_dice)
        expected = (["2", "3"], ["1", "4", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect="666665gs909087j")
    def test_remove_dice_remove_on_hand_and_not_on_hand(self, mock_input):
        kept_dice = ["5", "3", "6", "6"]
        table_dice = ["1"]
        actual = remove_dice(kept_dice, table_dice)
        expected = (["3"], ["1", "6", "6", "5"])
        self.assertEqual(expected, actual)
