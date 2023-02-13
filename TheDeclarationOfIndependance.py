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


# VRS() to respond to the weather conditions
def vehicleResponceSystem():
    if weatherAlert == "Snow":
        print("\nNWS has changed your Alarm by 15 minutes because of the weather forcast of", weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "Blizzard":
        print("\nNWS has changed your Alarm by 30 minutes because of the weather forcast of", weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 35 MPH")
    elif weatherAlert == "Rain":
        print("\nNWS is calling for", weatherAlert, ", please drive extra careful")
    elif weatherAlert == "Fog":
        print("\nNWS is calling for", weatherAlert, ", please drive extra careful")
    elif weatherAlert == "Windy":
        print("\nNWS is calling for", weatherAlert, "conditions, please drive extra careful")
    elif weatherAlert == "Icy":
        print("\nNWS has changed your Alarm by 60 minutes because of the weather forcast of", weatherAlert)
        print("VRS has been engaged only allowing your vehicle to go 25 MPH")
    else:
        print("\nNWS is calling for", weatherAlert,"drive safely and have a wonderful day!")

vehicleResponceSystem()