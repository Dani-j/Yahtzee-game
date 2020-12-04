
def SCORE_CARD() -> dict:
    """
    Return the Yahtzee score card.
    """
    pass


def start_game() -> None:  # do we need to write None?
    """Start the game"""
    pass


def set_players(score_card: dict) -> dict:
    """
    Ask the players name and return a dictionary containing the information of the two players.

    :param score_card:
    :precondition:
    :postcondition:
    :return:
    """
    pass


def one_round(two_players: dict) -> dict:
    """
    Let user play one round.

    :param two_players:
    :return:
    """
    pass


def main_menu(dice_time: int, dice: list):
    """
    Print the main menu.

    The color of available options are green. (grey if unavailable???)

    :param dice_time:
    :param dice:
    :return:
    """
    # have 5 options
    # can I ask the player to either remove or keep dice before writing the score?
    # or allow user the choose to write the score, then if the dice kept are not 5, will have to remove or take dice???
    pass


def ask_menu_choice(player: str, dice_time: int, dice: list) -> str:
    """
    Ask the player's choice with making sure the choice made is available.

    :param player:
    :param dice:
    :param dice_time:
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
    Write the score the score into the player's score card.

    :param score_card:
    :param dice:
    :return:
    """
    pass