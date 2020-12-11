import doctest
import random
import re


def INITIAL_SCORE_CARD():
    """The initial score card."""
    return {"UPPER SECTION": {"Ones": -1, "Twos": -1, "Threes": -1, "Fours": -1, "Fives": -1, "Sixes": -1,
                              "TOTAL": 0, "Bonus": 0, "TOTAL_": 0},
            "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "Full House": -1,
                              "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1,
                              "TOTAL": 0, "GRANT TOTAL": 0}}


def OPTION_UNAVAILABLE():
    """Print this string when user input an unavailable option."""
    print("Oops, option unavailable.")


def EMPETY_SCORE() -> int:
    """-1 means there is no score with the related row."""
    return -1


def FULL_HOUSE_POINTS() -> int:
    """Get 25 points if have valid full house."""
    return 25


def SMALL_STRAIGHT_POINTS() -> int:
    """Get 30 points if have valid small straight."""
    return 30


def LARGE_STRAIGHT_POINTS() -> int:
    """Get 40 points if have valid large straight."""
    return 40


def YAHTZEE_SCORE_POINTS() -> int:
    """Get 50 points if have first valid YAHTZEE."""
    return 50


def EXTRA_YAHTZEE_SCORE_POINTS() -> int:
    """Get 100 points if have valid YAHTZEE after first time."""
    return 100


def UPPER_SECTION_BONOUS_REQUIRED_POINTS() -> int:
    """Must have 65 points in the upper section total to have the bonus points."""
    return 65


def UPPER_SECTION_BONOUS() -> int:
    """Get 35 bonus points."""
    return 35


def NOT_VALID_ROW_POINTS():
    """Get 0 point when the dice is not match with the row requirement."""
    return 0


def play_yahtzee():
    """
    Let the user play Yahtzee.

    This Yahtzee game only allows two users to play.

    The game ends when both of the two players complete their score card.

    If only one of the players fills out all the rows in the score card,
        the other player can play until their score card is completed.

    :postcondition: print the result of the Yahtzee game.
    """
    player_1_score_card, player_2_score_card = INITIAL_SCORE_CARD(), INITIAL_SCORE_CARD()
    while True:
        player_1_scores = set(player_1_score_card["UPPER SECTION"].values()) | \
                          set(player_1_score_card["LOWER SECTION"].values())
        player_2_scores = set(player_2_score_card["UPPER SECTION"].values()) | \
                          set(player_2_score_card["LOWER SECTION"].values())
        if EMPETY_SCORE() in player_1_scores:
            player_1_score_card = one_turn("Player One", player_1_score_card)
        if EMPETY_SCORE() in player_2_scores:
            player_2_score_card = one_turn("Player Two", player_2_score_card)
        else:
            break
    winner(player_1_score_card, player_2_score_card)


def one_turn(player: str, score_card: dict) -> dict:
    """
    Let user play one turn and update the score card.

    At the beginning, the system automatically roll the dice for the player.
    One turn ends when the player writes the score.

    :param player: a string which is player's name
    :param score_card: a dictionary representing the Yahtzee score card
    :precondition: all the above parameter conditions must be met
    :postcondition: update the score card and return it
    :return: a dictionary which is the updated score card
    """
    kept_dice, dice_time = [], 2
    table_dice = roll_dice(kept_dice)
    while True:
        player_choice = ask_menu_choice(player, dice_time, table_dice, kept_dice)
        if player_choice == "1":
            kept_dice, table_dice = hold_dice(table_dice, kept_dice)
        elif player_choice == "2":
            kept_dice, table_dice = remove_dice(table_dice, kept_dice)
        elif player_choice == "3":
            table_dice, dice_time = roll_dice(kept_dice), dice_time - 1
        elif player_choice == "4":
            print_score_card(player, score_card)
        elif player_choice == "5":
            score_card = write_score(score_card, kept_dice, table_dice)
            print_score_card(player, score_card)
            return score_card


def roll_dice(kept_dice: list) -> list:
    """
    Roll the dice and return the result.

    :param kept_dice: a list of dice held by the player
    :precondition: kept_dice is a list of string(s) or an empty string, which length is less than 5
    :postcondition: return a list containing the dice on table
    :return: a list of strings
    """
    table_dice = random.sample(range(1, 6), 5 - len(kept_dice))
    table_dice = [str(a_dice) for a_dice in table_dice]
    return table_dice


