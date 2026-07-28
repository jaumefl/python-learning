import random


def main():
    secret = random.randint(1, 100)
    guess_count = 1

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == secret:
            break
        if guess < secret and guess >= 0:
            print("Too low. Try again.")
            guess_count += 1
        elif guess > secret and guess <= 100:
            print("Too high. Try again.")
            guess_count += 1

        else:
            print("Input should be in between 1 and 100. Try again.")

    print(f"Congratulations. You have guessed correctly, the number was {secret}, and it took you {guess_count} guesses.")


if __name__ == "__main__":
    main()