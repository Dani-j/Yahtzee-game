from unittest import TestCase
from yahtzee import available_row


class TestAvailableRow(TestCase):

    def test_available_row_all_available(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        dice = ["1", "2", "3", "4", "5"]
        actual = available_row(score_card, dice)
        expected = {1: "Ones", 2: "Twos", 3: "Three of a kind", 4: "YAHTZEE"}
        self.assertEqual(actual, expected)

    def test_available_row_part_available_in_upper_section(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": 2, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        dice = ["1", "2", "3", "4", "5"]
        actual = available_row(score_card, dice)
        expected = {1: "Ones", 3: "Three of a kind", 4: "YAHTZEE"}
        self.assertEqual(actual, expected)

    def test_available_row_part_available_in_lower_section(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": 7, "YAHTZEE": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        dice = ["1", "2", "3", "4", "5"]
        actual = available_row(score_card, dice)
        expected = {1: "Ones", 2: "Twos", 4: "YAHTZEE"}
        self.assertEqual(actual, expected)

    def test_available_row_yahtzee_0_point(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": 0, "TOTAL": 0, "GRANT_TOTAL": 0}}
        dice = ["1", "2", "3", "4", "5"]
        actual = available_row(score_card, dice)
        expected = {1: "Ones", 2: "Twos", 3: "Three of a kind"}
        self.assertEqual(actual, expected)

    def test_available_row_yahtzee_not_valid_dice(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": 50, "TOTAL": 0, "GRANT_TOTAL": 0}}
        dice = ["1", "2", "3", "4", "5"]
        actual = available_row(score_card, dice)
        expected = {1: "Ones", 2: "Twos", 3: "Three of a kind"}
        self.assertEqual(actual, expected)
