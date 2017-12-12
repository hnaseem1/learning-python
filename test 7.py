# Tells if a string entered is a Palindrome or not example: OPPO is a palindrome

string = str(raw_input("Enter a Word: ").lower())

bstring = string[::-1]

if string == bstring:

    print "This is a Palindrome"

else:
    print "This is NOT a Palindrome"


