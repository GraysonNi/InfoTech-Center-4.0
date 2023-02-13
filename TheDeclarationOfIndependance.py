# Programer: Grayson Nichols
# Date: 2.8.2023
# Program: Weather System Updates

#Import libraries here
import random

#Create weather conditions in a list and choose it randomly
def weather():
    weatherForcast = ["Snow", "Blizzard", "Rain", "Fog", "Windy", "Icy", "Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once in our VRS
weatherAlert = weather()

print(weatherAlert)

# VRS() to respond to the weather conditions
def vehicleResponceSystem():
    if weatherAlert == "Snow":
        