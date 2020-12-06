from unittest import TestCase
from yahtzee import main_menu
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class Test(TestCase):

    def test_main_menu_unavailable_choice_empty(self, mock_stdout):
        unavailable_choice = []
        main_menu(unavailable_choice)
        expected = "What do you want to do?\n" \
                   "\033[1;32m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Move the dice\033[0m\n" \
                   "\033[1;32m(3) - Roll the dice (2/3)\033[0m\n" \
                   "\033[1;32m(4) - check score card\033[0m\n" \
                   "\033[1;32m(5) - write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_menu_unavailable_choice_1(self, mock_stdout):
        unavailable_choice = [1]
        main_menu(unavailable_choice)
        expected = "What do you want to do?\n" \
                   "\033[1;37m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Move the dice\033[0m\n" \
                   "\033[1;32m(3) - Roll the dice (2/3)\033[0m\n" \
                   "\033[1;32m(4) - check score card\033[0m\n" \
                   "\033[1;32m(5) - write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_menu_unavailable_choice_3(self, mock_stdout):
        unavailable_choice = [3]
        main_menu(unavailable_choice)
        expected = "What do you want to do?\n" \
                   "\033[1;32m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Move the dice\033[0m\n" \
                   "\033[1;37m(3) - Roll the dice (2/3)\033[0m\n" \
                   "\033[1;32m(4) - check score card\033[0m\n" \
                   "\033[1;32m(5) - write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_main_unavailable_choice_1_3(self, mock_stdout):
        unavailable_choice = [1, 3]
        main_menu(unavailable_choice)
        expected = "What do you want to do?\n" \
                   "\033[1;37m(1) - Keep the dice\033[0m\n" \
                   "\033[1;32m(2) - Move the dice\033[0m\n" \
                   "\033[1;37m(3) - Roll the dice (2/3)\033[0m\n" \
                   "\033[1;32m(4) - check score card\033[0m\n" \
                   "\033[1;32m(5) - write score\033[0m\n"
        self.assertEqual(expected, mock_stdout.getvalue())
