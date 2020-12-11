from unittest import TestCase
from yahtzee import main_menu
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class TestMainMenu(TestCase):

    def test_main_menu_available_option_all(self, mock_stdout):
        available_options = {"1", "2", "3", "4", "5"}
        dice_time = 1
        main_menu(available_options, dice_time)
        expected = "Please choose one of the option (in green) below，must write the score before " \
                   "the next player play\n" \
                   "\033[1;32m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Remove the dice\033[0m\n" \
                   "\033[1;32m(3) - Roll the dice (1/3)\033[0m\n" \
                   "\033[1;32m(4) - Check score card\033[0m\n" \
                   "\033[1;32m(5) - Write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_menu_available_options_all_dice_time_2(self, mock_stdout):
        available_options = {"1", "2", "3", "4", "5"}
        dice_time = 2
        main_menu(available_options, dice_time)
        expected = "Please choose one of the option (in green) below，must write the score before " \
                   "the next player play\n" \
                   "\033[1;32m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Remove the dice\033[0m\n" \
                   "\033[1;32m(3) - Roll the dice (2/3)\033[0m\n" \
                   "\033[1;32m(4) - Check score card\033[0m\n" \
                   "\033[1;32m(5) - Write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_menu_available_options_not_3_dice_time_0(self, mock_stdout):
        available_options = {"1", "2", "4", "5"}
        dice_time = 0
        main_menu(available_options, dice_time)
        expected = "Please choose one of the option (in green) below，must write the score before " \
                   "the next player play\n" \
                   "\033[1;32m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Remove the dice\033[0m\n" \
                   "\033[1;37m(3) - Roll the dice (0/3)\033[0m\n" \
                   "\033[1;32m(4) - Check score card\033[0m\n" \
                   "\033[1;32m(5) - Write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_available_options_not_1_3_dice_time_0(self, mock_stdout):
        available_options = {"2", "4", "5"}
        dice_time = 0
        main_menu(available_options, dice_time)
        expected = "Please choose one of the option (in green) below，must write the score before " \
                   "the next player play\n" \
                   "\033[1;37m(1) - Keep the dice (NO DICE on table!)\033[0m\n" \
                   "\033[1;32m(2) - Remove the dice\033[0m\n" \
                   "\033[1;37m(3) - Roll the dice (0/3)\033[0m\n" \
                   "\033[1;32m(4) - Check score card\033[0m\n" \
                   "\033[1;32m(5) - Write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_available_options_not_1_3_dice_time_1(self, mock_stdout):
        available_options = {"2", "4", "5"}
        dice_time = 1
        main_menu(available_options, dice_time)
        expected = "Please choose one of the option (in green) below，must write the score before " \
                   "the next player play\n" \
                   "\033[1;37m(1) - Keep the dice (NO DICE on table!)\033[0m\n" \
                   "\033[1;32m(2) - Remove the dice\033[0m\n" \
                   "\033[1;37m(3) - Roll the dice (1/3)\033[0m\n" \
                   "\033[1;32m(4) - Check score card\033[0m\n" \
                   "\033[1;32m(5) - Write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())