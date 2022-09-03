from random import randint
import sys


def get_random_number(low, high):
    # generate a number based on user provided range
    return randint(low, high)


def is_in_range(guess, low, high):
    # check that input is in range
    if guess < low or guess > high:
        print(f"Input should be a number from {low} to {high}. Guess again.")
        return False
    else:
        return True


def run_guess(guess, number):
    # check input against generated number
    if guess != number:
        if guess < number:
            print("No no. You guessed too low. Try again!")
        else:
            print("Nope. Too high. Guess again!")
        return False
    else:
        print(f"You guessed correctly! The number was {number}")
        return True


def main() -> None:
    if len(sys.argv) > 1:
        try:
            low = int(sys.argv[1])
            high = int(sys.argv[2])
        except ValueError:
            print("Supply 2 integers as lower and upper range for guess")
            sys.exit(1)
    else:
        low = 1
        high = 10

    answer = get_random_number(low, high)

    while True:
        try:
            guess = int(input(f"Guess a number from {low} to {high}: "))
            if not is_in_range(guess, low, high):
                continue
            if run_guess(guess, answer):
                break
        except ValueError:
            print(
                f"Input should be a number from {low} to {high}. Guess again.")


if __name__ == "__main__":
    main()
