#!/usr/bin/env python3


# Created by: Joanna Keza
# Date: March 7, 2025
# This program asks the user for the major radius
# and minor radius of a Torus, then calculates
# the surface area and volume using TAU and PI

import math

# Greeting card
def main ():
    print ("********************************")
    print ("*                              *")
    print ("*       Welcome user !         *")
    print ("*                              *")
    print ("*******************************\n")

    def main ():
        # Get the user input for major and minor radius
        R = float(input("Enter the major radius: "))
        r = float (input("Enter the minor radius: "))

        # Calculate the surface area and volume 
        Volume = math.TAU ** 2 * R * r **2  # ** represents exponent
        Area = 4 * math.PI ** 2 * R * r  # ** represents exponent

if __name__ == "__main__":
    main()