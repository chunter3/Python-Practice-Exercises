# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old

from datetime import date

def char_input():

    curr_date = date.today()

    name = input("Enter your name: ")

    age = input("Enter your age: ")

    while int(age) <= 0 or int(age) > 100:  # Negative ages or ages greater than 100 are considered invalid

        age = input("Invalid age. Enter your age again: ")

    print(f"Hello {name}. You will be 100 years old in {curr_date.year + (100 - int(age))}.")


def main():

    char_input()
    
if __name__ == "__main__":
    main()