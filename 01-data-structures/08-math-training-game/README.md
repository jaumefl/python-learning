# Mental-Math Trainer (my own Zetamac)

A 120-second arithmetic drill. Random `+ - * /` problems fire until time runs
out, then the session is scored and appended to `results.csv`. A menu lets you
play, view the last 20 sessions, or quit.

## What's new here
- `random.choice` to pick the operator
- `time.time()` read live in the loop condition as a countdown, not a stopwatch
- append mode (`open(..., "a")`) for a log that survives restarts
- `datetime.now().strftime("%Y-%m-%d %H:%M")` to timestamp each session
- negative-index slicing to show only recent history

## Design notes
- Division problems present `product / first` so the answer is always an integer
  — no float comparison needed.
- Timestamps stored as `YYYY-MM-DD HH:MM` so the log sorts as plain text.

## Update — 2026-08-21: CSV logging

Sessions were originally appended to `record.txt` as sentences
(`2026-08-04 00:17 -> 25 correct answers out of 27 attempts.`). Project 15 needed
this data in Pandas, and parsing prose back into numbers is work that shouldn't
have to exist — so the log is now `results.csv`:

```
timestamp,correct,total
2026-08-04 00:17,25,27
```

The three existing sessions were migrated by hand and `record.txt` deleted.

New in this change:

- the **`csv` module** — `csv.writer` / `csv.reader` instead of hand-built
  strings, so quoting and line terminators are handled for me
- **`newline=""`** on every open: required on Windows, or `csv` writes `\r\n`,
  text mode expands the `\n` again, and every row gets a blank line after it
- **`Path(__file__).parent / "results.csv"`** so the file resolves regardless of
  which directory the script is run from
- the header is written only when the file doesn't exist, and that check has to
  happen **before** `open(..., "a")` — opening creates the file, so checking
  afterwards means the header never gets written
- **tuple unpacking** in the read loop (`for stamp, correct, total in rows`),
  which raises `ValueError` on a malformed row instead of printing nonsense
- `rows[1:]` to skip the header — `csv.reader` has no idea it's a header

Gotcha that caught me twice: a hand-typed CSV must end in a newline. Append mode
starts writing at the last byte, so a file ending mid-line concatenates the next
session onto it — the same smear as the missing `\n` in the original
`record.txt`.