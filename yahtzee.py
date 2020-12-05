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
    """
    pass


def set_players(score_card: dict) -> dict:
    """
    Ask the players name and return a dictionary containing the information of the two players.

    :param score_card: a yahtzee game score card template
    :precondition: score_card is a dictionary.
    :postcondition: return a dictionary has the players' names for the keys, and dictionaries for the values
        which has "score_card" and "dice" as the keys, and the players' score_card and dice list as the values.
    :return: a dictionary containing the information of the two players
    """
    pass


def one_round(two_players: dict) -> dict:
    """
    Let user play one round and update the score card.

    :param two_players: a dictionary containing the information of the two players
    :precondition: two_players is a dictionary containing the information of the two players
    :postcondition: update the score card and return it
    :return: a dictionary which is the score card
    """
    pass


def main_menu(dice_time: int, kept_dice: list) -> list:
    """
    Print the main menu while checking the available options.

    The color of available options are green (grey if unavailable).
    when the dice_time == 1, kept_list == [1, 2, 3, 4], all the functions will print like below in green color:
    What do you want to do?
    (1) - Keep the dice
    (2) - Move the dice
    (3) - Roll the dice (1/3)
    (4) - Check score card
    (5) - Write Score

    option "(1) - Keep the dice" will turn gray if the length of kept_dice is 5.
    option "(3) - Roll the dice (0/3)" will turn gray if the dice_time is 0 or the length of kept_dice is 5.

    :param dice_time: the time left to dice
    :param kept_dice: a list containing the dice that is hold by the users
    :precondition: all the above parameter conditions must be met
    :postcondition: return a list of available choices in the main menu.
    :return: a list of available choices in the main menu.
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
    :param input_dice: return a tuple containing two list of dice, the first one contains the dice on hand,
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

    :param score_card:
    :param player:
    :return:
    """


def write_score(score_card: dict, dice: list) -> dict:
    """
    Write the score into the player's score card.

    :param score_card:
    :param dice:
    :return:
    """
    pass
    # write the score in the helper function "count_scores()" or in this function????


# helper functions for write_score() (do you want comments like this to clarify the helper functions?)
def print_options(score_card: dict) -> dict:
    """
    Display the options of way to count the score to the players and return the available options.

    The color of available options are green. (grey if unavailable??? or black?)

    :param score_card:
    :return: a dictionary, the key of the dictionary is the letter presenting the choice, the key is the score type
    """
    pass


def choose_score_card_row(available_options: dict) -> str:
    """
    Ask the player the way to count the score and return the chosen way.

    :param available_options:
    :return:
    """
    pass


def count_scores(count_way: str, dice: list) -> int:
    """
    Calculate the score by the chosen way and return the score.

    :param count_way:
    :param dice:
    :return:
    """
    pass


def add_total_bonus(score_card: dict) -> dict:
    """
    Calculate the total score in upper section and lower section and the bonus.

    :param score_card:
    :return: score_card
    """
    pass


def winner(two_players: dict):
    """
    Compare the grand total scores between two players and find the winner.

    :param two_players:
    :return:
    """