def ask_menu_choice(player: str, dice_time: int, table_dice: list, kept_dice: list) -> str:
    """
    Return player's choice.

    :param player: a string representing the player's name.
    :param dice_time: an integer representing the number of time(s) the player could roll the dice
    :param table_dice: a list of dice on table
    :param kept_dice: a list of dice held by the user
    :precondition: player is in ["Player One", "Player Two"],
        both kept_dice and table_dice are a list of strings or an empty list
    :postcondition: return a string representing the player's choice, the string must be in ["1", "2", "3", "4", "5"]
    :return: a string representing the player's choice
    """
    print_dice_status(table_dice, kept_dice, player)
    available_options = available_main_options(dice_time, kept_dice)
    main_menu(available_options, dice_time)
    while True:
        player_choice = input("Please enter your choice by the provided \033[1;32m"
                              "option number (in green)\033[0m, then press enter:").strip()
        if player_choice in available_options:
            return player_choice
        OPTION_UNAVAILABLE()


def print_dice_status(table_dice: list, kept_dice: list, player="You have"):
    """
    Print the dice on table and the dice in hand.

    When table_dice = ['3', '1', '2'], dice on hand = ['1', '2'], will print:

    You have:
    Dice on the table: ['3', '1', '2']
    Dice on hand: ['1', '2']

    The table_dice list will be in green color, the kept_dice will be in blue color.

    :param table_dice: a list of dice on table
    :param kept_dice: a list of dice held by the player
    :param player: print the player's name or "You have" for the first sentence????
    :precondition: both kept_dice and table_dice are a list of strings or an empty list, player is a string
    :postcondition: print the dice on table in green color and the dice in hand in blue color.
    """
    print(f"\n{player}:\nDice on the table: \033[1;32m{table_dice}\033[0m\nDice on hold: \033[1;34m{kept_dice}\033[0m")


def available_main_options(dice_time: int, kept_dice: list) -> set:
    """
    Checking the available options and return it.

    When there is 0 dice held by the player, cannot remove the dice form the hand
    When there are 5 dice held by the player, cannot take any dice on table
    When the dice_time == 0, cannot roll the dice

    :param dice_time: an integer representing the number of time(s) the player could roll the dice
    :param kept_dice: a list of dice held by the player
    :precondition: dice_time is an integer that is smaller than 3, kept_dice is a list of string(s) or an empty string
    :postcondition: return a set, the element(s) in set are/is in ["1", "2", "3", "4", "5"]
    :return: a set containing the available options in the main menu

    >>> test_dice_time = 2
    >>> test_kept_dice = []
    >>> available_main_options(test_dice_time, test_kept_dice)
    {"1", "3", "4", "5"}
    >>> test_dice_time = 2
    >>> test_kept_dice = ["1", "2", "3", "4", "5"]
    >>> available_main_options(test_dice_time, test_kept_dice)
    {"2", "4", "5"}
    >>> test_dice_time = 0
    >>> test_kept_dice = ["1", "2", "3", "4"]
    >>> available_main_options(test_dice_time, test_kept_dice)
    {"1", "2", "4", "5"}
    """
    available_options = {"1", "2", "3", "4", "5"}
    if dice_time == 0 and len(kept_dice) != 5:
        available_options.difference_update({"3"})
    if len(kept_dice) == 5:
        available_options.difference_update({"1", "3"})
    if len(kept_dice) == 0:
        available_options.difference_update({"2"})
    return available_options


def main_menu(available_options: set, dice_time: int):
    """
    Print the well formatted main menu.

    The color of the available options are green (grey if unavailable).
    When the available_options = [] , all the functions will print like below in green color:

    Player One, please chose one of the green color option below
    (1) - Keep the dice
    (2) - Remove the dice
    (3) - Roll the dice (1/3)
    (4) - Check score card
    (5) - Write Score

    Options will turn gray if not in the available options.

    :param available_options: a set containing the available options in the main menu
    :param dice_time: an integer representing the number of time(s) the player could roll the dice
    :precondition: all the above parameter conditions must be met
    :postcondition: print the main menu in right color
    """
    print(f"Please choose one of the option (in green) below，must write the score before the next player play")
    if "1" not in available_options:
        print("\033[1;37m(1) - Keep the dice (NO DICE on table!)\033[0m")
    else:
        print("\033[1;32m(1) - Keep the dice\033[0m")
    if "2" not in available_options:
        print(f"\033[1;37m(2) - Remove the dice\033[0m")
    else:
        print(f"\033[1;32m(2) - Remove the dice\033[0m")
    if "3" not in available_options:
        print(f"\033[1;37m(3) - Roll the dice ({dice_time}/3)\033[0m")
    else:
        print(f"\033[1;32m(3) - Roll the dice ({dice_time}/3)\033[0m")
    print(f"\033[1;32m(4) - Check score card\033[0m")
    print(f"\033[1;32m(5) - Write score\033[0m")


