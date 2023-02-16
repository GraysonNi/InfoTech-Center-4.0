# Programer: Grayson Nichols
# Date: 2.16.2023
# Program: Infotech Center Upgrades

import random

def tirePressure():
  pressures = ["left front", "right front", "left back", "right back", "none"]
  tireState = random.choice(pressures)
  return(tireState)

tireStatus = tirePressure()

def pressureSensor():
    if tireStatus == "left front":
        print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
    elif tireStatus == "right front":
        print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
    elif tireStatus == "left back":
        print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
    elif tireStatus == "right back":
        print("\nYour", tireStatus, "tire has a low pressure, please fill it soon.")
    else:
        print("\nAll of your tires are at safe pressures.")

pressureSensor()