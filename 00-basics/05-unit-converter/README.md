# Unit Converter

A menu-driven converter for temperature, distance, and weight. The user picks a
conversion from the menu, enters a value, and gets the result rounded to two
decimals. It loops until they choose Quit, and re-prompts instead of crashing on
bad input. Six conversions: Celsius/Fahrenheit, kilometres/miles, and
kilograms/pounds, both directions.

## Concepts I used

- a dictionary as a dispatch table: `{1: (celsius_to_fahrenheit, ...)}` maps each
  menu choice to its function plus its input/output unit labels
- functions stored as values (no parentheses) and called later with `func(value)`
- tuple unpacking: `func, label, res = conversions[choice]`
- `if choice not in conversions` to guard against out-of-range numbers
- `while True` + `break` for the menu loop, `continue` to re-prompt on bad input

## What I learned

A dictionary can replace a long if/elif chain when every branch does the same
shape of work: look up the function and call it. The key insight is that a
function is just a value: `celsius_to_fahrenheit` is the function itself, and
adding `()` is what calls it. I also nailed down the difference between `continue`
(back to the menu) and `return` (exit the whole program) inside a loop.