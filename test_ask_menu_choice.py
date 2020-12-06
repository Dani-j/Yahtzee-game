from unittest import TestCase
from unittest.mock import patch
from yahtzee import ask_menu_choice


class Test(TestCase):
    """
    The player name (parameter player) is tested in the test_set_players, and the dice_time in the parameter
    unavailable_option is not used in this function, so no test for them in there.
    """
    @patch('builtins.input', side_effect=['1'])
    def test_ask_menu_choice_unavailable_option_none_input_1(self, mock_input):
        player = "Dani"
        unavailable_options = ([], 2)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "1"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_ask_menu_choice_unavailable_option_none_input_5(self, mock_input):
        player = "Dani"
        unavailable_options = ([], 2)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "5"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_ask_menu_choice_unavailable_option_none_input_2(self, mock_input):
        player = "Dani"
        unavailable_options = ([], 2)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "2"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_ask_menu_choice_unavailable_option_1_input_1(self, mock_input):
        player = "Dani"
        unavailable_options = ([1], 1)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "Please choose the available option number (color green)."
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_ask_menu_choice_unavailable_option_1_input_4(self, mock_input):
        player = "Dani"
        unavailable_options = ([1], 1)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "4"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_ask_menu_choice_unavailable_option_1_3_input_1(self, mock_input):
        player = "Dani"
        unavailable_options = ([1, 3], 1)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "Please choose the available option number (color green)."
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_ask_menu_choice_unavailable_option_1_3_input_3(self, mock_input):
        player = "Dani"
        unavailable_options = ([1, 3], 1)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "Please choose the available option number (color green)."
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    def test_ask_menu_choice_unavailable_option_1_3_input_5(self, mock_input):
        player = "Dani"
        unavailable_options = ([1, 3], 1)
        actual = ask_menu_choice(player, unavailable_options)
        expected = "5"
        self.assertEqual(expected, actual)
