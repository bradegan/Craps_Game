'''
    CS5001
    Fall 2018
    HW3
    Brad Egan
'''

'''
    I made sure this program would work by thoroughly testing this program by
making sure it behaved appropriately for various scenarios. I made sure to test
what would happen when I lost the bet, and making sure the program would quit
at the appropriate time. I also used a ton of print statements to validate the
inputs and outputs and make sure the bet reset to 10 after each roll. I also
made the user lose by modifying the rolls manually. Bankroll and bet size was
also modified for different scenarios.

'''


# Import random module.
import random

def main():
    # Define variables, as well as what count as a win or loss.
    bankroll = 100
    bet_size = 10
    win_list = [7, 11]
    lose_list = [2, 3, 12]

    # Nest program in a while loop to keep program running while positive
    # bankroll.
    while bankroll > 0:
        
        # Print menu of choices.
        print("Choose from the following options:")
        print("P: Print status.")
        print("B: Make a bet.")
        print("R: Roll the dice.")
        print("Q: Quit the game and leave the casino.")
        choice = str.upper(input("Enter your selection from the menu.\n"))
        # If user enters Q then program quits and breaks out of while loop.
        if choice == "Q":
            print("Quitting............................................")
            break
        
        # Prints, bankroll, bet size and directions.
        elif choice == "P":
            print ("Bank: $%i" % bankroll)
            print ("Current bet: $%i \n" % bet_size)
            print("Step right up! Roll two dice and add the values together.")
            print("Lucky 7 or 11 wins.")
            print("Snake-eyes, cross eyes, and box cars all lose.")
            print("Anything else, you don't lose any $ but you don't win any either. \n")

        # If user hits B it prints bankroll and prompts for bet input.
        elif choice == "B":
            print("You have $%i" % bankroll)
            while True:
                # Bet input validation. If user doesn't
                bet_input = int(input("Please enter a bet amount: $"))
                if (bet_input >= 1 and bet_input <= bankroll):
                    bet_size = bet_input
                    print("Thank you, your bet size is now $%i" % bet_size)
                    print("")
                    break
                else:
                    print("You need to bet at least $1 and no more than your "
                          "current bank, which is $%i" % bankroll)
                    
        # This is the roll logic module. Rolls a random integer between 1 and 6
        elif choice == "R":
            roll_1 = random.randint(1,6)
            roll_2 = random.randint(1,6)
            # Prints what the dice rolled.
            print("Roll 1 is", roll_1)
            print("Roll 2 is %i \n" % roll_2)
            # Checks if total of rolls are a win and adds bet to bankroll.
            if (roll_1 + roll_2) in win_list:
                bankroll += bet_size
                print("YOU WON $%i \n" % bet_size)
            # Checks if total of rolls are a loss and subracts bet from bankroll
            elif (roll_1 + roll_2) in lose_list:
                bankroll -= bet_size
                print("YOU LOST $%i \n" % bet_size)
            # If it is not a win or loss it a draw.
            else:
                print("DRAW! \n")
            # Makes sure default betsize is either 10 or your bankroll, whatever
            # is smaller.
            bet_size = min(10, bankroll)
            
        # If user does not enter P, B, R, or Q then input was an error.    
        else:
            print("I'm sorry, your input was an error, pick a valid choice.\n")
            
    # Prints how much you are leaving the casino with
    print("You're leaving the casino with $%i" % bankroll)


main()
