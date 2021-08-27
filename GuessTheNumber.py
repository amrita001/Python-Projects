def guess_the_number(secret_number): # Function to guess the correct number
    count = 1
    while (count <= 3):   # As game is giving only 3 chances so count is limited to 3
        user_num = int(input("\n\tGuess the number "))        # asking for the number
        if (user_num == secret_number):
            print("\n\tYou have correctly guessed it! :D")
            return 1       # To display only the 'Thanks for playing' part
            
        elif (user_num >= secret_number):
            print("\tToo high. ")
        
        else:
            print("\tToo low. ")
        count += 1
    return 0  # If returns 0 then user haven't won, else 1 means user have WON :)


#-- Execution starts from here --
#For Decoration purpose
print("\nWELCOME TO GUESSING GAME!")  # INTRO
print("------------------------------\n"+"\tHello User, \n\tKindly enter your name")
user_name = input("\n\tName: ")
print("\n------------------------------------------------------------------------\n" +
      "\tHere are the Rules: \n1. You will get 3 chances to guess the secret number" +
      "\n2. If you lose those 3 chances you will have to start again. Good luck!" +
      "\n------------------------------------------------------------------------")


secret_number = 7   # secret number which the user have to guess

won = guess_the_number(secret_number)  # User playing for the first time


if(won == 0):   # Checking if user have lost or not based on that 2nd chance will be given
    another_chance = input("\nThat's it " + user_name.title().split()[0] + "! Would you like to play again? (Yes/No) ")
    
    while(another_chance.lower()!="no"): # Until user gives a "NO" game will be continued
        stats = guess_the_number(secret_number) # Stats is same as won variable
        
        if(stats == 0): # Again checking if user has lost or not, if the user has then he'll be taken out of the loop
            another_chance = input("\nThat's it " + user_name.title().split()[0] + "! Would you like to play again? (Yes/No) ")
        else:
            break

print("\n--------------------------------------------------------\n \tThanks for playing " + user_name.title().split()[0]  + "! :) \n--------------------------------------------------------")
