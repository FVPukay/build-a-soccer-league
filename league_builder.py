# Teamtreehouse.com Python Web Development Program
# Project 1: Build a Soccer League
# Note: This is designed to work with Python 3

def league_builder():
    import csv

    player_list = []
    experienced = []
    inexperienced = []

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
