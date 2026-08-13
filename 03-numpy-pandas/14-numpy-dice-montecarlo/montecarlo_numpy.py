import numpy as np

def main():
    rng = np.random.default_rng(42)
    RUNS = 20
    sizes = [100, 1000, 10000, 100000, 1000000]

    print(f"{'Trials':>10} {'Estimate':>12} {'Abs err':>12} {'Rel err %':>13}")
    print("-" * 49)

    for size in sizes:
        estimates = [estimate_pi(size,rng) for _ in range(RUNS)]
        ests = np.array(estimates)
        est = ests.mean()
        abserr = np.abs(ests-np.pi).mean()

        relerr = (abserr/np.pi)* 100
        print(f"{size:>10,} {est:>12.4f} {abserr:>12.6f} {relerr:>12.3f}%")





def estimate_pi(n,rng):
    x = rng.random(size=n)
    y = rng.random(size=n)
    inside = (x**2 + y**2) <= 1.0

    return inside.mean()*4



if __name__ == '__main__':
    main()