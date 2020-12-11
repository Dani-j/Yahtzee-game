import doctest


def SCORE_CARD() -> dict:
    """
    Return the Yahtzee score card as a dictionary.

    -1 means there is no score for that row; the initial score of total, bonus are 0.

    :postcondition: return a dictionary has uppercase and lowercase for the keys, and dictionaries for the values.
        each dictionary has "row" as the keys, and the values are empty strings representing the score
    :return: a dictionary representing the score card
    """
    pass

def EMPETY_SCORE():
    """-1"""
    pass


def OPTION_UNAVAILABLE():
    """
    Print "Oops, option unavailable." when
    """
    pass


def FULL_HOUSE_POINTS():
    """25"""
    pass


def SMALL_STRAIGHT_POINTS():
    """30"""
    pass


def LARGE_STRAIGHT_POINTS():
    """40"""
    pass


def YAHTZEE_SCORE_POINTS():
    """50"""
    pass


def EXTRA_YAHTZEE_SCORE_POINTS():
    """100"""
    pass


def play_yahtzee():
    """
    Let user to play the yahtzee.

    This yahtzee game only allow two users to play.

    The game ends when both of the two players finish their score card.

    If only one of the player fills out all rows in the score card,
    the another play can play until fill out all their score card

    :postcondition: print the result of the Yahtzee game.
    """
    pass


def one_turn(player: str, score_card: dict) -> dict:
    """
    Let user play one round and update the score card.

    At the beginning of the
    In each turn, the player can have 5 options from main_menu.
    One turn ends when the players write the score.


    :param player: a string which is player's name
    :param score_card: a dictionary representing the yahtzee score card
    :precondition: all the above parameter conditions must be met
    :postcondition: update the score card and return it
    :return: a dictionary which is the updated score card
    """
    pass

def main_menu_unavailable_options(dice_time: int, kept_dice: list) -> tuple:
    """
    Checking the uavailable options and return it.

    1 representing the option "(1) - Keep the dice"
    3 representing the option "(3) - Roll the dice"

    :param dice_time: an integer in range [0, 2] representing the time left to dice
    :param kept_dice: a list containing the dice that is hold by the users
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple that the index 0 is a list containing the unavailable options in the main menu,
        index 1 is the left dice time
    :return: a tuple containing the unavailable options in the main menu and the left dice time.

    >>> test_dice_time = 2
    >>> test_kept_dice = []
    >>> main_menu_unavailable_options(test_dice_time, test_kept_dice)
    ([],2)
    >>> test_dice_time = 2
    >>> test_kept_dice = [1, 2, 3, 4, 5]
    >>> main_menu_unavailable_options(test_dice_time, test_kept_dice)
    ([1, 3], 2)
    """


def main_menu(unavailable_options: tuple):
    """
    Print the main menu formatted by the available_choice

    The color of available options are green (grey if unavailable).
    When the available_options = [] , all the functions will print like below in green color:

    What do you want to do?
    (1) - Keep the dice
    (2) - Move the dice
    (3) - Roll the dice (1/3)
    (4) - Check score card
    (5) - Write Score

    Option "(1) - Keep the dice" will turn gray if the unavailable_options [1, 3] (when the player has 5 dice on hand)
    Option "(3) - Roll the dice (0/3)" will turn gray if the available_options is [3] (run out of left dice time).
    Option "(3) - Roll the dice (0/3) !NO DICE" will turn gray if the available_options is [1, 3] (when the player has
    5 dice on hand).

    :param unavailable_options: a tuple of unavailable options in the main menu and left dice time
    :precondition: unavailable_options is a tuple that the index 0 is a list containing the unavailable options
        in the main menu, index 1 is the left dice time
    :postcondition: print the main menu in right color
    """
    pass


def ask_menu_choice(player: str, unavailable_options: tuple) -> str:
    """
    Ask the player's choice with making sure the choice made is available.

    :param player: a string representing the player's name.
    :param unavailable_options: a tuple containing unavailable choices in the main menu and the left dice time
    :precondition: all the above parameter conditions must be met
    :postcondition: return a string representing the player's choice, the string must in the available_options.
    :return: a string representing the player's choice
    """
    pass


def roll_dice(kept_dice: list) -> list:
    """
    Roll the dice and return the result and the kept_dice.

    :param kept_dice: a list representing the dice that is(are) kept by the player
    :precondition: kept_dice is a list no longer than 4
    :postcondition: return list whose length equals to 5 after add the length of kept_dice
    :return: a list representing the dice that are/is generated randomly
    """
    pass


def print_dice_status(table_dice: list, kept_dice: list):
    """
    Print the dice on table and the dice on hand.

    When table_dice = ['3', '1', '2'], dice on hand = ['1', '2'], will print:

    Dice on the table: ['3', '1', '2']
    Dice on hand: ['1', '2']

    The table_dice list will be in green color, the kept_dice will be in blue color.

    :param table_dice: a list of dice on table
    :param kept_dice: a list representing the dice that is(are) kept by the player
    :precondition: the total length of table_dice and table_dice is 5
    :postcondition: print the dice on table in green color and the dice on hand in blue color.
    """


