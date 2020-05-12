import sys


def __convert_height_to_int(string):
    try:
        [integer, *_] = string.split()
        return int(integer)
    except ValueError:
        raise ValueError


def __convert_exp_to_bool(string):
    try:
        if string.lower() != 'yes' and string.lower() != 'no':
            raise ValueError
        return string.lower() == 'yes'
    except ValueError:
        raise ValueError("Oops! There was an issue "
                         "converting experience to a Bool,"
                         " Please ensure it is 'yes' or 'no' "
                         "only and try again")


def clean_data(players):
    players_list = []

    for player in players.copy():
        players_dict = {}
        try:
            (key1, experience), \
                (key2, guardians), \
                (key3, height), \
                (key4, name) = sorted(player.items())

            players_dict[key1] = __convert_exp_to_bool(experience)
            players_dict[key2] = guardians.split(' and ')
            players_dict[key3] = __convert_height_to_int(height)
            players_dict[key4] = name
            players_list.append(players_dict)

        except ValueError as err:
            print(err)
            print("Please fix data in constants.py and please try again")
            sys.exit(1)

    return players_list
