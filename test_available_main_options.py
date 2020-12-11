from unittest import TestCase
from yahtzee import available_main_options


class TestAvailableMainOptions(TestCase):
    def test_available_main_options_dice_time_2_kept_dice_length_0(self):
        dice_time = 2
        kept_dice = []
        expected = available_main_options(dice_time, kept_dice)
        actual = {"1", "3", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_2_kept_dice_length_3(self):
        dice_time = 2
        kept_dice = [2, 3, 4]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"1", "2", "3", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_2_kept_dice_length_5(self):
        dice_time = 2
        kept_dice = [1, 2, 3, 4, 5]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"2", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_1_kept_dice_length_2(self):
        dice_time = 1
        kept_dice = [3, 1, 1]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"1", "2", "3", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_1_kept_dice_length_5(self):
        dice_time = 1
        kept_dice = [3, 1, 1, 3, 4]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"2", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_0_kept_dice_length_2(self):
        dice_time = 0
        kept_dice = [3, 1, 1]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"1", "2", "4", "5"}
        self.assertEqual(expected, actual)

    def test_available_main_options_dice_time_0_kept_dice_length_5(self):
        dice_time = 0
        kept_dice = [3, 1, 1, 1, 1]
        expected = available_main_options(dice_time, kept_dice)
        actual = {"2", "4", "5"}
        self.assertEqual(expected, actual)
