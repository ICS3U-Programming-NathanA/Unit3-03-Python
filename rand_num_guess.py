#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 5 2022
# This program asks the user for a number between 0 and 9 and then sees if they got the same number as the computer


import random


def main():
    # generates a number between 0 and 9
    random_num = random.randint(0, 9)

    # Get the the number they guessed
    user_num = int(input("Enter a number between 0 and 9: "))

    # An If statement to see if they got the same number as the generated number then display the results
    if random_num == user_num:
        print("You guessed the correct number")
    else:
        print("You guessed the wrong number")


if __name__ == "__main__":
    main()
