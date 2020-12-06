from unittest import TestCase
from unittest.mock import patch
from yahtzee import set_players


class Test(TestCase):
    """
    Because I plan to use SCORE_CARD() as the score_card in set_players(), all the score_card in the unit test
    are same.
    """
    @patch('builtins.input', side_effect=['Dani', 'Joe'])
    def test_set_players_input_letters(self, mock_input):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                                        "TOTAL": "", "Bonus": "", "TOTAL_": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "Full House": "",
                                        "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "",
                                        "TOTAL": "", "GRANT TOTAL": ""}}
        actual = set_players(score_card)
        expected = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                              'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                              'TOTAL_': ''},
                                            'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                              'Full House': '', 'Small Straight': '',
                                                              'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                              'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []},
                    'Joe': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                             'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                             'TOTAL_': ''},
                                           'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                             'Full House': '', 'Small Straight': '',
                                                             'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                             'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[';/', '][=-'])
    def test_set_players_input_symbol(self, mock_input):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                                        "TOTAL": "", "Bonus": "", "TOTAL_": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "Full House": "",
                                        "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "",
                                        "TOTAL": "", "GRANT TOTAL": ""}}
        actual = set_players(score_card)
        expected = {';/': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                              'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                              'TOTAL_': ''},
                                            'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                              'Full House': '', 'Small Straight': '',
                                                              'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                              'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []},
                    '][=-': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                             'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                             'TOTAL_': ''},
                                           'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                             'Full House': '', 'Small Straight': '',
                                                             'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                             'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2435', '8356231'])
    def test_set_players_input_numbers(self, mock_input):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                                        "TOTAL": "", "Bonus": "", "TOTAL_": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "Full House": "",
                                        "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "",
                                        "TOTAL": "", "GRANT TOTAL": ""}}
        actual = set_players(score_card)
        expected = {'2435': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                              'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                              'TOTAL_': ''},
                                            'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                              'Full House': '', 'Small Straight': '',
                                                              'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                              'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []},
                    '8356231': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                             'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                             'TOTAL_': ''},
                                           'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                             'Full House': '', 'Small Straight': '',
                                                             'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                             'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []}}
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['    ', '       '])
    def test_set_players_input_space(self, mock_input):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "Threes": "", "Fours": "", "Fives": "", "Sixes": "",
                                        "TOTAL": "", "Bonus": "", "TOTAL_": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "Full House": "",
                                        "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "",
                                        "TOTAL": "", "GRANT TOTAL": ""}}
        actual = set_players(score_card)
        expected = {'    ': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                              'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                              'TOTAL_': ''},
                                            'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                              'Full House': '', 'Small Straight': '',
                                                              'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                              'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []},
                    '       ': {'score_card': {'UPPER SECTION': {'Ones': '', 'Twos': '', 'Threes': '', 'Fours': '',
                                                             'Fives': '', 'Sixes': '', 'TOTAL': '', 'Bonus': '',
                                                             'TOTAL_': ''},
                                           'LOWER SECTION': {'Three of a kind': '', 'Four of a kind': '',
                                                             'Full House': '', 'Small Straight': '',
                                                             'Large straight': '', 'Chance': '', 'YAHTZEE': '',
                                                             'TOTAL': '', 'GRANT TOTAL': ''}}, 'dice': []}}
        self.assertEqual(expected, actual)
