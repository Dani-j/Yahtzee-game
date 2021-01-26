from unittest import TestCase
from yahtzee import winner
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class TestWinner(TestCase):

    def test_winner_the_second_player_win(self, mock_stdout):
        player_1_score_card = {'UPPER SECTION': {'Ones': 1, 'TOTAL': 1},
                               'LOWER SECTION': {'Three of a kind': 14, 'Four of a kind': 16,
                                                 'YAHTZEE': 0, 'TOTAL': 30, 'GRANT TOTAL': 31}}
        player_2_score_card = {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                               'LOWER SECTION': {'Three of a kind': 0, 'Four of a kind': 0,
                                                 'YAHTZEE': 50, 'TOTAL': 50, 'GRANT TOTAL': 53}}
        winner(player_1_score_card, player_2_score_card)
        expected ='Congrats, player two. You win!\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_winner_the_first_player_win(self, mock_stdout):
        player_1_score_card = {'UPPER SECTION': {'Ones': 1, 'TOTAL': 1},
                               'LOWER SECTION': {'Three of a kind': 14, 'Four of a kind': 16,
                                                 'YAHTZEE': 150, 'TOTAL': 180, 'GRANT TOTAL': 181}}
        player_2_score_card = {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                               'LOWER SECTION': {'Three of a kind': 0, 'Four of a kind': 0,
                                                 'YAHTZEE': 50, 'TOTAL': 50, 'GRANT TOTAL': 53}}
        winner(player_1_score_card, player_2_score_card)
        expected = 'Congrats, player one. You win!\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    def test_winner_the_draw(self, mock_stdout):
        player_1_score_card = {'UPPER SECTION': {'Ones': 3, 'TOTAL': 3},
                               'LOWER SECTION': {'Three of a kind': 14, 'Four of a kind': 16,
                                                 'YAHTZEE': 50, 'TOTAL': 80, 'GRANT TOTAL': 83}}
        player_2_score_card = {'UPPER SECTION': {'Ones': 3, 'TOTAL': 3},
                               'LOWER SECTION': {'Three of a kind': 0, 'Four of a kind': 30,
                                                 'YAHTZEE': 50, 'TOTAL': 80, 'GRANT TOTAL': 83}}
        winner(player_1_score_card, player_2_score_card)
        expected = 'Congrats. You both win!\n'
        self.assertEqual(expected, mock_stdout.getvalue())
