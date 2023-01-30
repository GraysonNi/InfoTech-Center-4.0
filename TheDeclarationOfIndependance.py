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


# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


print(gasLevelGauge())


