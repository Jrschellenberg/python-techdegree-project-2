import sys
from constants import TEAMS, PLAYERS
from clean_data import clean_data
from teams import balance_teams


def intro_msg():
    user_error = ""
    while True:
        print("""
---- MENU----

 Here are your choices:
  1) Display Team Stats
  2) Quit
            """)

        user_input = input("{}Enter an option > ".format(user_error))
        if user_input == '1':
            break
        elif user_input == '2':
            print("Goodbye.. See you next time!")
            sys.exit(0)
        user_error = user_input + " Is not a Valid Option "


def display_team_stats(teams):
    print()


def init():
    # need to update and build teams here
    teams = TEAMS.copy()
    players = clean_data(PLAYERS)
    # intro_msg()
    teams = balance_teams(teams, players)
    display_team_stats(teams)



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    init()
