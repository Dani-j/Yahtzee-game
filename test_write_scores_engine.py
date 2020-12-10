from unittest import TestCase
from yahtzee import write_scores_engine


class TestWriteScoresEngine(TestCase):
    
    def test_write_scores_engine_write_one_score_upper(self):
        score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": "", "Bonus": "", 'TOTAL_': ""},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": ""}}
        write_row = "A"
        dice = ["1", "2", "3", "4", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1"},
                    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_all_score_upper(self):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1", "Bonus": "", 'TOTAL_': "1"},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
        write_row = "B"
        dice = ["1", "2", "3", "4", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "2", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "3"},
                    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "3"}}
        self.assertEqual(expected, actual)
        
    def test_write_scores_engine_write_one_score_lower(self):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "2", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "3"},
                      "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "3"}}
        write_row = "C"
        dice = ["1", "2", "2", "2", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "2", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "3"},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", "TOTAL": "12",
                                      "GRANT_TOTAL": "15"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_all_score_lower(self):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "4", "TOTAL": "5", "Bonus": "0", 'TOTAL_': "5"},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", "TOTAL": "12",
                                        "GRANT_TOTAL": "17"}}
        write_row = "D"
        dice = ["2", "2", "2", "2", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "4", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "5"},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "13", "TOTAL": "25",
                                      "GRANT_TOTAL": "30"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_bonus(self):
        score_card = {"UPPER SECTION": {'Ones': '3', 'Twos': '10', 'Threes': '9', 'Fours': '16',
                                        'Fives': '20', 'Sixes': '', 'TOTAL': '58', 'Bonus': '', 'TOTAL_': '58'},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", "TOTAL": "12",
                                        "GRANT_TOTAL": "70"}}
        write_row = "F"
        dice = ["6", "6", "6", "2", "5"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {'Ones': '3', 'Twos': '10', 'Threes': '9', 'Fours': '16',
                                      'Fives': '20', 'Sixes': '18', 'TOTAL': '58', 'Bonus': '35', 'TOTAL_': '111'},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", "TOTAL": "12",
                                      "GRANT_TOTAL": "182"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_first_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "4", "TOTAL": "5", "Bonus": "0", 'TOTAL_': "5"},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", 'YAHTZEE': '', "TOTAL": "12",
                                        "GRANT_TOTAL": "17"}}
        write_row = "E"
        dice = ["2", "2", "2", "2", "2"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "4", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "5"},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "13", 'YAHTZEE': '50', "TOTAL": "75",
                                      "GRANT_TOTAL": "80"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_second_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": "2", "Twos": "4", "TOTAL": "6", "Bonus": "0", 'TOTAL_': "6"},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", 'YAHTZEE': '50', "TOTAL": "62",
                                        "GRANT_TOTAL": "68"}}
        write_row = "E"
        dice = ["3", "3", "3", "3", "3"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "2", "Twos": "4", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "6"},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "13", 'YAHTZEE': '150', "TOTAL": "175",
                                      "GRANT_TOTAL": "181"}}
        self.assertEqual(expected, actual)

    def test_write_scores_engine_write_forth_yahtzee(self):
        score_card = {"UPPER SECTION": {"Ones": "2", "Twos": "4", "TOTAL": "6", "Bonus": "0", 'TOTAL_': "6"},
                      "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "", 'YAHTZEE': '250', "TOTAL": "262",
                                        "GRANT_TOTAL": "268"}}
        write_row = "E"
        dice = ["6", "6", "6", "6", "6"]
        actual = write_scores_engine(score_card, write_row, dice)
        expected = {"UPPER SECTION": {"Ones": "1", "Twos": "4", "TOTAL": "3", "Bonus": "0", 'TOTAL_': "5"},
                    "LOWER SECTION": {"Three of a kind": "12", "Four of a kind": "13", 'YAHTZEE': '350', "TOTAL": "375",
                                      "GRANT_TOTAL": "380"}}
        self.assertEqual(expected, actual)
