import random
attempt = 0

print(f"Attempt: {attempt}")
answer = input("Roll the dice? (y/n): ").lower()

while True:
    if answer == "y":

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        die3 = random.randint(1, 6)
        die4 = random.randint(1, 6)
        die5 = random.randint(1, 6)
            #user picks amount
        amount = int(input("How many dice? (1-5): "))


        if amount == 1 :
            print(f"Your die shows: {die1}")
            attempt += 1
        elif amount == 2:
            print(f"Your dice show: {die1}, {die2}")
            attempt += 1
        elif amount == 3:
            print(f"Your dice show: {die1}, {die2}, {die3}")
            attempt += 1
        elif amount == 4:
            print(f"Your dice show: {die1}, {die2}, {die3}, {die4}")
            attempt += 1
        elif amount == 5:
            print(f"Your dice show: {die1}, {die2}, {die3}, {die4}, {die5}")
            attempt += 1
        else:
            print("Invalid amount.")
        print()
        print(f"Attempt: {attempt}")
        answer = input("Roll the dice? (y/n): ").lower()


    elif answer == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid answer.")
        answer = input("Roll the dice? (y/n): ").lower()