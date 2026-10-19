#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: Oct 2026
# This program asks the user to enter an integer and checks if it is positive, negative, or zero


def main():
    # # if ... then ... elseif ... else example
    user_input = int(input("Enter an integer: "))

    if user_input > 0:
        print(f"{user_input} is a positive number.")
    elif user_input < 0:
        print(f"{user_input} is a negative number.")
    elif user_input == 0:
        print(f"{user_input} is a just zero.")
    else:
        print(f"{user_input} is no idea.")


if __name__ == "__main__":
    main()
