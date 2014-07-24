##Importing all the required modules
import string
from random import randint
import List
import HangmanMods

##Global variables
lenList = len(List.countries)
compVal = None
prompt = 'Y'
count = 0

##Outermost loop, looping through the main list
while count < lenList :
    if prompt.upper() == 'Y' :         ##Confirmation regarding continuing the game : YES
        
        compVal = HangmanMods.randVal(0,lenList-1,List.countries)       ##Getting the computer's value
        compList = list(compVal)
        
        userVal = '_'*len(compVal)      ##Initialising the user's value
        userList = list(userVal)

        if " " in compVal :
            userList[compList.index(" ")] = " "     ##Adding a " " in the user's value for the same in the computer's value

        userVal = string.join(userList)     ##Joining it back and printing for the user to know the total number of characters
        print userVal

        lives = 10        ##Maximum number of lives 
        flag = 1

        ##User input
        temp = HangmanMods.userInput()

        word = 0        ##Number of correct characters entered
            
        ##Comparison
        while word < len(compVal) and lives > 0 and userVal != string.join(compList):     ##Looping for a particular value of userVal as long as one of the conditions doesn't fail            
            if temp in compVal:
                i = 0       
                while i < len(compVal) :      ##Adding this letter to the user value
                    if temp == compList[i] :
                        userList[i] = temp
                    i+=1                
                word+=1
                userVal = string.join(userList)
                print "\nCorrect. It's there \n"
                print userVal + "\n"                
                ##Checking if the words are the same
                if userVal == string.join(compList) :
                    print "Excellent. You guessed it right. \n"
                else :
                    temp = HangmanMods.userInput()
                    continue                
            else:
                print "\nNo. Not there\n"
                lives -=1
                print "You have " + str(lives) + " tries left\n"
                userVal = string.join(userList)
                print userVal + "\n"
                temp = HangmanMods.userInput()
                continue
                if userVal == string.join(compList) :
                    print "Excellent. You guessed it right. \n"
                    break
                
        prompt = raw_input("\nDo you want to continue the game? Answer Y or N : \n")
    elif prompt == 'N' or prompt == 'n' :       ##Confirmation regarding continuing the game : NO    
        break
    else :      ##Confirmation regarding continuing the game : NOT APPLICABLE
        print "Enter a valid value"
        prompt = raw_input("\nDo you want to continue the game? Answer Y or N : \n")
    count+=1



  
    





    