def hold_dice(table_dice: list, kept_dice: list) -> tuple:
    """
    Let the player keep the dice.

    When the player does not enter anything, do not keep any new dice.

    :param table_dice: a list of dice on table that can be held by the user
    :param kept_dice: a list of dice held by the player
    :precondition: both kept_dice and table_dice are a list of strings or an empty list
    :postcondition: the first list in the return tuple containing the the dice on table, the other one containing the
        dice in hand
    :return: a tuple containing two lists
    """
    print_dice_status(table_dice, kept_dice)
    input_dice = list(input("Please enter the\033[1;32m dice number(s)\033[0m that you want to "
                            "hold from the dice on table: "))
    kept_dice, table_dice = move_available_dice(table_dice, kept_dice, input_dice)
    return kept_dice, table_dice


def move_available_dice(dice_to_remove: list, dice_to_add: list, input_dice: list) -> tuple:
    """
    Diagnose the available input dice and move them/it either to table or the player's hand.

    :param dice_to_remove: a list containing the dice that may be removed to dice_to_add
    :param dice_to_add: a list containing the dice that may be added more from dice_to_remobe
    :param input_dice: a list containing dice the player wants to hold/move
    :precondition: all the above parameter conditions must be met
    :postcondition: the first list in the return tuple containing the the dice on hand, another one containing the
        dice on table
    :return: a tuple containing two lists

    >>> test_dice_to_remove = ['3', '1', '2']
    >>> test_dice_to_add = ['1', '2']
    >>> test_input_dice = ["2", "3", "1", "5"]
    >>> move_available_dice(test_dice_to_remove, test_dice_to_add, test_input_dice)
    (['1', '2', '2', '3', '1'], [])
    >>> test_dice_to_remove = ['1', '2']
    >>> test_dice_to_add = ['3', '1', '2']
    >>> test_input_dice = ["1", "2"]
    >>> move_available_dice(test_dice_to_remove, test_dice_to_add, test_input_dice)
    (['3', '1', '2', '2', '1'], [])
    """
    dice_unavailable = []
    for dice in input_dice:
        if dice not in dice_to_remove and dice != " ":
            dice_unavailable.append(dice)
        elif dice in dice_to_remove:
            dice_to_add.append(dice)
            dice_to_remove.remove(dice)

    if len(dice_unavailable) != 0:
        print(f"{dice_unavailable} are/is not available.")

    return dice_to_add, dice_to_remove


def remove_dice(table_dice: list, kept_dice: list) -> tuple:
    """
    Let the player remove the dice from the table.

    When the player does not enter anything, do not remove any more dice.

    :param table_dice: a list of dice on table
    :param kept_dice: a list of dice held by the player
    :precondition: both kept_dice and table_dice are a list of strings or an empty list
    :postcondition: the first list in the return tuple containing the the dice on table, the other one containing the
        dice on hand
    :return: a tuple containing two lists
    """
    print_dice_status(table_dice, kept_dice)
    input_dice = list(input("Please enter the\033[1;34m dice number(s)\033[0m that "
                            "you want to put back to the table: "))
    table_dice, kept_dice = move_available_dice(kept_dice, table_dice, input_dice)
    return kept_dice, table_dice


