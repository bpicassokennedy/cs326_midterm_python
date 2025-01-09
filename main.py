# Programmer: Bella Picasso-Kennedy 
# Purpose: CS 326 Midterm - Palindrome Checker 

def user_input():
    word = input("Enter a word to check if it's a palindrome: ")
    word = word.strip() # returns new string with leading and trailing spaces removed
    return word

def is_palindrome(s): # same logic used as the c++ program
    n = len(s)
    for i in range(n//2): # for integer division, would not accept a float, resulted in runtime error
        if s[i] != s[n - i - 1]:
            return False
    return True

def main():
    input = user_input()
    palindrome = is_palindrome(input)
    if palindrome:
        print(input, "is a palindrome! :)")
    else:
        print(input, "is not a palindrome :(")
if __name__ == "__main__":
    main()