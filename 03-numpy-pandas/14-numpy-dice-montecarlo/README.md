# 14 — Dice & Monte Carlo in NumPy
 
Projects 10 and 11 rewritten so that no Python loop ever touches an individual
trial. Every simulation generates all N random values at once as a NumPy array
and lets compiled code do the arithmetic. The loop versions are kept verbatim in
`baseline.py` so the two can be timed side by side.
 
## What's here
 
- `dice_numpy.py` — coin and die simulation, vectorized. Interactive menu.
- `montecarlo_numpy.py` — Monte Carlo π, vectorized. 20 runs per sample size.
- `baseline.py` — the loop code from projects 10 and 11, copied unchanged and
  stripped of its I/O. The "before" in the benchmark.
- `benchmark.py` — times both versions at four sample sizes and prints speedups.
## The rewrite
 
The die went from a loop with a `Counter` to two lines:
 
```python
rolls = rng.integers(1, 7, size=n)
return np.bincount(rolls, minlength=7)
```
 
`bincount` walks the array once in C and tallies each value using the value
itself as an index — `Counter` without the Python-level loop.
 
π went from a loop with a running `hits` counter to four lines:
 
```python
x = rng.random(size=n)
y = rng.random(size=n)
inside = (x**2 + y**2) <= 1.0
return inside.mean() * 4
```
 
The comparison produces a **boolean mask** — an array of True/False, one per
point. Since `True` is 1, `.mean()` on that mask *is* the fraction of points
inside the quarter circle, so the estimate falls out of the array with no
counting at all.
 
## Accuracy (montecarlo_numpy.py)
 
20 runs per size, seed 42. Errors are averaged per run, not measured on the
averaged estimate — averaging estimates first lets overshoots cancel
undershoots and reports the accuracy of 20N samples under an N label.
 
```
    Trials     Estimate      Abs err     Rel err %
--------------------------------------------------
       100       3.1600     0.133841        4.260%
     1,000       3.1344     0.041759        1.329%
    10,000       3.1481     0.013341        0.425%
   100,000       3.1412     0.003147        0.100%
 1,000,000       3.1416     0.001090        0.035%
```
 
Each 10× in samples cuts the error by roughly 3.2×, against √10 ≈ 3.16. Same
1/√N law project 11 found — vectorizing changed the speed, not the statistics.
 
## Speedups (benchmark.py)
 
Four sample sizes, best of 3 runs each, `time.perf_counter()`.
 
```
Coin flips
      Trials     Loop (s)    NumPy (s)    Speedup
-------------------------------------------------
      10,000       0.0049       0.0001      92.4x
     100,000       0.0495       0.0004     121.1x
   1,000,000       0.4859       0.0063      76.8x
  10,000,000       5.1970       0.0587      88.6x
 
Die rolls
      Trials     Loop (s)    NumPy (s)    Speedup
-------------------------------------------------
      10,000       0.0041       0.0001      53.8x
     100,000       0.0467       0.0007      67.5x
   1,000,000       0.4347       0.0074      58.4x
  10,000,000       4.5002       0.0923      48.7x
 
Monte Carlo pi
      Trials     Loop (s)    NumPy (s)    Speedup
-------------------------------------------------
      10,000       0.0017       0.0001      14.3x
     100,000       0.0166       0.0032       5.2x
   1,000,000       0.1839       0.0327       5.6x
  10,000,000       1.7875       0.2724       6.6x
```
 
## The results
 
**Ten million die rolls went from 4.5 seconds to 0.09 seconds.** That is the
headline, and it is the difference between a simulation you run once and a
simulation you run inside another loop.
 
**π only sped up ~6×, while the dice sped up ~50×.** Same technique, same
machine, an order of magnitude apart — and the gap is the most interesting thing
in the table. Count what each version allocates. `sim_die` builds one integer
array and tallies it. `estimate_pi` builds six arrays per call: `x`, `y`, `x**2`,
`y**2`, their sum, and the boolean mask. At 10 million trials that is roughly
half a gigabyte of memory traffic for arithmetic that is nearly free by
comparison. The die is limited by how fast the CPU can compute; π is limited by
how fast values move between RAM and the CPU.
 
So vectorization buys speed by spending memory, and once a calculation is
memory-bound, vectorizing harder stops helping. Fusing those six arrays into one
pass is what `numexpr` and `numba` exist to do.
 
**π's speedup falls as N grows** (14.3× at 10 000, then ~5–6×), while the dice
hold roughly flat. At small N the arrays still fit in CPU cache and the memory
cost is hidden; by 10 million they do not, and the true memory-bound rate shows
through. The small-N number is the flattering one, not the honest one.
 
**One caveat on the coin row.** The loop version stores `"H"` and `"T"` strings;
the NumPy version uses 0/1 integers. So that speedup mixes vectorization with a
cheaper data type and is not strictly apples-to-apples. Dice and π are — both
compare integers to integers and floats to floats.
 
## Running it
 
```
pip install numpy
python dice_numpy.py       # interactive
python montecarlo_numpy.py # accuracy table
python benchmark.py        # speedup tables, takes ~45s
```
 
`benchmark.py` spends nearly all of that 45 seconds inside the loop versions at
10 million trials. The wait is the point.
