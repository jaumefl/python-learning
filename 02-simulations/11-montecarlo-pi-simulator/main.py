import random
import math

RUNS = 20


def main():

    sizes = [100, 1000, 10000, 100000, 1000000]

    print("\n")
    print(f"{'Trials':>10} {'Estimate':>12} {'Abs err':>12} {'Rel err %':>12}")
    print("-" * 49)
    for size in sizes:
        estimate_total = 0
        error_total = 0
        for _ in range(RUNS):
            est = estimate_pi(size)
            estimate_total += est
            error_total += abs(est - math.pi)

        mean_estimate = estimate_total / RUNS
        mean_abs_error = error_total / RUNS
        rel_error = 100 * mean_abs_error / math.pi
        print(f"{size:>10,} {mean_estimate:>12.6f} {mean_abs_error:>12.6f} {rel_error:>12.3f}")

    print("\n")


def estimate_pi(trials):
    hits = 0
    for _ in range(trials):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            hits += 1

    estimation = (hits / trials) * 4

    return estimation


if __name__ == "__main__":
    main()