def hold_dice(table_dice: list, kept_dice: list) -> tuple:
    """
    Let the player keep the dice.

    When the player does not enter anything, do not keep any new dice.

    :param table_dice: a list of dice on table that can be hold on hand
    :param kept_dice: a list representing the dice that is(are) kept by the player
    :precondition: all the above parameter conditions must be met
    :postcondition: return two list of dice, total length is 5
    :return: two lists, one contains the dice on table, another one contains the dice on hand
    """
    pass


def remove_dice(kept_dice: list, table_dice: list) -> tuple:
    """
    Let the player remove the dice.

    When the player does not enter anything, do not remove any more dice

    :param kept_dice: a list representing the dice that is(are) kept by the player that could be removed
    :param table_dice: a list of dice on table
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple containing two list of dice, total length is 5
    :return: a tuple containing two lists, index 0 contains the dice on hand, index 1 contains the dice on table
    """
    pass


def move_available_dice(table_dice: list, kept_dice: list, input_dice: list) -> tuple:
    """
    Diagnose the available input dice and move them/it either to table or the player's hand.

    This function will be used in remove_dice and hold_dice function
    because both of them have steps that move the available dice from one to another.

    For remove the card, just input table_dice as kept_dice, input kept_dice as table_dice.

    The dice always move from right to left (i.e. the left list in the tuple can only increase or not change,
    the right list can only decrease or not change)

    :param table_dice: a list of dice on table
    :param kept_dice: a list representing the dice that is(are) kept by the player
    :param input_dice: a list containing dice the player wants to hold/move, the elements in the list are in table_dice
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple containing two list of dice, one contains the dice on hand,
        another one contains the dice on the table
    :return: a tuple containing two lists

    >>> test_table_dice = ['3', '1', '2']
    >>> test_kept_dice = ['1', '2']
    >>> test_input_dice = ["2", "3", "1"]
    >>> move_available_dice(test_table_dice, test_kept_dice, test_input_dice)
    (['1', '2', '2', '3', '1'], [])
    >>> test_table_dice = ['3', '1', '2']
    >>> test_kept_dice = ['1', '2']
    >>> test_input_dice = ["1", "2"]
    >>> move_available_dice(test_kept_dice, test_table_dice, test_input_dice)
    (['3', '1', '2', '2', '1'], [])
    """
    pass


def print_score_card(score_card: dict, player: str):
    """
    Display the score card to the player.

    :param score_card: a dictionary
    :param player: a string representing the player's name
    :precondition: all the above parameter conditions must be met
    :postcondition: print a formated score card

    >>> test_score_card = {"UPPER SECTION": {"Ones": "3", "Twos": "", "Threes": "", "Fours": "", "Fives": "10",
"Sixes": "", "TOTAL": "", "Bonus": "", "TOTAL_": ""}, "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "",
"Full House": "25", "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "", "TOTAL": "",
"GRANT TOTAL": ""}}
    >>> test_player = "Dani"
    >>> print_score_card(test_score_card, test_player)
    Dani's score card:
    ------------------------------------
               UPPER SECTION
    ------------------------------------
    Ones                 3
    Twos
    Threes
    Fours
    Fives                10
    Sixes
    TOTAL
    Bonus
    TOTAL_
    ------------------------------------
               LOWER SECTION
    ------------------------------------
    Three of a kind
    Four of a kind
    Full House           25
    Small Straight
    Large straight
    Chance
    YAHTZEE
    TOTAL
    GRANT TOTAL
    """
    pass


def write_score(score_card: dict, kept_dice: list, table_dice: list) -> dict:
    """
    Write the score into the player's score card.

    In this function, score are updated in the helper function for an easier unit testing

    :param score_card: a dictionary, the key and values are all strings
    :param kept_dice: a list
    :param table_dice: a list
    :precondition: all the above parameter conditions must be met
    :postcondition: return the updated score card, which is a dictionary
    :return: a dictionary
    """
    pass


