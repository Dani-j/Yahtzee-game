from unittest import TestCase
from yahtzee import winner


class Test(TestCase):

    def test_winner_the_second_player_win(self):
        two_players = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '1', 'TOTAL': '1'},
                                               'LOWER SECTION': {'Three of a kind': '14', 'Four of a kind': '16',
                                                                 'YAHTZEE': '0', 'TOTAL': '30', 'GRANT TOTAL': '31'}},
                                'dice': []},
                       'Joe': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                                              'LOWER SECTION': {'Three of a kind': '0', 'Four of a kind': '0',
                                                                'YAHTZEE': '50', 'TOTAL': '50', 'GRANT TOTAL': '53'}},
                               'dice': []}}
        actual = winner(two_players)
        expected = "Joe"
        self.assertEqual(expected, actual)

    def test_winner_the_first_player_win(self):
        two_players = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '1', 'TOTAL': '1'},
                                               'LOWER SECTION': {'Three of a kind': '14', 'Four of a kind': '16',
                                                                 'YAHTZEE': '50', 'TOTAL': '80', 'GRANT TOTAL': '81'}},
                                'dice': []},
                       'Joe': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                                              'LOWER SECTION': {'Three of a kind': '0', 'Four of a kind': '0',
                                                                'YAHTZEE': '0', 'TOTAL': '0', 'GRANT TOTAL': '3'}},
                               'dice': []}}
        actual = winner(two_players)
        expected = "Dani"
        self.assertEqual(expected, actual)

    def test_winner_the_draw(self):
        two_players = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                                               'LOWER SECTION': {'Three of a kind': '14', 'Four of a kind': '16',
                                                                 'YAHTZEE': '50', 'TOTAL': '80', 'GRANT TOTAL': '83'}},
                                'dice': []},
                       'Joe': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
                                              'LOWER SECTION': {'Three of a kind': '0', 'Four of a kind': '30',
                                                                'YAHTZEE': '50', 'TOTAL': '80', 'GRANT TOTAL': '83'}},
                               'dice': []}}
        actual = winner(two_players)
        expected = "Dani & Joe"
        self.assertEqual(expected, actual)
