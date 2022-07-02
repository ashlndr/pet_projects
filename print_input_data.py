print("Test list of commands:\n")

teams_list = ("test_team_1", "test_team_2")  # set of commands names


def input_team_name():
    print(teams_list)
    team = input("Enter team name: ")
    while team not in teams_list:
        print(f'{team} not in a team list.\n'
              f'{teams_list}')
        team = input("Reenter your team name: ")
    return team


def input_quarter():
    quarter = input("Quarter of evaluation: ")
    return quarter


def input_due_date():
    due_date = input("Enter due date: ")
    return due_date
