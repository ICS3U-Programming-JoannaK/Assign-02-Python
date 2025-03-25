#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 7, 2025
# This program asks the user for the major radius
# and minor radius of a Torus, then calculates
# the surface area and volume using PI

import math


def main():
    # Display greeting card in purple
    print("\033[1;35m")  # This sets the greeting card to purple

    # greeting card
    print("***********************************")
    print("*                                 *")
    print("* Welcome to the Torus calculator!*")
    print("*                                 *")
    print("***********************************\n")

    # rest color to default
    print("\033[0m")

    # Get the user input for major and minor radius
    major_radius = float(input("Enter the major radius: "))
    minor_radius = float(input("Enter the minor radius: "))
    unit = input("Enter the units (m, cm, etc): ")

    # check if the major radius is greater than the minor radius
    if major_radius < minor_radius:
        print(
            "Error: The major radius should be larger than "
            "the minor radius. Please try again.\n"
        )  # This will show if minor radius is greater than major radius

    # calculate the volume and area
    volume = 2 * math.pi**2 * major_radius * minor_radius**2  # ** represents exponent
    area = 4 * math.pi**2 * major_radius * minor_radius  # ** represents exponent

    # display surface area and volume
    print("Volume of the Torus: {:,.2f}({}^3)".format(volume, unit))
    print("Area of the Torus: {:,.2f}({}^2)".format(area, unit))

    # Display the formulas used
    print("\n")
    print("Formulas used:")
    print("Volume = 2π2Rr2")
    print("Area = 4π2Rr")

    # display exit message
    print("\033[1;35m")
    print("***********************************")
    print("*                                 *")
    print("* Thank you for using my program !*")
    print("*                                 *")
    print("***********************************\n")


if __name__ == "__main__":
    main()
