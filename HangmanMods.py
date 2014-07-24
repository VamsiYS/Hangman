from random import randint
import string


##function to return a random value from the list
def randVal(a,b,L) :
    x = randint(a,b)
    return L[x]

##function to get input and ensure it is a letter
def userInput() :
    flag = 1
    a = raw_input("\nEnter your guess: \n")
    a = a.upper()
    while a not in string.ascii_uppercase :
        print "Enter a single letter"
        a = userInput()           
    return a
