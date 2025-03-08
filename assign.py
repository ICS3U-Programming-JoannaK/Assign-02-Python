#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 7, 2025
# This program asks the user for the major radius
# and minor radius of a Torus, then calculates
# the surface area and volume using TAU and PI

import math

def main():
    # Greeting card
    print("********************************")
    print("*                              *")
    print("*       Welcome user !         *")
    print("*                              *")
    print("********************************\n")
    
    # Get the user input for major and minor radius
    major_radius = float(input("Enter the major radius: "))
    minor_radius = float(input("Enter the minor radius: "))

    # Calculate the surface area and volume
    volume = math.tau**2 * major_radius * minor_radius**2  # ** represents exponent
    area = 4 * math.pi**2 * major_radius * minor_radius  # ** represents exponent
    
    # display surface area and volume
    print("Volume of the Torus: {:,.2f}".format(volume))
    print("Area of the Torus:  {:,.2f}".format(area))

if __name__ == "__main__":
    main()
