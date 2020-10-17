import random
game_active = True

print("Welcome To Guess The Number!!")
def main():
    global game_active
    num = random.randint(1, 100)
    Tries = 1
    while game_active:
        user_guess = int(input("Guess a number 1-100:"))

        if user_guess == num:
            print("Congratulations, you guessed it right!") 
            print(f"Number of tries:{Tries}")
            game_active = False

        elif user_guess > num:
            print("Guess Lower")
            Tries += 1

        elif user_guess < num:
            print("Guess Higher")
            Tries += 1

main()

while game_active:
    replay = input("Do you want to play again?Enter Y/N:")
    if replay.lower() == "y":
        main()
    else:
        game_active = False

      