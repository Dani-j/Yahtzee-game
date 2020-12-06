from unittest import TestCase
from yahtzee import main_menu_unavailable_options


class Test(TestCase):
    def test_main_menu_unavailable_options_dice_time_2_kept_dice_length_0(self):
        dice_time = 2
        kept_dice = []
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([], 2)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_2_kept_dice_length_3(self):
        dice_time = 2
        kept_dice = [2, 3, 4]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([], 2)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_2_kept_dice_length_5(self):
        dice_time = 2
        kept_dice = [1, 2, 3, 4, 5]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([1, 3], 2)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_1_kept_dice_length_2(self):
        dice_time = 1
        kept_dice = [3, 1, 1]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([], 1)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_1_kept_dice_length_5(self):
        dice_time = 1
        kept_dice = [3, 1, 1, 3, 4]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([1, 3], 1)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_0_kept_dice_length_2(self):
        dice_time = 0
        kept_dice = [3, 1, 1]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([3], 0)
        self.assertEqual(expected, actual)

    def test_main_menu_unavailable_options_dice_time_0_kept_dice_length_5(self):
        dice_time = 0
        kept_dice = [3, 1, 1, 1, 1]
        expected = main_menu_unavailable_options(dice_time, kept_dice)
        actual = ([1, 3], 0)
        self.assertEqual(expected, actual)
