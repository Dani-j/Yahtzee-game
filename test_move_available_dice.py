from unittest import TestCase
from yahtzee import move_available_dice


class TestMoveAvailableDice(TestCase):

    def test_move_available_remove_all(self):
        dice_to_remove = ['3', '1', '2']
        dice_to_add = ['1', '2']
        input_dice = ["2", "3", "1"]
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2', '2', '3', '1'], [])
        self.assertEqual(expected, actual)

    def test_move_available_dice_remove_part(self):
        dice_to_remove = ['3', '3', '2']
        dice_to_add = ['1', '2']
        input_dice = ["3", "3"]
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2', '3', '3'], ['2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_remove_none(self):
        dice_to_remove = ['3', '6', '2']
        dice_to_add = ['1', '2']
        input_dice = []
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2'], ['3', '6', '2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_input_dice_extra_not_number(self):
        dice_to_remove = ['3', '4', '2']
        dice_to_add = ['1', '2']
        input_dice = ['3', '4', "j", "/", "@"]
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2', '3', '4'], ['2'])
        self.assertEqual(expected, actual)

    def test_move_available_dice_input_dice_extra_repeat_number(self):
        dice_to_remove = ['3', '5', '2']
        dice_to_add = ['1', '2']
        input_dice = ['3', '5', "2", "2", "2"]
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2', '3', '5', "2"], [])
        self.assertEqual(expected, actual)

    def test_move_available_dice_input_dice_extra_other_number(self):
        dice_to_remove = ['3', '5', '4']
        dice_to_add = ['1', '2']
        input_dice = ['3', '5', "2", "8", "9"]
        actual = move_available_dice(dice_to_remove, dice_to_add, input_dice)
        expected = (['1', '2', '3', '5'], ['4'])
        self.assertEqual(expected, actual)
