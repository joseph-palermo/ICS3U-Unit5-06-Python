#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program takes a number and rounds it


def rounding(number, decimal_point):
    # this function takes a number and rounds it

    # process
    rounded_number = (number[0]*(10**decimal_point))
    rounded_number = rounded_number + 0.5
    rounded_number = int(rounded_number)
    rounded_number = rounded_number/(10**decimal_point)

    return rounded_number


def main():
    # this function gets a number from the user and outputs the rounded number

    rounding_number = []

    # process
    while True:
        user_number = input("Enter the number you want to be rounded: ")
        decimal_place = input("Enter how many decimals you want left: ")

        try:
            user_number = float(user_number)
            decimal_place = int(decimal_place)
            rounding_number.append(user_number)
            if user_number == float(user_number) and \
               decimal_place == int(decimal_place):
                user_rounded_number = rounding(rounding_number, decimal_place)
                print("")
                print("The rounded number is: ", user_rounded_number)
                break
            else:
                print("")
                print("Please insert a number")
                break
        except Exception:
            print("")
            print("Please insert a number")
            break


if __name__ == "__main__":
    main()
