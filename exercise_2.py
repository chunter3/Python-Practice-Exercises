# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

#Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def odd_or_even():

    while True:
        
        try:
            
            user_num = int(input("Enter a number: "))
            break
            
        except ValueError:
            
            print("You did not input a number. Please try again\n")

    if user_num % 4 == 0:

        print("Your number is even and a multiple of 4\n")

    elif user_num % 2 == 0:

        print("Your number is even\n")
    
    else:

        print("Your number is odd\n")

    while True:

        try:
            
            num = int(input("dividend: "))
            
            check = int(input("divisor: "))

            break
        
        except ValueError:

             print("You did not input a number. Please try again\n")

    try:

        if num % check == 0:

            print(f"{num} divides evenly into {check}")

        else:

            print(f"{num} does not divides evenly into {check}")

    except ZeroDivisionError:

        print("Division by zero!")


def main():

    odd_or_even()
    
if __name__ == "__main__":
    main()
