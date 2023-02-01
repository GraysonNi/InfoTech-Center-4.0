# Programer: Grayson Nichols
# Date: 1.20.2023
# Program: Infotech Center 4.0 - Gasoline

"""
We will create a Function that will tell us our Fuel gauge level
   - Create a list with Gas Levels
   - Randomize and choose from the list to determine our gas level

create a Function to determine our closest Gas Station
   - Create a list of gas stations
   - Randomly choose a gas station from the list

Create s Function to determine our gas level and closest gas station
   - Print Gas level
   - Print Closest Gas Station
"""

# Import Libraries Here
import random
from time import sleep


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Varianle calling gasLevelGaugev function to store its value
gasLevelIndicator = gasLevelGauge()

# List of gas stations Function
def listOfGasStations():
   gasStations = ["Shell","Costco","Buc-ee's","Speedway","7-11","Circle-K","Meijer","Marathon"]
   gasStationNearby = random.choice(gasStations)
   return gasStationNearby

# Determine Gas Level & closest gas station
def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),2)
    milesToGasStationQuarterTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print("***WARNING YPU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")