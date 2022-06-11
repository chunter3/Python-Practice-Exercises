# Exercise from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old

# Extras:

# Ask the user for another number and print out that many copies of the previous message
# Print out that many copies of the previous message on separate lines

from datetime import date

def char_input():

    curr_date = date.today()

    name = input("Enter your name: ")

    age = int(input("Enter your age: "))

    while age <= 0 or age > 100:  # Negative ages or ages greater than 100 are considered invalid

        age = int(input("Invalid age. Enter your age again: "))

    numOfMsgs = int(input("How many copies of the message do you want (default = 1): "))

    if numOfMsgs > 1:

        for x in range(numOfMsgs):

            print(f"\nHello {name}. You will be 100 years old in {curr_date.year + (100 - int(age))}.\n")

    else:
        
        print(f"\nHello {name}. You will be 100 years old in {curr_date.year + (100 - int(age))}.")


def main():

    char_input()
    
if __name__ == "__main__":
    main()