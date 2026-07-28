# Number Guessing Game

My first Python project. The program picks a random number between 1 and 100,
and I have to guess it. It tells me if my guess is too high or too low until I
get it right, then shows how many tries it took.

## Concepts I used

- `while` loop to keep asking until the guess is correct
- `if` / `elif` / `else` for the too high / too low / invalid cases
- `input()` and converting the text to a number with `int()`
- the `random` module (`random.randint`)

## What I learned

`input()` always gives back text, so I had to convert it to an integer before
I could compare it. I also got used to Python using indentation instead of
braces to group code.