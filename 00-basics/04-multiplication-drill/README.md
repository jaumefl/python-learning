# Multiplication Drill

A timed times-tables trainer. The user picks how many questions they want and
the highest number to drill, then answers a series of random multiplication
problems. At the end the program reports the score, total time, and average
time per question. It asks whether to play again and loops until the user says
no. This is my first step toward the mental-math trainer I want to build later.

## Concepts I used

- the `time` module: two `time.time()` snapshots subtracted to measure elapsed seconds
- f-strings to inject variables into prompts and into the multiline results block
- `while True` + `break` to keep replaying until the user opts out
- `try` / `except ValueError` to survive non-numeric input
- `round(x, 2)` to trim the timing floats for display

## What I learned

`time.time()` on its own is a meaningless number — it only means something when
you take it twice and subtract to get the elapsed time. I also learned that
`while True` with a `break` is the right shape for a loop that runs an unknown
number of times (the "play again?" loop), as opposed to a `for` loop when I know
the count up front.
