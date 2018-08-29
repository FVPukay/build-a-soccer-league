# Teamtreehouse.com Python Web Development Program
# Project 1: Build a Soccer League
# Note: This is designed to work with Python 3

def league_builder():
    import csv

    player_list = []

    # Read the data from the supplied csv file.
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.reader(csvfile, delimiter=',')
        player_list = list(player_reader)
