import sys
import random

while True:
    print("Choose an option:")
    print("1. Easy (1-50), guess limit 10")
    print("2. Medium (1-100) guess limit 20")
    print("3. Hard (1-500) guess limit 40")
    print("4. Exit Game")

    difficulty = input()
    upper_range = None
    guess_limit = None
    guess_counter = 0
    games_played = 0
    games_won = 0
    best_score = 0
    average_guess = 0

    match difficulty:
        case "1":
            upper_range = 50
            guess_limit = 10
        case "2":
            upper_range = 100
            guess_limit = 20
        case "3":
            upper_range = 500
            guess_limit = 40
        case "4":
            sys.exit()
        case _:
            print("Please enter a valid option")
            continue

    rand_number = random.randint(1,upper_range)
    guess = int(input(f"Enter a random number between 1 and {upper_range}: "))
    guess_counter += 1

    if guess == rand_number:
        print("Correct")
    else:
        while guess != rand_number:

            if guess_counter >= guess_limit:
                print("You've ran out of guesses")
                break
            guess_counter += 1

            if guess < rand_number:
                print("\nToo Low!")
                guess = int(input(f"Guess number {guess_counter}: "))
            else:
                print("\nToo High!")
                guess = int(input(f"Guess number {guess_counter}: "))
        if guess == rand_number:
            print(f"You got it in {guess_counter} guesses")

    play_again = input("Would you like to play again, 'y' or 'n'?")

    if play_again == "y":
        continue
    else:
        sys.exit()
