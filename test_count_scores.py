from unittest import TestCase
from yahtzee import count_scores


class TestCountScores(TestCase):

    def test_count_scores_ones_get_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_row = (1, "Ones")
        dice = ["1", "1", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (2, "Ones")
        self.assertEqual(actual, expected)

    def test_count_scores_ones_not_valid_zero_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_row = (1, "Ones")
        dice = ["3", "3", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Ones")
        self.assertEqual(actual, expected)

    def test_count_scores_twos_get_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_row = (2, "Twos")
        dice = ["1", "2", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (2, "Twos")
        self.assertEqual(actual, expected)

    def test_count_scores_twos_not_valid_zero_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
        write_row = (2, "Twos")
        dice = ["1", "1", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Twos")
        self.assertEqual(actual, expected)

    def test_count_scores_fours_get_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (4, "Fours")
        dice = ["1", "1", "4", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (8, "Fours")
        self.assertEqual(actual, expected)

    def test_count_scores_fours_not_valid_zero_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (4, "Fours")
        dice = ["1", "1", "2", "2", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Fours")
        self.assertEqual(actual, expected)

    def test_count_scores_sixes_get_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (6, "Sixes")
        dice = ["1", "1", "6", "6", "6"]
        actual = count_scores(score_card, write_row, dice)
        expected = (18, "Sixes")
        self.assertEqual(actual, expected)

    def test_count_scores_sixes_not_valid_zero_points(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (6, "Sixes")
        dice = ["1", "1", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Sixes")
        self.assertEqual(actual, expected)

    def test_count_scores_three_of_a_kind_3_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (7, "Three of a kind")
        dice = ["1", "1", "1", "3", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (11, "Three of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_three_of_a_kind_4_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (7, "Three of a kind")
        dice = ["1", "1", "1", "1", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (9, "Three of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_three_of_a_kind_5_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (7, "Three of a kind")
        dice = ["1", "1", "1", "1", "1"]
        actual = count_scores(score_card, write_row, dice)
        expected = (5, "Three of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_three_of_a_invalid(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (7, "Three of a kind")
        dice = ["1", "1", "2", "3", "4"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Three of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_four_of_a_kind_4_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (8, "Four of a kind")
        dice = ["1", "1", "1", "1", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (9, "Four of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_four_of_a_kind_5_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (8, "Four of a kind")
        dice = ["4", "4", "4", "4", "4"]
        actual = count_scores(score_card, write_row, dice)
        expected = (20, "Four of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_four_of_a_kind_invalid(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (8, "Four of a kind")
        dice = ["4", "4", "5", "5", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Four of a kind")
        self.assertEqual(actual, expected)

    def test_count_scores_full_house_3_repeat_numbers_2_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (9, "Full House")
        dice = ["1", "1", "1", "3", "3"]
        actual = count_scores(score_card, write_row, dice)
        expected = (25, "Full House")
        self.assertEqual(actual, expected)

    def test_count_scores_full_house_5_repeat_numbers(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (9, "Full House")
        dice = ["1", "1", "1", "1", "1"]
        actual = count_scores(score_card, write_row, dice)
        expected = (25, "Full House")
        self.assertEqual(actual, expected)

    def test_count_scores_full_house_invalid(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (9, "Full House")
        dice = ["1", "2", "3", "4", "4"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "Full House")
        self.assertEqual(actual, expected)

    def test_count_scores_small_straight_1234_repeat_number_at_the_end(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (10, "Small Straight")
        dice = ["1", "2", "3", "4", "4"]
        actual = count_scores(score_card, write_row, dice)
        expected = (30, "Small Straight")
        self.assertEqual(actual, expected)

    def test_count_scores_small_straight_1234_repeat_number_in_middle(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (10, "Small Straight")
        dice = ["1", "2", "2", "3", "4"]
        actual = count_scores(score_card, write_row, dice)
        expected = (30, "Small Straight")
        self.assertEqual(actual, expected)

    def test_count_scores_small_straight_2345(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (10, "Small Straight")
        dice = ["2", "2", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (30, "Small Straight")
        self.assertEqual(actual, expected)

    def test_count_scores_small_straight_3456(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (10, "Small Straight")
        dice = ["3", "4", "4", "5", "6"]
        actual = count_scores(score_card, write_row, dice)
        expected = (30, "Small Straight")
        self.assertEqual(actual, expected)

    def test_count_scores_large_straight_12345(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (11, "Large straight")
        dice = ["1", "2", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (40, "Large straight")
        self.assertEqual(actual, expected)

    def test_count_scores_large_straight_23456(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (11, "Large straight")
        dice = ["2", "3", "4", "5", "6"]
        actual = count_scores(score_card, write_row, dice)
        expected = (40, "Large straight")
        self.assertEqual(actual, expected)

    def test_count_scores_chance(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (12, "Chance")
        dice = ["1", "1", "3", "4", "5"]
        actual = count_scores(score_card, write_row, dice)
        expected = (14, "Chance")
        self.assertEqual(actual, expected)

    def test_count_scores_yahtzee_first_write(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (13, "YAHTZEE")
        dice = ["1", "1", "1", "1", "1"]
        actual = count_scores(score_card, write_row, dice)
        expected = (50, "YAHTZEE")
        self.assertEqual(actual, expected)

    def test_count_scores_yahtzee_second_write(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": 50,
                                        "TOTAL": 50, "GRANT TOTAL": 50}}
        write_row = (13, "YAHTZEE")
        dice = ["1", "1", "1", "1", "1"]
        actual = count_scores(score_card, write_row, dice)
        expected = (100, "YAHTZEE")
        self.assertEqual(actual, expected)

    def test_count_scores_yahtzee_third_write(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": 150,
                                        "TOTAL": 150, "GRANT TOTAL": 150}}
        write_row = (13, "YAHTZEE")
        dice = ["1", "1", "1", "1", "1"]
        actual = count_scores(score_card, write_row, dice)
        expected = (100, "YAHTZEE")
        self.assertEqual(actual, expected)

    def test_count_scores_yahtzee_invalid(self):
        score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                                        "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
                      "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                                        "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                                        "TOTAL": 0, "GRANT TOTAL": 0}}
        write_row = (13, "YAHTZEE")
        dice = ["1", "1", "1", "1", "2"]
        actual = count_scores(score_card, write_row, dice)
        expected = (0, "YAHTZEE")
        self.assertEqual(actual, expected)
