import numpy as np
def main():
    rng = np.random.default_rng()
    try:
        mode = int(input("""Select what to simulate:
        1. Coin
        2. Die
        Select --> """).strip())
        if mode not in (1, 2):
            print("Invalid choice. Try again.")
            return
        reps = int(input("""Type in how many reps to simulate: """))
        if reps <= 0:
            print("Please enter a valid answer")
            return
    except ValueError:
        print("Please enter a valid answer")
        return

    if mode == 1:
        heads,tails = sim_coin(reps,rng)
        print(f"\n{'Side':>6} {'Count':>12} {'Expected':>12} {'Observed':>10} {'Theory':>8}")
        print("-" * 52)
        for label, count in (("Heads", heads), ("Tails", tails)):
            print(f"{label:>6} {count:>12,} {reps / 2:>12,.0f} {count / reps * 100:>9.2f}% {50:>7.2f}%")

    elif mode == 2:
        counts = sim_die(reps,rng)
        expected = reps / 6
        print(f"\n{'Face':>6} {'Count':>12} {'Expected':>12} {'Observed':>10} {'Theory':>8}")
        print("-" * 52)
        for face in range(1, 7):
            print(
                f"{face:>6} {counts[face]:>12,} {expected:>12,.0f} {counts[face] / reps * 100:>9.2f}% {100 / 6:>7.2f}%")





def sim_coin(n, rng):
    flips = rng.integers(0,2,size=n)
    tails = flips.sum() # 1 = tails, 0 = heads

    return n-tails, tails

def sim_die(n, rng):
    rolls = rng.integers(1,7,size=n)
    return np.bincount(rolls,minlength=7)




if __name__ == '__main__':
    main()