from unittest import TestCase
from yahtzee import update_score_card


class TestUpdateScoreCard(TestCase):

    def test_update_score_card_write_one_score_upper(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_score_row = (1, "Ones")
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, "TOTAL_": 1},
                    "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 1}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_all_score_upper(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_score_row = (2, "Twos")
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": 2, "TOTAL": 3, "Bonus": 0, 'TOTAL_': 3},
                    "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 3}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_one_score_lower(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_score_row = (12, "Three of a kind")
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, "TOTAL": 12, "GRANT_TOTAL": 13}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_all_score_lower(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, "TOTAL": 12, "GRANT_TOTAL": 13}}
        write_score_row = (13, "Four of a kind")
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": 13, "TOTAL": 25, "GRANT_TOTAL": 26}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_bonus(self):
        score_card = {"UPPER SECTION": {'Ones': 3, 'Twos': 10, 'Threes': 9, 'Fours': 16,
                                        'Fives': 20, 'Sixes': -1, 'TOTAL': 58, 'Bonus': 0, 'TOTAL_': 58},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, "TOTAL": 12,
                                        "GRANT_TOTAL": 70}}
        write_score_row = (18, 'Sixes')
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {'Ones': 3, 'Twos': 10, 'Threes': 9, 'Fours': 16,
                                      'Fives': 20, 'Sixes': 18, 'TOTAL': 76, 'Bonus': 35, 'TOTAL_': 111},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, "TOTAL": 12,
                                      "GRANT_TOTAL": 123}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_first_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': -1,
                                        "TOTAL": 12, "GRANT_TOTAL": 13}}
        write_score_row = (50, 'YAHTZEE')
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': 50,
                                      "TOTAL": 62, "GRANT_TOTAL": 63}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_second_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': 50,
                                        "TOTAL": 62, "GRANT_TOTAL": 63}}
        write_score_row = (100, 'YAHTZEE')
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': 150,
                                      "TOTAL": 162, "GRANT_TOTAL": 163}}
        self.assertEqual(expected, actual)

    def test_update_score_card_write_forth_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                      "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': 250,
                                        "TOTAL": 262, "GRANT_TOTAL": 263}}
        write_score_row = (100, 'YAHTZEE')
        actual = update_score_card(score_card, write_score_row)
        expected = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": 1, "Bonus": 0, 'TOTAL_': 1},
                    "LOWER SECTION": {"Three of a kind": 12, "Four of a kind": -1, 'YAHTZEE': 350,
                                      "TOTAL": 362, "GRANT_TOTAL": 363}}
        self.assertEqual(expected, actual)
