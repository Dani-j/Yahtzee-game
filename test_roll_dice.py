from unittest import TestCase
from yahtzee import roll_dice
from unittest.mock import patch


class TestRollDice(TestCase):

    @patch('random.sample', return_value=["1", "2", "4", "5", "6"])
    def test_roll_dice_kept_dice_length_0(self, mock_output):
        kept_dice = []
        result = roll_dice(kept_dice)
        expected = ["1", "2", "4", "5", "6"]
        self.assertEqual(result, expected)

    @patch('random.sample', return_value=["2", "4", "5", "6"])
    def test_roll_dice_kept_dice_length_1(self, mock_output):
        kept_dice = ["1"]
        result = roll_dice(kept_dice)
        expected = ["2", "4", "5", "6"]
        self.assertEqual(result, expected)

    @patch('random.sample', return_value=["1", "2", "4"])
    def test_roll_dice_kept_dice_length_2(self, mock_output):
        kept_dice = ["1", "3"]
        result = roll_dice(kept_dice)
        expected = ["1", "2", "4"]
        self.assertEqual(result, expected)

    @patch('random.sample', return_value=["1", "3"])
    def test_roll_dice_kept_dice_length_3(self, mock_output):
        kept_dice = ["1", "3", "5"]
        result = roll_dice(kept_dice)
        expected = ["1", "3"]
        self.assertEqual(result, expected)

    @patch('random.sample', return_value=["6"])
    def test_roll_dice_kept_dice_length_4(self, mock_output):
        kept_dice = ["1", "3", "5", "1"]
        result = roll_dice(kept_dice)
        expected = ["6"]
        self.assertEqual(result, expected)
