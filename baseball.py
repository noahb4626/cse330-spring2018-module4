
import sys, os
import re # import regex package


# usage message setup
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")
filename = sys.argv[1]
if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

# constructor for Player class
class Player:
    # Player has a name, # of at-bats, and # of hits
    def __init__(self, name, bats, hits):
        self.name = name
        self.bats = bats
        self.hits = hits

    # average function calculates hits/bats (called once entire file has been combed)
    def average(self):
        return self.hits / self.bats

    # tostring method for Player
    def __str__(self):
        return f"{self.name}: {self.average():.3f}" #:.3f - 3 digits after decimal point

# regular expression that matches name, # bats, # hits
player_regex = re.compile(r"(\w+ \w+) batted (\d+) times with (\d+) hits")


# create an empty dictionary that stores players
players = {}

with open(filename) as f:
    for line in f:
        # use regex on each line to search for player data
        match = player_regex.search(line)
        # if a line does not contain player info, move on to next line
        if match is None:
            continue
        # fill name, bats, hits info with results from reg ex
        name, bats, hits = match.groups()
        # cast bats and hits as integers (they will be read in as strings)
        bats, hits = int(bats), int(hits)
        # if name is not in players dictionary, add to dictionary
        if name not in players:
            players[name] = Player(name, bats, hits)
        # if player has already been added to dictionary, update their bats & hits values
        else:
            players[name].bats += bats
            players[name].hits += hits

# iterate through all players (sorted by batting average in descending order)
# print name & batting average
for player in sorted(players.values(), key=lambda x: x.average(), reverse=True):
    print(player)
