# Mental-Math Trainer (my own Zetamac)

A 120-second arithmetic drill. Random `+ - * /` problems fire until time runs
out, then the session is scored and appended to `record.txt`. A menu lets you
play, view the last 20 sessions, or quit.

## What's new here
- `random.choice` to pick the operator
- `time.time()` read live in the loop condition as a countdown, not a stopwatch
- append mode `open("record.txt", "a")` for a persistent log
- `datetime.now().strftime("%Y-%m-%d %H:%M")` to timestamp each session
- negative-index slicing `lines[-20:]` to show only recent history

## Design notes
- Division problems present `product / first` so the answer is always an integer
  — no float comparison needed.
- Timestamps stored as `YYYY-MM-DD HH:MM` so the log sorts as plain text and
  parses cleanly in Pandas later (Project 15).
