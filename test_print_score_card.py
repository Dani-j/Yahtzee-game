from unittest import TestCase
from yahtzee import print_score_card
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class TestPrintScoreCard(TestCase):

    def test_print_score_card_no_score(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Player One"
        print_score_card(player, score_card)
        expected = "\nPlayer One's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                        \nTwos                        \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind             \nFour of a kind              \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_in_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Player Two"
        print_score_card(player, score_card)
        expected = "\nPlayer Two's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                 1      \nTwos                        \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind             \nFour of a kind              \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_in_upper_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "2"},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": ""}}
        player = "Player Two"
        print_score_card(player, score_card)
        expected = "\nPlayer Two's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                 1      \nTwos                 2      \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind             \nFour of a kind              \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_in_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": ""}}
        player = "Player Two"
        print_score_card(player, score_card)
        expected = "\nPlayer Two's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                        \nTwos                        \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind      12     \nFour of a kind              \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_in_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": ""},
                      "LOWER SECTION": {"Three of a kind": "14", "Four of a kind": "19"}}
        player = "Player Two"
        print_score_card(player, score_card)
        expected = "\nPlayer Two's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                        \nTwos                        \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind      14     \nFour of a kind       19     \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_all_score_in_upper_and_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "4"},
                      "LOWER SECTION": {"Three of a kind": "13", "Four of a kind": "22"}}
        player = "Player Two"
        print_score_card(player, score_card)
        expected = "\nPlayer Two's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                 1      \nTwos                 4      \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind      13     \nFour of a kind       22     \n"
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_print_score_card_a_score_upper_lower_section(self, mock_stdout):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "6"},
                      "LOWER SECTION": {"Three of a kind": "11", "Four of a kind": ""}}
        player = "Player One"
        print_score_card(player, score_card)
        expected = "\nPlayer One's score card:\n" \
                   "----------------------------\n       UPPER SECTION        \n----------------------------\n" \
                   "Ones                        \nTwos                 6      \n" \
                   "----------------------------\n       LOWER SECTION        \n----------------------------\n" \
                   "Three of a kind      11     \nFour of a kind              \n"
        self.assertEqual(expected, mock_stdout.getvalue())
