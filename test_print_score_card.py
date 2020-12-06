from unittest import TestCase
from yahtzee import print_score_card
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class Test(TestCase):
    """
    Parameter player is test in the test_set_players, so it is not tested here"
    """

    def test_print_score_card_no_score(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes                 ' \
                   'Twos                 ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind      ' \
                   'Four of a kind       \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes              1  ' \
                   'Twos                 ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind      ' \
                   'Four of a kind       \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "2"},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes              1  ' \
                   'Twos              2  ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind      ' \
                   'Four of a kind       \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": ""}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes                 ' \
                   'Twos                 ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind   12 ' \
                   'Four of a kind       \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "14", "Four of a kind": "19"}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes                 ' \
                   'Twos                 ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind   14 ' \
                   'Four of a kind    19 \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_upper_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "4"},
                      "LOWER SECTION": {"Three of a kind": "13", "Four of a kind": "22"}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes              1  ' \
                   'Twos              4  ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind   13 ' \
                   'Four of a kind    22 \n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_upper_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "6"},
                      "LOWER SECTION": {"Three of a kind": "11", "Four of a kind": ""}}
        player = "Dani"
        print_score_card(score_card, player)
        expected = '---------------------\n    UPPER SECTION    \n---------------------\nOnes                 ' \
                   'Twos              6  ' \
                   '---------------------\n    LOWER SECTION    \n---------------------\nThree of a kind   11 ' \
                   'Four of a kind       \n'
        self.assertEqual(expected, mock_stdout.getvalue())


