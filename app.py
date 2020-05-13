import sys

from clean_data import clean_data
from constants import TEAMS, PLAYERS
from teams import balance_teams

ERROR_MSG = " Is not a Valid Option "


def exit_program():
    print("Goodbye.. See you next time!")
    sys.exit(0)


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
            exit_program()
        user_error = user_input + ERROR_MSG


def get_user_selected_team(balanced_teams):
    teams_to_display = list(map(lambda team: team['team_name'], balanced_teams))
    valid_option = []
    user_error = ""
    for num, team in enumerate(teams_to_display, start=1):
        valid_option.append(str(num))
        print("{}.) {}".format(num, team))
    print("{}.) {}".format('0', 'Quit'))

    while True:
        user_input = input("{}Enter an option > ".format(user_error))
        if user_input == "0":
            exit_program()
        if user_input in valid_option:
            return int(user_input) - 1
        user_error = user_input + ERROR_MSG


def display_team_stats(team):

    print(f"""
Team: {team['team_name']}
--------------------
Total Players: {team['total_players']}
Average Height: {team['average_height']}

Players on Team: {team['player_names']}
Experienced Players: {team['experienced_players_total']}
Inexperienced Players: {team['inexperienced_players_total']}

Guardian Names: {team['guardian_names']}


""")
    input("Hit ENTER to continue...")


def init():
    teams = TEAMS.copy()
    players = clean_data(PLAYERS)
    balanced_teams = balance_teams(teams, players)
    intro_msg()
    while True:
        team_index = get_user_selected_team(balanced_teams)
        display_team_stats(balanced_teams[team_index])


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    init()
