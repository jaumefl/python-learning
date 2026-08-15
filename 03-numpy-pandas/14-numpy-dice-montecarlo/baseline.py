import random
from collections import Counter

def sim_coin_loop(n):
    counts = Counter()
    for _ in range(n):
        flip = random.choice(["H", "T"])
        counts[flip] += 1

    heads = counts["H"]
    tails = counts["T"]

    return heads, tails

def sim_die_loop(n):
    counts = Counter()
    for _ in range(n):
        rolled = random.randint(1, 6)
        counts[rolled] += 1
    return counts

def estimate_pi_loop(n):
    hits = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            hits += 1

    estimation = (hits / n) * 4

    return estimation
