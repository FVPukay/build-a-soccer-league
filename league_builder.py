# Teamtreehouse.com Python Web Development Program
# Project 1: Build a Soccer League
# Note: This is designed to work with Python 3

def league_builder():
    import csv

    player_list = []
    experienced = []
    inexperienced = []

    sharks = []
    dragons = []
    raptors = []

    sharks_first_practice = 'September 1, 2018'
    dragons_first_practice = 'September 2, 2018'
    raptors_first_practice = 'September 3, 2018'

    def assign_to_team(team_1, team_2, team_3, copy):
        team_1.append(copy.pop())
        team_2.append(copy.pop())
        team_3.append(copy.pop())

    def write_to_file(team_str, team_list):
        file.write(team_str)
        file.write('\n')
        for player in team_list:
            file.write(', '.join(player))
            file.write('\n')
        file.write('\n\n')

    def create_welcome_letter(team_list, first_practice, team_str):
        for player in team_list:
            full_name = player[0].split(' ')
            file_name = '_'.join(full_name) + '.txt'
            with open(file_name, 'w') as file:
                file.write('Dear ' + player[2] + ',' + '\n\n')
                file.write('Congratulations! ' + player[0] +
                           ' is on the ' + team_str + '!\n')
                file.write('The first practice is on ' + first_practice + '.')

    # Read the data from the supplied csv file.
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.reader(csvfile, delimiter=',')
        player_list = list(player_reader)

    # Store the data in an appropriate data type for the next task.
    for row in player_list:
        if row[2] == 'YES':
            experienced.append(row)
        elif row[2] == 'NO':
            inexperienced.append(row)
    # Remove height
    else:
        for row in experienced:
            del row[1]
        for row in inexperienced:
            del row[1]

    # Iterate through all 18 players and assign them to teams such that each
    # team has the same number of players and such that the number of
    # experienced players on each team is also the same.

    experienced_copy = experienced[:]
    inexperienced_copy = inexperienced[:]

    while experienced_copy:
        try:
            assign_to_team(sharks, dragons, raptors, experienced_copy)
        except IndexError as error:
            print(error)
    else:
        while inexperienced_copy:
            try:
                assign_to_team(sharks, dragons, raptors, inexperienced_copy)
            except IndexError as error:
                print(error)

    # Output a text file called teams.txt that contains the league roster
    # listing the team name, and each player on the team including the player's
    # information: name, whether they've played soccer before and their
    # guardians' names.

    with open('teams.txt', 'w') as file:
        write_to_file('Sharks', sharks)
        write_to_file('Dragons', dragons)
        write_to_file('Raptors', raptors)

    # Create 18 welcome letter text files to the player's guardians.
    create_welcome_letter(sharks, sharks_first_practice, 'Sharks')
    create_welcome_letter(dragons, dragons_first_practice, 'Dragons')
    create_welcome_letter(raptors, raptors_first_practice, 'Raptors')

# Make sure the script does not execute when imported.
if __name__ == '__main__':
    league_builder()
