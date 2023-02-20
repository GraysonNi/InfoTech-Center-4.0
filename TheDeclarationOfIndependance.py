# Programer: Grayson Nichols
# Date: 2.17.2023
# Program: Infotech Center Upgrades

# Import Libraries Here
import time
import random

def station():
    stationGenre = ["Hip-Hop", "Pop", "Country", "Latin", "Rock", "Electronic", "Heavy Metal"]
    newStation = random.choice(stationGenre)
    return newStation
currentStation = station()

def radio():
    if currentStation == "Hip-Hop":
        print("\n You are now listening to", currentStation, "Radio.")
    elif currentStation == "Pop":
        print("\n You are now listening to", currentStation, "Radio.")
    elif currentStation == "Country":
        print("\n You are now listening to", currentStation, "Radio.")
    elif currentStation == "Latin":
        print("\n You are now listening to", currentStation, "Radio.")
    elif currentStation == "Rock":
        print("\n You are now listening to", currentStation, "Radio.")
    elif currentStation == "Electronic":
        print("\n You are now listening to", currentStation, "Radio.")
    else:
        print("\n You are now listening to", currentStation, "Radio.")
radio()