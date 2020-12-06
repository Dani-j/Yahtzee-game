from unittest import TestCase
from yahtzee import move_available_dice


class Test(TestCase):

    def test_move_available_dice_all_from_table_dice_to_kept_dice(self):
        table_dice = ['3', '1', '2']
        kept_dice = ['1', '2']
        input_dice = ["2", "3", "1"]
        actual = move_available_dice(table_dice, kept_dice, input_dice)
        expected = (['1', '2', '2', '3', '1'], [])
        self.assertEqual(expected, actual)

    def test_move_available_dice_all_part_from_table_dice_to_kept_dice(self):
        table_dice = ['3', '3', '2']
        kept_dice = ['1', '2']
        input_dice = ["3", "3"]
        actual = move_available_dice(table_dice, kept_dice, input_dice)
        expected = (['1', '2', '3', '3'], ['2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_none_from_table_dice_to_kept_dice(self):
        table_dice = ['3', '6', '2']
        kept_dice = ['1', '2']
        input_dice = []
        actual = move_available_dice(table_dice, kept_dice, input_dice)
        expected = (['1', '2'], ['3', '6', '2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_all_from_kept_dice_to_table_dice(self):
        table_dice = ['3', '4', '2']
        kept_dice = ['1', '2']
        input_dice = ['1', '2']
        actual = move_available_dice(kept_dice, table_dice, input_dice)
        expected = (['3', '4', '2', '1', "2"], [])
        self.assertEqual(expected, actual)

    def test_move_available_dice_part_from_kept_dice_to_table_dice(self):
        table_dice = ['3', '3', '2']
        kept_dice = ['1', '2']
        input_dice = ["1"]
        actual = move_available_dice(kept_dice, table_dice, input_dice)
        expected = (['3', '3', '2', '1'], ['2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_none_from_kept_dice_to_table_dice(self):
        table_dice = ['3', '4', '6']
        kept_dice = ['1', '2']
        input_dice = []
        actual = move_available_dice(kept_dice, table_dice, input_dice)
        expected = (['3', '4', '6'], ['1', '2'])
        self.assertEqual(expected, actual)


