from constants import TEAMS, PLAYERS
from clean_data import clean_data


def init():
    teams = TEAMS.copy()
    players = clean_data(PLAYERS)
    print(players)


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    init()
