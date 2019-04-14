#The Guessing Game.

#Write a program that generates a random number between 1 and 10 and let’s
#the user guess what number was generated. The result should be sent back
#to the user via a print statement.

import random
RandomVaried = random.randint(0,10)
while True:
    
    UserGuess = int(input("try to guess the number from 0 to 10 :"))
    
    if UserGuess>=0 and UserGuess <= 10:
        if UserGuess > RandomVaried:
            print("Less")
        elif UserGuess < RandomVaried:
            print("more")
        else: print("BINGO")
    else:print("wrong number")
    if(input("q for try again") !='q'): break