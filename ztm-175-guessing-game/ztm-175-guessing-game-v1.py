from random import randint
import sys

# generate a number based on user provided range
try:
    low = int(sys.argv[1])
    high = int(sys.argv[2])
except ValueError:
    print("Unable to parse code as an integer")
    sys.exit(1)

number = randint(low, high)
# number = randint(1, 10)

# input from user?

while True:
    try:
        guess = int(input(f"Guess a number from {low} to {high}: "))
        # check input is a number 1~10
        if guess < low or guess > high:
            print(
                f"Input should be a number from {low} to {high}. Guess again.")
            continue

        # check input against generated number
        if guess != number:
            if guess < number:
                print("No no. You guessed too low. Try again!")
            else:
                print("Nope. Too high. Guess again!")
            continue
        else:
            print(f"You guessed correctly! The number was {number}")
            break
    except ValueError:
        print(f"Input should be a number from {low} to {high}. Guess again.")