def print_score_card(player: str, score_card: dict):
    """
    Display the score card to the player.

    :param player: a string representing the player's name
    :param score_card: a dictionary representing the Yahtzee score card
    :precondition: all the above parameter conditions must be met
    :postcondition: print a formated score card

    >>> test_score_card = {"UPPER SECTION": {"Ones": "3", "Twos": -1, "Threes": -1, "Fours": -1, "Fives": "10",
"Sixes": -1, "TOTAL": -1, "Bonus": -1, "TOTAL_": ""}, "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1,
"Full House": "25", "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1, "TOTAL": -1,
"GRANT TOTAL": ""}}
    >>> test_player = "Dani"
    >>> print_score_card(test_player, test_score_card)
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
    print(f"\n{player}'s score card:")
    for section, rows in score_card.items():
        header_filled = f'{section:^28s}'
        markers = "-" * len(header_filled)
        header = [markers, header_filled, markers]
        results = []
        for count, row in enumerate(rows):
            if rows[row] == -1:
                results.append(f"{row:<16s}{'':^12s}")
            else:
                results.append(f"{row:<16s}{str(rows[row]):^12s}")
        print("\n".join(header + results))


def write_score(score_card: dict, kept_dice: list, table_dice: list) -> dict:
    """
    Write the score into the player's score card.

    :param score_card: a nested dictionary representing the Yahtzee score card
    :param kept_dice: a list of dice held by the player
    :param table_dice: a list of dice on table
    :precondition: score_card is a nested dictionary,
        both kept_dice and table_dice are a list of strings or an empty list
    :postcondition: return the updated score card, which is a dictionary
    :return: a dictionary
    """
    dice = sorted(kept_dice + table_dice)
    print_dice_status(table_dice, kept_dice)
    write_row = choose_score_card_row(score_card, dice)
    write_score_row = count_scores(score_card, write_row, dice)
    score_card = update_score_card(score_card, write_score_row)
    return score_card


def choose_score_card_row(score_card: dict, dice: list) -> tuple:
    """
    Ask the player which row to write the score, return their choice with the row name

    :param score_card: a dictionary, the key and values are all strings
    :param dice: a length 5 list of strings merged by table_dice and kept_dice
    :precondition: all the above parameter conditions must be met
    :postcondition: the return tuple containing the row number and the row name
    :return: a tuple consists of a number and a string
    """
    available_options = available_row(score_card, dice)
    print_row_options(available_options, score_card)
    while True:
        player_choice = input(f"The available options are shown in green, please enter one of the available "
                              f"options by number: ").strip()
        if player_choice.isnumeric():
            if int(player_choice) in available_options:
                return int(player_choice), available_options[int(player_choice)]
        OPTION_UNAVAILABLE()


def available_row(score_card: dict, dice: list) -> dict:
    """
    Checking the available rows to write the score and return the the rows.

    The dice list is used for checking if the user can choose "YAHTZEE"
        when they have a positive score in "YAHTZEE" row.

    :param score_card: a dictionary representing the yahtzee score card
    :param dice: a length 5 list of strings merged by table_dice and kept_dice
    :precondition: all the above parameter conditions must be met
    :postcondition: the return dictionary containing the option number as the key, row name as the value
    :return: a dictionary

    >>> test_score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
"LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
    >>> test_dice = ["1", "2", "3", "4", "5"]
    >>> available_row(test_score_card, test_dice)
    {1: "Ones", 2: "Twos", 3: "Three of a kind", 4: "YAHTZEE"}
    >>> test_score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
"LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": 50, "TOTAL": 0, "GRANT_TOTAL": 0}}
    >>> test_dice = ["1", "1", "1", "2", "1"]
    >>> available_row(test_score_card, test_dice)
    {1: "Ones", 2: "Twos", 3: "Three of a kind"}
    >>> test_score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
