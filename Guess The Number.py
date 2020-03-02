import sys
import random
print("Welcome To Guess The Number!!")
print("The objective is to guess the right number between 1 and  ")
print("The  first one to get five points wins!")



def main():
    #function repeats the program until one person gets five points 
    human_p = 0
    computer_p = 0
    while human_p < 5 and computer_p < 5:
        
        #Deck for card values
        my_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35
        ,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        
        print("\n")
        print("Deck")
        print(my_deck)

        mystery_number1 = random.randint(1, 50)
        #input your guess according to the deck

        Usr_Guess = int(input("\nEnter your guess--->\n"))
    
        if Usr_Guess == mystery_number1:
            print("Congratulations, you guessed it right!")
            human_p = human_p + 1
            print("\n")
            print("Statistics")
            print("Your points: %s" % human_p)
            print("Computer's points: %s" % computer_p)
            print("Now it is the computer's turn to guess")

        else:
            print("Wrong!")
            print("The answer was %s" % mystery_number1)
            print("\n")
            print("Statistics")
            print("Your points: %s" % human_p)
            print("Computer's points: %s" % computer_p)
            print("Now it is the computer's turn to guess")
        
        print("\n")
        print("Computer's Turn")

        computer_guess = random.randint(1, 50)
        print("The computer guessed %s" % computer_guess)

        if computer_guess == mystery_number1:
            print("The computer guessed it right!")
            computer_p = computer_p + 1
            print("\n")
            print("Your points: %s" % human_p)
            print("Computer's points: %s" % computer_p)

        else:
           print("The computer guessed wrong")
    
    print("\n")
    print("Final Score:")
    print("Your points: %s" % human_p)  
    print("Computer's points: %s" %computer_p)

#function tells who won the game
    if human_p > computer_p:
       print("\nGood job you won the game!\n")

    elif human_p < computer_p:
       print("\nBetter luck next time!\n")
       print("The computer won")

    else:
       print("\nIt was a tie!\n")

main()
user_input = str(input("Do you want to play again? Please enter yes or no --->"))

#Function runs the whole game if the user inputs yes    
if user_input == 'yes':  
        main()

else: 
    sys.exit()
