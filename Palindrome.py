string1 = input("enter the string")


string1 = string1.casefold()

rev_str = reversed(string1)

print()

if list(string1) == list(rev_str):
    print("The string is a palindrome")
else:
    print("this string is not a palindrome")