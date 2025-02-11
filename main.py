# Programmer: Bella Picasso-Kennedy 
# Purpose: CS 326 Midterm - Palindrome Checker in Python

def menu():
    print("--- PALINDROME CHECKER! ---")
    print("Palindrome Defintion: a word, phrase, or sequence that reads the same backward as forward")
    print("----------------------------")
    print("1. Check to see if a word is a palindrome")
    print("2. Exit ")
    print("Enter your choice: ", end= "")  # source: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ 

def user_input():
    response = input()
    return response

def is_palindrome(s): # same logic used as the c++ program
    s = s.lower() # convert string to all lowercase, so the program is not case-sensitive, source: https://www.geeksforgeeks.org/python-string-lower/?ref=header_outind 
    s = s.replace(" ", "") # removes spaces in between phrases! ex. nurses run -> nursesrun, source: https://www.geeksforgeeks.org/python-string-replace/ 
    n = len(s)
    for i in range(n//2): # for integer division, would not accept a float, resulted in runtime error
        if s[i] != s[n - i - 1]: 
            return False
    return True

def main():
    while True: # python syntatically does not support a do while loop! this works to mimic do while loop behavior, source: https://www.geeksforgeeks.org/python-do-while/?ref=header_outind 
        menu()
        choice = int(user_input())
        while choice < 1 or choice > 2:
            print("Invalid option! Try again: ", end= "")
            choice = int(user_input())
        if choice == 1: # user wants to enter a word, phrase, or sequence!
            print("Enter a word to check if it's a palindrome: ", end= "")
            input = user_input()
            palindrome = is_palindrome(input)
            if palindrome:
                print(input.strip(), "is a palindrome! :)\n")
            else:
                print(input.strip(), "is not a palindrome... :(\n")
        else:
            print("Goodbye! :)")
            break
if __name__ == "__main__":
    main()