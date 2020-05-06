from constants import TEAMS, PLAYERS

def unpack_player(name, guardians, experience, height):
    return (name, guardians, experience, height)


def clean_data(players):
    players_copy = []
    for p in players:
        player = p.copy()
        name, guardians, experience, height = unpack_player(**p)
        print(name)


def init():
    teams = TEAMS.copy()
    players = clean_data(PLAYERS)


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    init()
