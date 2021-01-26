from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_row_options


@patch('sys.stdout', new_callable=io.StringIO)
class TestPrintRowOptions(TestCase):

    def test_print_row_options_no_score(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0}}
        available_options = {1: "Ones", 2: "Twos", 3: "Three of a kind", 4: "Four of a kind"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;32m(1) - Ones\033[0m\n' \
                   '\033[1;32m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;32m(3) - Three of a kind\033[0m\n' \
                   '\033[1;32m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_a_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0}}
        available_options = {2: "Twos", 3: "Three of a kind", 4: "Four of a kind"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;37m(1) - Ones\033[0m\n' \
                   '\033[1;32m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;32m(3) - Three of a kind\033[0m\n' \
                   '\033[1;32m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_all_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": 1},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1}}
        available_options = {3: "Three of a kind", 4: "Four of a kind"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;37m(1) - Ones\033[0m\n' \
                   '\033[1;37m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;32m(3) - Three of a kind\033[0m\n' \
                   '\033[1;32m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_a_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1}}
        available_options = {1: "Ones", 2: "Twos", 4: "Four of a kind"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;32m(1) - Ones\033[0m\n' \
                   '\033[1;32m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;37m(3) - Three of a kind\033[0m\n' \
                   '\033[1;32m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_all_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1},
                      "LOWER SECTION": {"Three of a kind": 14, "Four of a kind": 19}}
        available_options = {1: "Ones", 2: "Twos"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;32m(1) - Ones\033[0m\n' \
                   '\033[1;32m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;37m(3) - Three of a kind\033[0m\n' \
                   '\033[1;37m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_a_score_upper_a_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": 6},
                      "LOWER SECTION": {"Three of a kind": 11, "Four of a kind": -1}}
        available_options = {1: "Ones", 3: "Three of a kind"}
        print_row_options(available_options, score_card)
        expected = '---------------------\nUPPER SECTION\n---------------------\n\033[1;32m(1) - Ones\033[0m\n' \
                   '\033[1;37m(2) - Twos\033[0m\n---------------------\nLOWER SECTION\n' \
                   '---------------------\n\033[1;37m(3) - Three of a kind\033[0m\n' \
                   '\033[1;32m(4) - Four of a kind\033[0m\n\n'
        self.assertEqual(expected, mock_stdout.getvalue())
