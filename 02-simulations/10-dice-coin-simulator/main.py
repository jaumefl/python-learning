import random
from collections import Counter
def main():
    while True:
        try:
            game = int(input("""What do you want to simulate?
            1. Flipping a coin
            2. Rolling a 6-sided fair die
            Pick your choice: """).strip())
        except ValueError:
            print("Please enter a valid option.")
            continue

        if game <= 0 or game >= 3:
            print("Please enter a valid option.")
            continue

        try:
            repetitions = int(input("""How many repetitions would you like to simulate? --> """))
        except ValueError:
            print("Please enter an integer.")
            continue

        if game == 1:

            counts = Counter()
            for _ in range(repetitions):
                flip = random.choice(["H", "T"])
                counts[flip] += 1

            heads = counts["H"]
            tails = counts["T"]

            print(f"""Heads: {heads} times vs expected {repetitions/2} --> {round(heads/repetitions*100,2)}% vs expected 50%
Tails: {tails} times vs expected {repetitions/2} --> {round(tails/repetitions*100,2)}% against expected 50%
""")

        if game == 2:
            counts = Counter()
            for _ in range(repetitions):
                rolled = random.randint(1, 6)
                counts[rolled] += 1

            expected = round(repetitions/6,2)
            print(f"""
1 --> {counts[1]} times vs expected {expected} times // {round(counts[1]/repetitions*100,2)}% vs expected 16.67%
2 --> {counts[2]} times vs expected {expected} times // {round(counts[2]/repetitions*100,2)}% vs expected 16.67%
3 --> {counts[3]} times vs expected {expected} times // {round(counts[3]/repetitions*100,2)}% vs expected 16.67%
4 --> {counts[4]} times vs expected {expected} times // {round(counts[4]/repetitions*100,2)}% vs expected 16.67%
5 --> {counts[5]} times vs expected {expected} times // {round(counts[5]/repetitions*100,2)}% vs expected 16.67%
6 --> {counts[6]} times vs expected {expected} times // {round(counts[6]/repetitions*100,2)}% vs expected 16.67%
""")


        more = input("Would you like to perform another simulation? (y/n) ")
        if more != "y":
            break

if __name__ == "__main__":
    main()