def print_row_options(score_card: dict) -> list:
    """
    Display the options of the available row to write the score and return the available rows.

    The color of available options are green. (grey if unavailable)

    if score_card = {"UPPER SECTION": {"Ones": "3", "Twos": "", "Threes": "", "Fours": "", "Fives": "10", "Sixes":
    "", "TOTAL": "", "Bonus": "", "TOTAL_": ""}, "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "",
    "Full House": "25", "Small Straight": "", "Large straight": "", "Chance": "", "YAHTZEE": "", "TOTAL": "",
    "GRANT TOTAL": ""}}

    the function will print like below:

    ---------------------
    UPPER SECTION
    ---------------------
    (A) - Ones
    (B) - Twos
    (C) - Threes
    (D) - Fours
    (E) - Fives
    (F) - Sixes
    ---------------------
    LOWER SECTION
    ---------------------
    (G) - Three of a kind
    (H) - Four of a kind
    (I) - Full House
    (J) - Small Straight
    (K) - Large straight
    (L) - Chance
    (M) - YAHTZEE

    While "(A) - Ones", "(F) - Sixes", and "(I) - Full House" are in grey color, others are in green color.

    :param score_card: a dictionary, the key and values are all strings
    :precondition: score_card is a dictionary has uppercase and lowercase for the keys, and dictionaries for the values
        each dictionary has "row" as the keys, and the values are empty strings representing the score
    :postcondition: return a list of letters representing the available row to add the score
    :return: a list containing the available row to add the score
    """
    pass


def choose_score_card_row(available_row_options: list) -> str:
    """
    Ask the player which row to write the score and return the chosen row.

    :param available_row_options: a list containing the available row to add the score
    :precondition:  available_row_options is a list of letters
    :postcondition: return a string, which is a letter in available_row_options
    :return: a string representing the row to write
    """
    pass


def write_scores_engine(score_card: dict, write_row: str, dice: list) -> dict:
    """
    Write the score into the player's score card.

    This function write the score into the chosen row write_row first based the dice, then update the total and bonus.

    :param score_card: a dictionary, the key and values are all strings
    :param write_row: a string representing the row to write
    :param dice: a list merged by table_dice and kept_dice, the length is 5
    :precondition: all the above parameter conditions must be met
    :postcondition: return a dictionary representing the score card that has been updated the scores
    :return: an dictionary which is the score card

    >>> test_score_card = {"UPPER SECTION": {"Ones": "", "Twos": "", "TOTAL": "", "Bonus": "", 'TOTAL_': ''},
"LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": ""}}
    >>> test_write_row = "A"
    >>> test_dice = ["1", "2", "3", "4", "5"]
    {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1", "Bonus": "", 'TOTAL_': '1'},
    "LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
    >>> test_score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1", "Bonus": "", 'TOTAL_': '1'},
"LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
    >>> test_write_row = "C"
    >>> test_dice = ["2", "2", "3", "4", "5"]
    {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1", "Bonus": "", 'TOTAL_': '1'},
    "LOWER SECTION": {"Three of a kind": "0", "Four of a kind": "", "TOTAL": "0", "GRANT_TOTAL": "1"}}
    >>> test_score_card = {"UPPER SECTION": {"Ones": "1", "Twos": "", "TOTAL": "1", "Bonus": "", 'TOTAL_': '1'},
"LOWER SECTION": {"Three of a kind": "", "Four of a kind": "", "TOTAL": "", "GRANT_TOTAL": "1"}}
    >>> test_write_row = "B"
    >>> test_dice = ["2", "2", "2", "2", "5"]
    {"UPPER SECTION": {"Ones": "1", "Twos": "8", "TOTAL": "1", "Bonus": "0", 'TOTAL_': '9'},
    "LOWER SECTION": {"Three of a kind": "0", "Four of a kind": "", "TOTAL": "0", "GRANT_TOTAL": "9"}}
    """
    pass


def winner(two_players: dict) -> str:
    """
    Compare the grand total scores between two players and find the winner.

    :param two_players: a dictionary containing the information of the two players
    :precondition: two_players is a dictionary has the players' names for the keys, and dictionaries for the values
        each dictionary has "score_card" and "dice" as the keys, whose values are the players' score_card and dice.
        All the scores are filled
    :postcondition: a string which is the the winner's name, or both players' name if there is a draw
    :return: a string

    >>> test_two_players = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '1', 'TOTAL': '1'},
'LOWER SECTION': {'Three of a kind': '14', 'Four of a kind': '16', 'YAHTZEE': '0', 'TOTAL': '30', 'GRANT TOTAL': '31'}},
'dice': []}, 'Joe': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},
'LOWER SECTION': {'Three of a kind': '0', 'Four of a kind': '0', 'YAHTZEE': '50', 'TOTAL': '50', 'GRANT TOTAL': '53'}},
'dice': []}}
    >>> winner(test_two_players)
    'Joe'
    >>> test_two_players = {'Dani': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'}, 'LOWER SECTION':
{'Three of a kind': '14', 'Four of a kind': '16', 'YAHTZEE': '50', 'TOTAL': '80', 'GRANT TOTAL': '83'}}, 'dice': []},
'Joe': {'score_card': {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'},'LOWER SECTION': {'Three of a kind': '0',
'Four of a kind': '30', 'YAHTZEE': '50', 'TOTAL': '80', 'GRANT TOTAL': '83'}}, 'dice': []}}
    >>> winner(test_two_players)
    'Dani & Joe'
    """


def main():
    doctest.testmod()
    play_yahtzee()


if __name__ == "__main__":
    main()
