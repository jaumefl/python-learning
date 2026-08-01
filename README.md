# Python Learning Journey

Learning Python from the basics toward quantitative finance (NumPy, Pandas).
Each project lives in its own folder with a small README. This log is the record of the climb.

## Learning Log

| # | Project | Date       | New concepts                                   | What I learned                                                                                                                                                                                                                                                         |
|---|---------|------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | Number guessing game | 2026-07-28 | `random`                                       | `input()` always returns text, so I had to `int()` it before comparing. Also got used to indentation replacing braces.                                                                                                                                                 |
| 2 | FizzBuzz | 2026-07-29 | `for`, `range()`                               | `range(1, n+1)` is exclusive on the upper end. Modulo I already knew from Java.                                                                                                                                                                                        |
| 3 | CLI calculator | 2026-07-29 | functions, branching on operator, try / except | Split each operation into its own function and dispatched with if/elif on the user's choice. Learned that dividing ints in Python 3 still returns a float.                                                                                                             |
| 4 | Multiplication drill | 2026-07-30 | `time`, f-strings, `while True` / `break`      | `time.time()` is only useful taken twice and subtracted. `while True` + `break` is the right shape for a "play again?" loop when I don't know the number of rounds up front.                                                                                           |
| 5 | Unit converter | 2026-08-01 | dictionary dispatch (functions as values) | Stored each function in a dict keyed by menu number, so one lookup replaced the whole if/elif chain. Learned functions are values you can pass around, `func` stores it, `func()` calls it. Also that `continue` returns to the menu while `return` kills the program. |
| 6 | Word frequency counter | 2026-08-01 | file I/O (`with open`), `dict.get()` counting, `collections.Counter`, list comprehensions | Counted words with `counts.get(word, 0) + 1`, then refactored the whole loop + sort into `Counter(words).most_common()`. Learned that `.strip()` and `sorted()` return new values that vanish if I don't assign them, and that `open()` needs `encoding="utf-8"` on Windows or an em dash comes out as mojibake. |

## Roadmap

- **00-basics** — variables, loops, functions, input
- **01-data-structures** — lists, dicts, strings, file I/O
- **02-simulations** — probability sims, OOP
- **03-numpy-pandas** — vectorization, data analysis, finance