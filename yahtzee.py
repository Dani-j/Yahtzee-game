import doctest


def SCORE_CARD() -> dict:
    """
    Return the Yahtzee score card as a dictionary.
    """
    pass


def play_yahtzee():
    """
    Let user to play the yahtzee.

    This yahtzee game only allow two users to play.
    The game ends when both of the two players finish their score card.
    If one of the player fills out all rows in the score card, then another play can play until fill our all their
    score card too.
    """
    pass


def set_players(score_card: dict) -> dict:
    """
    Ask the players name and return a dictionary containing the information of the two players.

    :param score_card: a yahtzee game score card template
    :precondition: score_card is a dictionary.
    :postcondition: return a dictionary has the players' names for the keys, and dictionaries for the values
        each dictionary has "score_card" and "dice" as the keys, whose values are the players' score_card and dice.
    :return: a dictionary containing the information of the two players
    """
    pass


def one_round(two_players: dict) -> dict:
    """
    Let user play one round and update the score card.

    In one round, only when one player write the score of a row, the another player can start playing.
    In the one round, the player can have 5 options from main_menu.
    One round ends when both players write the scores.


    :param two_players: a dictionary containing the information of the two players
    :precondition: two_players is a dictionary containing the information of the two players
    :postcondition: update the score card and return it
    :return: a dictionary which is the score card
    """
    pass


def main_menu_unavailable_choice(dice_time: int, kept_dice: list) -> tuple:
    """
    Checking the uavailable options and return it.

    1 representing the option "(1) - Keep the dice"
    3 representing the option "(3) - Roll the dice"

    :param dice_time: an integer in range [0, 2] representing the time left to dice
    :param kept_dice: a list containing the dice that is hold by the users
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple that the index 0 is a list containing the unavailable choices in the main menu,
        index 1 is the dice time
    :return: a tuple containing the unavailable choices in the main menu and the dice time.

    >>> test_dice_time = 2
    >>> test_kept_dice = []
    >>> main_menu_unavailable_choice(test_dice_time, test_kept_dice)
    ([],2)
    >>> test_dice_time = 2
    >>> test_kept_dice = [1, 2, 3, 4, 5]
    >>> main_menu_unavailable_choice(test_dice_time, test_kept_dice)
    ([3], 2)
    """


def main_menu(unavailable_choice: tuple):
    """
    Print the main menu formatted by the available_choice

    The color of available options are green (grey if unavailable).
    when the available_choice = [] , all the functions will print like below in green color:

    What do you want to do?
    (1) - Keep the dice
    (2) - Move the dice
    (3) - Roll the dice (1/3)
    (4) - Check score card
    (5) - Write Score

    Option "(1) - Keep the dice" will turn gray if the unavailable_choice is [1, 3] (when the player has 5 dice on hand)
    Option "(3) - Roll the dice (0/3)" will turn gray if the available_choice is [3] (run out of dice time).
    Option "(3) - Roll the dice (0/3) !NO DICE" will turn gray if the available_choice is [1, 3] (when the player has
    5 dice on hand).

    :param unavailable_choice: a tuple of unavailable choices in the main menu and dice time
    :precondition: unavailable_choice is a tuple that the index 0 is a list containing the unavailable choices
        in the main menu, index 1 is the dice time
    :postcondition: print the main menu in right color
    """
    pass


def ask_menu_choice(player: str, available_options: list) -> str:
    """
    Ask the player's choice with making sure the choice made is available.

    :param player: a string representing the player's name.
    :param available_options: a list containing available choices in the main menu
    :precondition: all the above parameter conditions must be met
    :postcondition: return a string representing the player's choice, the string must in the available_options.
    :return: a string representing the player's choice
    """
    pass


def roll_dice(kept_dice: list) -> list:
    """
    Roll the dice and show them/it to the player, as well as showing the dice on hand.

    :param kept_dice: a list representing the dice that is(are) kept by the player
    :precondition: kept_dice is a list no longer than 5
    :postcondition: return a list whose length equals to 5 after add the length of kept_dice
    :return: a list representing the dice that are/is generated randomly
    """
    pass


