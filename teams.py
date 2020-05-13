import sys
import random
from functools import reduce


def __get_inexperienced(array):
    return [player for player in array if not player['experience']]


def __get_experienced(array):
    return [player for player in array if player['experience']]


def __is_team_experience_balanced(num_teams, experienced_players,
                                  inexperienced_players):
    num_experienced = len(experienced_players)
    num_inexperienced = len(inexperienced_players)
    return num_experienced == num_inexperienced \
        and num_experienced % num_teams == 0 \
        and num_inexperienced % num_teams == 0


def __is_experienced(player):
    return player['experience']


def __calculate_average_height(array):
    heights = list(map(lambda player: player['height'], array))
    average_height = \
        reduce((lambda acc, cur: acc + cur), heights) / len(heights)
    return round(average_height, 2)


def __flatten(arr):
    # Code used from SOF https://stackoverflow.com/a/40601769
    """Takes N-dimensional list, Returns 1-Dimensional list.
    Returned list will be ordered following N-Dimensional list"""
    try:
        return __flatten(arr[0]) \
               + (__flatten(arr[1:])
                  if len(arr) > 1 else []) if type(arr) is list else [arr]
    except IndexError:
        return []


def __get_joined_str(array, key, delimiter):
    """
    :param list array: list to map over
    :param str key: the key to look up in dictionary
    :param str delimiter: The delimiter to join together list
    :return:
    """
    guardians = list(map(lambda player: player[key], array))
    one_d_guardians = __flatten(guardians)
    return delimiter.join(one_d_guardians)


def balance_teams(teams, players):
    """
    :param list teams: List of Available Teams
    :param list players: List of Available Players
    :return list: Returns A Balanced list of teams with Players
    """
    try:
        num_players = len(players)
        num_teams = len(teams)

        players_per_team = num_players / num_teams
        experienced_players = __get_experienced(players)
        inexperienced_players = __get_inexperienced(players)

        if not players_per_team.is_integer():
            raise ValueError("The Players per Team is not Properly Balanced."
                             "\nPlease Update players and try again")
        if not __is_team_experience_balanced(num_teams, experienced_players,
                                             inexperienced_players):
            raise ValueError("Cannot Balance Teams with The Given Data!")

        """
        Have algorithm that iterates over number of teams
        Inside this loop, iterates over players_per_team
        Since we know Experience is balanced,
        toggle back and forth between the arrays
        Randomly Grab a player copy using random lib, remove original ref.
        """

        balanced_teams = []

        for team in range(num_teams):
            team_dict = {'players': []}
            is_player_experienced = True

            for chosen_player in range(int(players_per_team)):
                players_to_chose = experienced_players \
                    if is_player_experienced else inexperienced_players

                # get random player
                player_index_to_choose = \
                    random.randint(0, (len(players_to_chose) - 1))
                rand_player = players_to_chose[player_index_to_choose].copy()
                del players_to_chose[player_index_to_choose]

                team_dict['players'].append(rand_player)
                is_player_experienced = not is_player_experienced

            # Now we add Stats as Needed
            players = team_dict['players'].copy()
            del team_dict['players']

            team_dict['experienced_players_total'] = \
                len(__get_experienced(players))
            team_dict['inexperienced_players_total'] = \
                len(__get_inexperienced(players))

            team_dict['average_height'] = __calculate_average_height(players)
            team_dict['guardian_names'] = \
                __get_joined_str(players, "guardians", ", ")
            team_dict['player_names'] = __get_joined_str(players, "name", ", ")
            team_dict['total_players'] = len(players)
            team_dict['team_name'] = teams[team]

            balanced_teams.append(team_dict)

        return balanced_teams

    except ValueError as err:
        print("{}\nExiting gracefully...".format(err))
        sys.exit()
