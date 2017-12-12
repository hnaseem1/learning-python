# creating a guessing game using random


import random
def main():
    a = random.randint(1, 9)
    b = int(input("I am thinking about a number between 1 and 9, can you guess? ----> "))
    b = b - a

    if b == 0:
        print "Yes that is correct"

    elif b == -1 or b == 1:
        print "close!"

    elif b == -3 or b == 3 or b == -4 or b == 4 or b == -2 or b == 2:
        print "too low!"

    elif b == -5 or b == 5 or b == -6 or b == 6:
        print "too high!"

    else:
        print "You have not entered a number between 1 and 9"
        main()
    
    print "I was thinking"
    print a
            
    main()
main()
   

