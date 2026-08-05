# Dice / Coin Simulator

Simulates coin flips or fair 6-sided die rolls over N trials, tallies outcomes
with `collections.Counter`, and prints each empirical probability next to the
theoretical one. Watching the two converge as N grows is the law of large
numbers in action — the first step toward the probability work ahead.

## Concepts
- `collections.Counter` for tallying outcomes without one variable per result
- Empirical vs theoretical probability
- `random.choice` / `random.randint`, list-free incremental counting
- Rounding *last*, after the arithmetic, to avoid float display errors