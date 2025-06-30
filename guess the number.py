import random

#game code
def play_game():
    answer = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1-100: "))
            if guess > 100 or guess < 1:
                print()
                print("Out of range!")
                print()

            elif guess > answer:
                print("Too high!")

            elif guess < answer:
                print("Too low!")

            elif guess == answer:
                print("Correct!")
                break

        except ValueError:
            print()
            print("Please type out a valid number.")
            print()

#start game
play_game()
retry= input("Try again? (y/n):")
while True:
    if retry == "y":
        play_game()
        retry = input("Try again? (y/n):")
    elif retry == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid answer.")
        retry = input("Try again? (y/n):")