"LOWER SECTION": {"Three of a kind": -1, "YAHTZEE": 50, "TOTAL": 0, "GRANT_TOTAL": 0}}
    >>> test_dice = ["1", "1", "1", "1", "1"]
    >>> available_row(test_score_card, test_dice)
    {1: "Ones", 2: "Twos", 3: "Three of a kind", 4: "YAHTZEE"}
    """
    available_options = {}
    count = 1
    for section, rows in score_card.items():
        for row, score in rows.items():
            if row == "TOTAL":
                break
            if row == "YAHTZEE" and re.match(r"(.)\1{4}", "".join(dice)) and score != 0:
                available_options[count] = row
                continue
            if score == -1:
                available_options[count] = row
            count += 1
    return available_options


def print_row_options(available_options: dict, score_card: dict) -> list:
    """
    Display the options of the available row to write the score and return the available rows.

    The color of available options are green. (grey if unavailable)

    If score_card = {"UPPER SECTION": {"Ones": "3", "Twos": -1, "Threes": -1, "Fours": -1, "Fives": "10", "Sixes":
    -1, "TOTAL": -1, "Bonus": -1, "TOTAL_": ""}, "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1,
    "Full House": "25", "Small Straight": -1, "Large straight": -1, "Chance": -1, "YAHTZEE": -1, "TOTAL": -1,
    "GRANT TOTAL": ""}}, he function will print like below:

    ---------------------
    UPPER SECTION
    ---------------------
    (1) - Ones
    (2) - Twos
    (3) - Threes
    (4) - Fours
    (5) - Fives
    (6) - Sixes
    ---------------------
    LOWER SECTION
    ---------------------
    (7) - Three of a kind
    (8) - Four of a kind
    (9) - Full House
    (10) - Small Straight
    (11) - Large straight
    (12) - Chance
    (13) - YAHTZEE

    While "(A) - Ones", "(F) - Sixes", and "(I) - Full House" are in grey color, others are in green color.

    :param available_options: dictionary containing the option number as the key, row name as the value
    :param score_card: a dictionary representing the yahtzee score card
    :precondition: available_options must not empty
    :postcondition: return a list of letters representing the available row to add the score
    :return: a list containing the available row to add the score
    """
    options_prints = []
    markers = "-" * 21
    count = 0
    for section, rows in score_card.items():
        options_prints += [markers, section, markers]
        for row in rows:
            if row == "TOTAL":
                break
            count += 1
            if count in available_options:
                options_prints.append(f"\033[1;32m({count}) - {row}\033[0m")  # {chr(ord('@')+count)}
            else:
                options_prints.append(f"\033[1;37m({count}) - {row}\033[0m")  # {chr(ord('@')+count)}
    print("\n".join(options_prints) + "\n")


def count_scores(score_card, write_row: tuple, dice: list) -> tuple:
    """
    Calculate the score with the given row and dice.

    :param score_card: a dictionary representing the yahtzee score card
    :param write_row: a tuple consists of the row number and the row name
    :param dice: a list merged by table_dice and kept_dice, the length is 5
    :precondition: all the above parameter conditions must be met
    :postcondition: return the score and the row name
    :return: a tuple

    >>> test_score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": 0, "Bonus": 0, 'TOTAL_': 0},
"LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": 0}}
    >>> test_write_row = (1, "Ones")
    >>> test_dice = ["1", "1", "3", "4", "5"]
    >>> count_scores(test_score_card, test_write_row, test_dice)
    (2, "Ones")
    >>> test_score_card = {"UPPER SECTION": {"Ones": "1", "Twos": -1, "TOTAL": "1", "Bonus": 0, 'TOTAL_': 1},
"LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": -1, "GRANT_TOTAL": 1}}
    >>> test_write_row = (4, "Four of a kind")
    >>> test_dice = ["2", "4", "4", "4", "4"]
    >>> count_scores(test_score_card, test_write_row, test_dice)
    (18, "Four of a kind")
    """
    if write_row[0] < 7:
        return sum([int(a_dice) for a_dice in dice if int(a_dice) == write_row[0]]), write_row[1]
    if write_row[0] == 7 and dice.count(dice[2]) >= 3 or write_row[0] == 8 and dice.count(dice[2]) >= 4 or \
            write_row[0] == 12:
        return sum([int(a_dice) for a_dice in dice]), write_row[1]
    if write_row[0] == 9 and re.match(r"(.)\1(.)\2{2}|(.)\3{2}(.)\4", "".join(dice)):
        return FULL_HOUSE_POINTS(), write_row[1]
    if write_row[0] == 10 and set(dice) in ({"1", "2", "3", "4"}, {"2", "3", "4", "5"}, {"3", "4", "5", "6"}):
        return SMALL_STRAIGHT_POINTS(), write_row[1]
    if write_row[0] == 11 and dice in (["1", "2", "3", "4", "5"], ["2", "3", "4", "5", "6"]):
        return LARGE_STRAIGHT_POINTS(), write_row[1]
    if write_row[0] == 13 and re.match(r"(.)\1{4}", "".join(dice)):
        if score_card["LOWER SECTION"]["YAHTZEE"] == EMPETY_SCORE():
            return YAHTZEE_SCORE_POINTS(), write_row[1]
        return EXTRA_YAHTZEE_SCORE_POINTS(), write_row[1]
    return NOT_VALID_ROW_POINTS(), write_row[1]


def update_score_card(score_card: dict, write_score_row: tuple) -> dict:
    """
    Write the score into the player's score card.
    
    :param score_card: a dictionary representing the Yahtzee score card
    :param write_score_row: a tuple representing the score and the row name
    :precondition: all the above parameter conditions must be met
    :postcondition: update the score card and return it
    :return: an dictionary
    
    >>> test_score_card = {"UPPER SECTION": {"Ones": -1, "Twos": -1, "TOTAL": -1, "Bonus": -1, 'TOTAL_': 0},
"LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": -1, "GRANT_TOTAL": 0}}
    >>> test_write_score_row = (2, "Ones")
    >>> update_score_card(test_score_card, test_write_score_row)
    {"UPPER SECTION": {"Ones": 2, "Twos": -1, "TOTAL": 2, "Bonus": -1, 'TOTAL_': 2},
    "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": -1, "GRANT_TOTAL": 2}}
    >>> test_score_card = {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": "1", "Bonus": 0, 'TOTAL_': 1},
"LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": -1, "GRANT_TOTAL": 1}}
    >>> test_write_score_row = (18, "Four of a kind")
    >>> update_score_card(test_score_card, test_write_score_row)
    {"UPPER SECTION": {"Ones": 1, "Twos": -1, "TOTAL": "1", "Bonus": 0, 'TOTAL_': 1},
    "LOWER SECTION": {"Three of a kind": -1, "Four of a kind": 18, "TOTAL": 18, "GRANT_TOTAL": 19}}
    >>> test_score_card = {"UPPER SECTION": {"Ones": "1", "Twos": -1, "TOTAL": "1", "Bonus": 0, 'TOTAL_': 1'},
"LOWER SECTION": {"Three of a kind": -1, "Four of a kind": -1, "TOTAL": 0, "GRANT_TOTAL": "1"}}
    """
    # if write_score_row[1] in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]:
    #     score_card["UPPER SECTION"][write_score_row[1]] = write_score_row[0]
    #     score_card["UPPER SECTION"]["TOTAL"] += write_score_row[0]
    #     if score_card["UPPER SECTION"]["TOTAL"] >= 63:
    #         score_card["UPPER SECTION"]["Bonus"] = 35
    #     score_card["UPPER SECTION"]["TOTAL_"] = score_card["UPPER SECTION"]["TOTAL"] + (
    #         score_card["UPPER SECTION"]["Bonus"])
    #


def winner(player_1_score_card: dict, player_2_score_card: dict):
    """
    Compare the grand total scores between two players and find the winner.

    :param player_1_score_card: a dictionary representing the score card of the player one.
    :param player_2_score_card: a dictionary representing the score card of the player two.
    :precondition: all the above parameter conditions must be met
    :postcondition: print the correct result

    >>> test_player_1_score_card = {'UPPER SECTION': {'Ones': 1, 'TOTAL': 1}, 'LOWER SECTION':
    {'Three of a kind': 14, 'Four of a kind': 16, 'YAHTZEE': 0, 'TOTAL': 30, 'GRANT TOTAL': 31}}
    >>> test_player_2_score_card = {'UPPER SECTION': {'Ones': '3', 'TOTAL': '3'}, 'LOWER SECTION':
    {'Three of a kind': 0, 'Four of a kind': 0, 'YAHTZEE': 50, 'TOTAL': 50, 'GRANT TOTAL': 53}}
    >>> winner(test_player_1_score_card, test_player_2_score_card)
    'Congrats, player two, You win!'
    >>> test_player_1_score_card = {'UPPER SECTION': {'Ones': 3, 'TOTAL': 3}, 'LOWER SECTION':
{'Three of a kind': 14, 'Four of a kind': 16, 'YAHTZEE': 50, 'TOTAL': 80, 'GRANT TOTAL': 83}}
    >>> test_player_2_score_card = {'UPPER SECTION': {'Ones': 3, 'TOTAL': 3},'LOWER SECTION':
    {'Three of a kind': 0, 'Four of a kind': 30, 'YAHTZEE': 50, 'TOTAL': 80, 'GRANT TOTAL': 83}}
    >>> winner(test_player_1_score_card, test_player_2_score_card)
    'Congrats. You both win!'
    """
    player_1_score = player_1_score_card["LOWER SECTION"]["GRANT TOTAL"]
    player_2_score = player_2_score_card["LOWER SECTION"]["GRANT TOTAL"]
    if player_1_score == player_2_score:
        print("Congrats. You both win!")
    elif player_1_score > player_2_score:
        print("Congrats, player one. You win!")
    else:
        print("Congrats, player two. You win!")


def main():
    doctest.testmod()
    play_yahtzee()


if __name__ == "__main__":
    main()
