# FizzBuzz

Prints the numbers 1 to N, but replaces multiples of 3 with "Fizz",
multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
The user picks how high to count.

## Concepts I used

- `for` loop over `range(1, n+1)` to count up to and including N
- `if` / `elif` / `else`, ordered most-specific-first (check 15 before 5 and 3)
- the modulo operator `%` (already familiar)
- `input()` + `int()` to read the upper bound

## What I learned

`range()` excludes the second argument, so to count up to N I had to
write `range(1, n+1)`.