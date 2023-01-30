# Programer: Grayson Nichols
# Date: 1.20.2023
# Program: Infotech Center Upgrades

"""
Our Welcome Screen will start our program letting
drivers know that the Infotech Center 4.0 OS is loading
"""

# Import Libraries Here
import time
import sys

timeToSleep = 2
x = 0
a = 0



print("\n\nWelcome - InfotechCenter 4.0\n")
time.sleep(timeToSleep)
#print("\nInfotech Center 4.0 OS is now loading")

while x != 20:
    x += 1
    b = ("\033[1;33;40m Infotech center is now loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b)
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x ==20:
        print('\033[1;32;40;40m Retina Scan Complete - Access Granted!')