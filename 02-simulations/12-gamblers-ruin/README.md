# Gambler's Ruin

You start with `start` units and bet 1 unit per round on a coin that comes up in
your favour with probability `p`. You stop when you hit your `target` or when
you hit zero. The program simulates 10 000 such games at every value of `p` from
0.00 to 1.00 and reports how often you were ruined, how long the games lasted,
and how much that duration varied.

Every simulated ruin rate is printed beside the exact value from the closed-form
formula. Agreement between the two columns is the correctness check — the
simulation is only interesting once it reproduces the known answer.

## The formula

For a walk starting at `k` with absorbing barriers at 0 and `N`, the probability
of reaching `N` before 0 is:

- **Fair game (p = 0.5):** `k / N`
- **Biased game:** `(1 − rᵏ) / (1 − rᴺ)` where `r = (1 − p) / p`

Ruin probability is 1 minus that. The fair case needs its own branch because
`r = 1` makes the general formula divide by zero, and `p = 0` needs one too
because `r = (1 − p) / p` divides by zero directly.

The fair case has a one-line justification: in a fair game your expected final
wealth equals your starting wealth. You finish with either 0 or `N`, so
`N × P(win) = k`, giving `P(win) = k / N`. You win in proportion to your share
of the money on the table.

## Sample output

Start 10, target 20, 10 000 trials per row. Abridged to the region where
anything happens — outside roughly 0.40–0.60 the table is flat at 100% or 0%.

```
     p     Ruin %   Theory %      Mean    Median     Stdev
----------------------------------------------------------
  0.40     98.41%     98.30%      48.6      40.0      32.7
  0.42     96.34%     96.19%      57.0      46.0      39.3
  0.44     92.15%     91.77%      69.0      54.0      52.0
  0.46     83.75%     83.25%      82.6      64.0      64.7
  0.47     76.80%     76.88%      90.8      70.0      71.9
  0.48     68.35%     69.01%      95.5      72.0      75.6
  0.49     60.07%     59.87%      98.9      76.0      79.8
  0.50     50.21%     50.00%     101.5      78.0      82.5
  0.51     40.53%     40.13%      98.5      74.0      81.1
  0.52     32.04%     30.99%      95.5      72.0      75.7
  0.54     17.42%     16.75%      82.5      64.0      63.9
  0.56      8.35%      8.23%      69.2      54.0      50.8
  0.58      4.14%      3.81%      58.1      46.0      41.1
  0.60      1.64%      1.70%      48.0      40.0      30.7
```

## The results

**A 1% edge is not a small number.** Going from p = 0.50 to p = 0.49 takes ruin
from 50% to 60%. At 0.47 it is 77%, at 0.45 it is 88%. The curve is steeply
nonlinear, and it is why a house edge of a couple of percent is enough to make a
casino's outcome a certainty rather than a gamble.

**Mean rounds peaks exactly at p = 0.50.** The fair game lasts longest (101.5
rounds) and duration falls away on both sides. An edge in *either* direction
pushes you to a barrier faster; only a fair walk has no reason to go anywhere.
The fair case also has an exact prediction, `start × (target − start)` = 10 × 10
= 100, which the measured 101.5 sits right on top of.

**The standard deviation is almost as large as the mean** — 82.5 against 101.5
at p = 0.50. A typical game misses the average by 80% of the average. Compare
counting heads in 100 coin flips, where the mean is 50 and the stdev is 5.

**Median is well below mean** (78 vs 101.5), so the distribution is
right-skewed. It is squashed against a floor — the fastest possible loss is 10
straight losses, 10 rounds — but has no ceiling, since the walk can wander near
the middle for hundreds of rounds. The rare very long games drag the mean up
while the median barely moves.

Together those last two are the point of the whole project.