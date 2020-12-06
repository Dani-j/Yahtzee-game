from unittest import TestCase
from yahtzee import write_scores_engine


class Test(TestCase):
    
    def test_write_scores_engine_write_score_upper(self):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": "", "Bonus": "", 'TOTAL_': ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": ""}}
        write_row = "A"
        dice = ["1", "2", "3", "4", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1"},
                    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_zero_0(self):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": ""}}
        write_row = "A"
        dice = ["1", "2", "3", "4", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1"},
                    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
        self.assertEqual(expected, actual)
        
    def test_write_scores_engine_all(self):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": ""}}
        write_row = "A"
        dice = ["1", "2", "3", "4", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": ""},
                    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": ""}}
        self.assertEqual(expected, actual)