def print_dice_status(table_dice, kept_dice):
    """
    Print the dice on table and the dice on hand.

    When table_dice = ['3', '1', '2'], Dice on hand = ['1', '2'], will print:

    Dice on the table: ['3', '1', '2']
    Dice on hand: ['1', '2']

    The table_dice list will be in green color, the kept_dice will be in blue color.

    :param table_dice: a list of dice on table
    :param kept_dice: a list representing the dice that is(are) kept by the player
    :postcondition: print the dice on table in green color and the dice on hand in blue color.
    """


def hold_dice(table_dice: list, kept_dice: list) -> tuple:
    """
    let the player keep the dice.

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
    let the player remove the dice.

    when the player does not enter anything, do not remove any more dice

    :param kept_dice: a list representing the dice that is(are) kept by the player that could be removed
    :param table_dice: a list of dice on table
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple containing two list of dice, total length is 5
    :return: a tuple containing two lists, one contains the dice on table, another one contains the dice on hand
    """
    pass


def move_available_dice(table_dice: list, kept_dice: list, input_dice: list) -> tuple:
    """
    Diagnose the available input dice and move them/it either to table or the player's hand.

    This function will be used in remove_dice and hold_dice function
    because both of them have steps that move the available dice from one to another.
    For remove the card, just input table_dice as kept_dice, input kept_dice as table_dice.

    :param table_dice: a list of dice on table
    :param kept_dice: a list representing the dice that is(are) kept by the player
    :param input_dice: a list containing the input dice from the player
    :precondition: all the above parameter conditions must be met
    :postcondition: return a tuple containing two list of dice, the first one contains the dice on hand,
        the second one contains the dice on the table
    :return: a tuple containing two lists

    >>> test_table_dice = ['3', '1', '2']
    >>> test_kept_dice = ['1', '2']
    >>> test_input_dice = ["2", "3", "1", "4"]
    >>> move_available_dice(test_table_dice, test_kept_dice, test_input_dice)
    (['1', '2', '2', '5', '1'], [])
    >>> test_table_dice = ['3', '1', '2']
    >>> test_kept_dice = ['1', '2']
    >>> test_input_dice = ["2", "3", "1", "4"]
    >>> move_available_dice(test_kept_dice, test_table_dice, test_input_dice)
    ([], ['3', '1', '2', '2', '1'])
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

    :param score_card: a dictionary, the key and values are all strings
    :param kept_dice: a list
    :param table_dice: a list
    :precondition: all the above parameter conditions must be met
    :postcondition: return the updated score card, which is a dictionary
    :return: a dictionary
    """
    pass


# ask if I should separate into return and print?
def print_options(score_card: dict) -> dict:  # should I separate it?? one for find the available ones, one for print??
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

    :param score_card:
    :precondition:
    :postcondition:
    :return: a list containing the available options
    """
    pass


def choose_score_card_row(available_options: dict) -> str:
    """
    Ask the player which row to write the score and return the chosen row.

    :param available_options:
    :precondition:
    :postcondition:
    :return:
    """
    pass


def count_scores(score_card: dict, write_row: str, dice: list) -> int:
    """
    Calculate the score by the chosen way and return the score.

    :param score_card:
    :param write_row: a
    :param dice: a list merged by table_dice and kept_dice
    :precondition:
    :postcondition:
    :return: an str which is the scores in a given row
    """
    pass


def total_and_bonus(score_card: dict) -> dict:  # JUST RETURN NOT UPDATE??
    """
    Calculate the total score in upper section and lower section and the bonus.

    :param score_card:
    :precondition:
    :postcondition:
    :return: score_card
    """
    pass


def winner(two_players: dict):
    """
    Compare the grand total scores between two players and find the winner.

    :param two_players:
    :precondition:
    :postcondition:
    :return: a string representing the winner's name
    """


def main():
    doctest.testmod()
    play_yahtzee()


if __name__ == "__main__":
    main()
