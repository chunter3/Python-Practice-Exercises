# Take a numeric list and write a program that prints out all the elements of the list that are less than 5

#Extra:

# Make a new list that has all the elements less than 5 from this list in it and print out this new list
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user

def lst_less_than_five(int_lst, user_input):

        print(f"Original list: {int_lst}")
        
        print(f"List w/ only elements less than 5: {[x for x in int_lst if x < 5]}")
        
        print(f"List w/ only elements less than {user_input}: {[x for x in int_lst if x < user_input]}")


def main():

    try:

        int_lst = [int(x) for x in input("Enter the elements in the list: ").split()]

        user_input = int(input("Enter one last number: "))

        lst_less_than_five(int_lst, user_input)

    except ValueError:

        print("Given list contains a non-numeric value. Exiting")
    
if __name__ == "__main__":
    main()