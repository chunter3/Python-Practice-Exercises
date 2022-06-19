# Given a string, find the length of the longest substring without repeating characters.

def length_of_longest_substring(string):
    
    substring_lst = []

    substring = ""

    for char in list(string):

        if char in substring:

            substring_lst.append(substring)

            substring = f"{char}"

            continue

        substring = f"{substring}{char}"

        substring_lst.append(substring)

    if substring_lst:  # checks if the list is not empty
        
        print(f"The longest non-repeating substring is {max(substring_lst, key=len)} with a length of {len(max(substring_lst, key=len))}")

    else:

        print(f"The longest non-repeating substring is {substring} with a length of {len(substring)}")


def main():

    while(True):
        
        string = input("Input a string: ")
        
        length_of_longest_substring(string)

        cont = input("Continue? ('y' or 'n'): ")

        if cont == 'n':

            break

if __name__ == "__main__":
    main()