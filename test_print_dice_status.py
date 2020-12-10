from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_dice_status


@patch('sys.stdout', new_callable=io.StringIO)
class TestPrintDiceStatus(TestCase):

    def test_print_dice_status_table_dice_length_0_kept_dice_length_5(self, mock_stdout):
        table_dice = []
        kept_dice = ["1", "2", "3", "5", "6"]
        print_dice_status(table_dice, kept_dice)
        expected = "Dice on the table: \033[1;32m[]\033[0m\nDice on hand: \033[1;34m['1', '2', '3', '5', '6']\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_dice_status_table_dice_length_1_kept_dice_length_4(self, mock_stdout):
        table_dice = ["1"]
        kept_dice = ["1", "2", "3", "5"]
        print_dice_status(table_dice, kept_dice)
        expected = "Dice on the table: \033[1;32m['1']\033[0m\nDice on hand: \033[1;34m['1', '2', '3', '5']\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_dice_status_table_dice_length_2_kept_dice_length_3(self, mock_stdout):
        table_dice = ["2", "6"]
        kept_dice = ["1", "2" "6"]
        print_dice_status(table_dice, kept_dice)
        expected = "Dice on the table: \033[1;32m['2', '6']\033[0m\nDice on hand: \033[1;34m['1', '2', '6']\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_dice_status_table_dice_length_3_kept_dice_length_2(self, mock_stdout):
        table_dice = ["2", "3", "3",]
        kept_dice = ["1", "2"]
        print_dice_status(table_dice, kept_dice)
        expected = "Dice on the table: \033[1;32m['2', '3', '3']\033[0m\nDice on hand: \033[1;34m['1', '2']\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_dice_status_table_dice_length_4_kept_dice_length_1(self, mock_stdout):
        table_dice = ["1", "4", "3", "5"]
        kept_dice = ["4"]
        print_dice_status(table_dice, kept_dice)
        expected = "Dice on the table: \033[1;32m['1', '4', '3', '5']\033[0m\nDice on hand: \033[1;34m['4']\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())
