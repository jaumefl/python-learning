import random
import math
def main():

    sizes = [100, 1000, 10000, 100000, 1000000]#

    print("\n")

    for size in sizes:
        est = estimate_pi(size)
        print(f"Number of trials: {size};  Estimated pi: {est:.4f};  Absolute error: {abs(est - math.pi):.6f};  Relative error: {100*abs(est - math.pi)/math.pi:.3f}%")

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