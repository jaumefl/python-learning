import statistics
import random
REPETITIONS = 10000
def main():
    start = ask_number("Starting amount of units: ", int)
    target = ask_number("Target amount: ", int)
    while not 0 < start < target:
        print("Need 0 < start < target.")
        start = ask_number("Starting amount of units: ", int)
        target = ask_number("Target amount: ", int)

    print(f"\nStart: {start}   Target: {target}   Trials: {REPETITIONS}\n")
    print(f"{'p':>6} {'Ruin %':>10} {'Theory %':>10} {'Mean':>9} {'Median':>9} {'Stdev':>9}")
    print("-" * 58)

    for i in range(101):
        s = run_trial(start, target, i / 100)
        print(f"{s['p']:>6.2f} {s['ruin']:>10.2%} {s['theory']:>10.2%} "
              f"{s['mean']:>9.1f} {s['median']:>9.1f} {s['stdev']:>9.1f}")



def run_trial(start, target, p):

    round_list = []
    successes = []

    for _ in range(REPETITIONS):
        end, rounds = one_game(start, target, p)
        round_list.append(rounds)
        successes.append(end != 0)

    empirical_ruin_rate = 1 - statistics.mean(successes)
    theoretical_ruin_rate = theoretical_ruin(start, target, p)
    mean_rounds = statistics.mean(round_list)
    rounds_sample_sd_dev = statistics.stdev(round_list)
    rounds_median = statistics.median(round_list)

    return{
        "p": p,
        "ruin": empirical_ruin_rate,
        "theory": theoretical_ruin_rate,
        "mean": mean_rounds,
        "median": rounds_median,
        "stdev": rounds_sample_sd_dev,
    }


def theoretical_ruin(start, target, p):
    if p == 0:
        return 1.0
    if p == 0.5:
        return 1 - start/target
    r = (1 - p) / p
    return 1 - (1 - r ** start) / (1 - r ** target)




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