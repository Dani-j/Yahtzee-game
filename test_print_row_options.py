from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_row_options


@patch('sys.stdout', new_callable=io.StringIO)
class TestPrintRowOptions(TestCase):
    
    def test_print_row_options_no_score(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": ""}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n(A) - Ones           ' \
                   '(B) - Twos           ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n(C) - Three of a kind' \
                   '(D) - Four of a kind \n'
        self.assertEqual(expected, mock_stdout.getvalue())
        
    def test_print_row_options_a_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": ""}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '\033[1;32m(A) - Ones           \033[0m' \
                   '(B) - Twos           ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n(C) - Three of a kind' \
                   '(D) - Four of a kind \n'
        self.assertEqual(expected, mock_stdout.getvalue())
        
    def test_print_row_options_all_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "2"},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '\033[1;32m(A) - Ones           \033[0m' \
                   '\033[1;32m(B) - Twos           \033[0m' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n(C) - Three of a kind' \
                   '(D) - Four of a kind \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_a_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": ""}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '(A) - Ones           ' \
                   '(B) - Twos           ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n' \
                   '\033[1;32m(C) - Three of a kind\033[0m' \
                   '(D) - Four of a kind \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_all_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "14", "Four of a kind": "19"}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '(A) - Ones           ' \
                   '(B) - Twos           ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n' \
                   '\033[1;32m(C) - Three of a kind\033[0m' \
                   '\033[1;32m(D) - Four of a kind \033[0m\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_all_score_upper_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "4"},
                      "LOWER SECTION": {"Three of a kind": "13", "Four of a kind": "22"}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '\033[1;32m(A) - Ones           \033[0m' \
                   '\033[1;32m(B) - Twos           \033[0m' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n' \
                   '\033[1;32m(C) - Three of a kind\033[0m' \
                   '\033[1;32m(D) - Four of a kind \033[0m\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_row_options_a_score_upper_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "6"},
                      "LOWER SECTION": {"Three of a kind": "11", "Four of a kind": ""}}
        print_row_options(score_card)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\n' \
                   '(A) - Ones           ' \
                   '\033[1;32m(B) - Twos           \033[0m' \
                   '---------------------\n    LOWER SECTION    \n---------------------\n' \
                   '\033[1;32m(C) - Three of a kind\033[0m' \
                   '(D) - Four of a kind \n'
        self.assertEqual(expected, mock_stdout.getvalue())
