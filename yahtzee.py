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


def main_menu(dice_time: int, kept_dice: list):
    """
    Print the main menu while checking the available options.

    The color of available options are green (grey if unavailable).
    when the dice_time == 1, kept_list == [1, 2, 3, 4], all the functions will print like below in green color:
    what's your choice?
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

    :param player:
    :param available_options: [2, 4, 5]
    :return:


    """
    # can I do this??? if unavailable choice, will ask the player to enter the choice again
    # until the player enter an available choice??
    # use while loop (only return when enter an available choice; otherwise, print warning, and ask again)???
    pass


def roll_dice(kept_dice: list) -> list:
    """
    Roll the dice and show them/it to the player.

    :param kept_dice:
    :return:
    """
    pass


def hold_dice(kept_dice: list, current_dice: list) -> list:
    """
    let the player keep the dice.

    when the player does not enter anything, do not keep any more dice

    :param kept_dice:
    :param current_dice:
    :return: a list representing the kept dice
    """
    pass


def remove_dice(kept_dice: list, current_dice: list) -> list:
    """
    let the player remove the dice.

    when the player does not enter anything, do not remove any more dice

    :param kept_dice:
    :param current_dice:
    :return: a list representing the kept dice after removing.
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