# Programmer: Bella Picasso-Kennedy 
# Purpose: CS 326 Midterm - Palindrome Checker 

def menu():
    print("--- PALINDROME CHECKER! ---")
    print("Palindrome Defintion: a word, phrase, or sequence that reads the same backward as forward")
    print("----------------------------")
    print("1. Check to see if a word is a palindrome")
    print("2. Exit ")
    choice = input("Enter your choice: ") # reads in as a string, needs to be converted to an int so the while loop condition executes correctly
    choice = int(choice)
    while choice != 1 and choice != 2:
        choice = input("Invalid option! Try again: ")
        choice = int(choice)
    return choice

def user_input():
    word = input("Enter a word to check if it's a palindrome: ")
    word = word.strip() # new string with leading and trailing spaces removed!
    return word

def is_palindrome(s): # same logic used as the c++ program
    s = s.lower() # convert string to all lowercase, so the program is not case-sensitive
    s = s.replace(" ", "") # removes spaces in between phrases! ex. nurses run -> nursesrun
    n = len(s)
    for i in range(n//2): # for integer division, would not accept a float, resulted in runtime error
        if s[i] != s[n - i - 1]:
            return False
    return True

def main():
    while True: # python syntatically does not support a do while loop! this works to mimic do while loop behavior
        choice = menu()
        if choice == 1: # user wants to enter a word, phrase, or sequence!
            input = user_input()
            palindrome = is_palindrome(input)
            if palindrome:
                print(input, "is a palindrome! :)\n")
            else:
                print(input, "is not a palindrome :(\n")
        else:
            print("Goodbye! :)")
            break
if __name__ == "__main__":
    main()