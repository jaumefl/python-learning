import time

import numpy as np

from baseline import sim_die_loop, sim_coin_loop, estimate_pi_loop
from dice_numpy import sim_die, sim_coin
from montecarlo_numpy import estimate_pi


REPEATS = 3
SIZES = [10_000, 100_000, 1_000_000, 10_000_000]

def time_call(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start

def run(title, loop_fn, np_fn, sizes, rng):
    print(f"\n{title}")
    print(f"{'Trials':>12} {'Loop (s)':>12} {'NumPy (s)':>12} {'Speedup':>10}")
    print("-" * 49)

    for n in sizes:
        t_loop = min(time_call(loop_fn, n) for _ in range(REPEATS))
        t_np = min(time_call(np_fn, n, rng) for _ in range(REPEATS))
        print(f"{n:>12,} {t_loop:>12.4f} {t_np:>12.4f} {t_loop / t_np:>9.1f}x")

def main():
    rng = np.random.default_rng(42)

    run("Coin flips", sim_coin_loop, sim_coin, SIZES, rng)
    run("Die rolls", sim_die_loop, sim_die, SIZES, rng)
    run("Monte Carlo pi", estimate_pi_loop, estimate_pi, SIZES, rng)
    print()

if __name__ == "__main__":
    main()