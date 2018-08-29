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
            sharks.append(experienced_copy.pop())
            dragons.append(experienced_copy.pop())
            raptors.append(experienced_copy.pop())
        except IndexError as error:
            print(error)
    else:
        while inexperienced_copy:
            try:
                sharks.append(inexperienced_copy.pop())
                dragons.append(inexperienced_copy.pop())
                raptors.append(inexperienced_copy.pop())
            except IndexError as error:
                print(error)

    # Output a text file called teams.txt that contains the league roster
    # listing the team name, and each player on the team including the player's
    # information: name, whether they've played soccer before and their
    # guardians' names.

    with open('teams.txt', 'w') as file:
        file.write('Sharks')
        file.write('\n')
        for player in sharks:
            file.write(', '.join(player))
            file.write('\n')
        file.write('\n\n')
        file.write('Dragons')
        file.write('\n')
        for player in dragons:
            file.write(', '.join(player))
            file.write('\n')
        file.write('\n\n')
        file.write('Raptors')
        file.write('\n')
        for player in raptors:
            file.write(', '.join(player))
            file.write('\n')

# Make sure the script does not execute when imported.
if __name__ == '__main__':
    league_builder()
