# Monte Carlo π Estimator

Estimates π by throwing random darts at the unit square and counting how many
land inside the quarter circle `x² + y² ≤ 1`. That fraction approximates the
ratio of areas, π/4, so `4 × hits / trials` estimates π. The value is never
computed — it is measured.

The program runs the estimator at five sample sizes (100 up to 1 000 000) and
prints an aligned convergence table. Each row is averaged over `RUNS = 20`
independent runs, because a single run is too noisy to show a trend.

## Sample output

```
    Trials     Estimate      Abs err    Rel err %
-------------------------------------------------
       100     3.122000     0.124159        3.952
     1,000     3.137400     0.060759        1.934
    10,000     3.139360     0.013160        0.419
   100,000     3.140344     0.004319        0.137
 1,000,000     3.141895     0.001492        0.047
```

## The result

Dividing each error by the row below gives 2.04, 4.62, 3.05, 2.89 — averaging
about **3.1**, against √10 ≈ 3.16. Ten times the samples buys roughly 3.2× less
error, not 10×. Monte Carlo error scales as **1/√N**, so one extra decimal
place of accuracy costs 100× the work. That is the whole reason Monte Carlo is
simultaneously indispensable and slow.

## Concepts
- `random.random()` — continuous sampling in [0, 1), after only discrete
  `randint` / `choice` so far
- `math.pi`, `abs()` for error measurement
- f-string format specifiers (`:>12.6f`, `:>10,`) replacing `round()` for display
- Building a table: header printed once, fixed column widths, values aligned
- Extracting `estimate_pi(trials)` — a pure function that takes a number and
  returns a number, with no I/O inside
- Averaging *errors* rather than *estimates* to measure accuracy
- Monte Carlo convergence, 1/√N
