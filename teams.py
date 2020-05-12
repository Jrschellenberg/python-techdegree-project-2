import random


def __is_experienced(player):
    return player['experience']


def balance_teams(teams, players):
    try:
        players_per_team = len(players)/len(teams)
        if not players_per_team.is_integer():
            raise ValueError

        experienced_players = [player for player in players if player['experience']]
        inexperienced_players = [player for player in players if not player['experience']]

        print(experienced_players)


        # while len(players) > 0:
        #     random_player


    except ValueError:
        raise ValueError
