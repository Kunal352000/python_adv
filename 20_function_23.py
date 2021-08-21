"""
create a function to check wheather given string object is palindrome or not?
"""
string=input("Enter the string: ")
def is_palindrome(x):
    if x==x[::-1]:
        print("given string is palindrome")
    else:
        print("given string is not palindrome")
is_palindrome(string)
"""
output:
-------
Enter the string: 'kunal'
given string is not palindrome


Enter the string: 'tttt'
given string is palindrome
"""
