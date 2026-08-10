import statistics
import random
def main():
    start = ask_number("Starting amount of units: ", int)
    target = ask_number("Target amount: ", int)
    while not 0 < start < target:
        print("Need 0 < start < target.")
        start = ask_number("Starting amount of units: ", int)
        target = ask_number("Target amount: ", int)

    p = ask_number("Probability: ", float)
    while not 0 <= p <= 1:
        print("Probability must be between 0 and 1.")
        p = ask_number("Probability of success: ", float)

    REPETITIONS = 1000

    round_count = []
    successes = []

    for _ in range(REPETITIONS):
        end, rounds = one_game(start, target, p)
        round_count.append(rounds)
        if end == 0:
            successes.append(0)
        else:
            successes.append(1)







def one_game(start, target, p):
    bankroll = start
    rounds = 0

    while 0 < bankroll < target:
        if (random.random() < p):
            bankroll += 1
        else:
            bankroll -= 1
        rounds += 1

    return bankroll, rounds

def ask_number(prompt, converter):
    while True:
        try:
            return converter(input(prompt))
        except ValueError:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()