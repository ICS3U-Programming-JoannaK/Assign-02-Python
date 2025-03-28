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
    print(
        "The major radius should be larger than "
        "the minor radius.\n"
    )
    major_radius = float(input("Enter the major radius: "))
    minor_radius = float(input("Enter the minor radius: "))
    unit = input("Enter the units (m, cm, etc): ")

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

    # Display information on the shape
    print("\n")
    print("------More on the Torus shape------")
    print("A Torus is a 3D shape that resembles a donut. It has two radius:")
    print(
        "1. Major Radius (R): This is the distance from \n"
        "the center of hole to the center of the tube\n"
    )
    print("Minor radius (r): This is the radius of the tube itself")
    print("the distance from the center of the" "tube to the surface of the Torus\n")
    print("Thank you for using the Torus calculator ! Goodbye!\n")

    # display exit message
    print("\033[1;35m")
    print("***********************************")
    print("*                                 *")
    print("* Thank you for using my program !*")
    print("*                                 *")
    print("***********************************\n")


if __name__ == "__main__":
    main()
