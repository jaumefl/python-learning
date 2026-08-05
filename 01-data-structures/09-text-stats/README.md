# Text Stats Analyzer

Reads a `.txt` file from `samples/` and reports statistics about it: character
counts (with and without spaces), word count, sentence count, average word
length, average words per sentence, the longest word, the most common word, and
an estimated reading time.

## Run
    python main.py

Enter a sample name without the extension (e.g. `short`, `medium`, `messy`);
the program looks in `samples/`.

## Concepts
- String methods: `.replace`, `.split`, `.strip`, `.lower`
- `collections.Counter` + `.most_common(1)` for the most frequent word
- `try` / `except FileNotFoundError` instead of crashing on a bad name
- Empty-input guards (`if not words:`) before any indexing or division

## Notes / gotchas
- `.split()` with no argument collapses runs of whitespace, but `.split(".")`
  does not — consecutive delimiters leave empty strings, so `"!!!"` and `"..."`
  produced phantom sentences until filtered with `if s.strip()`.
- You can't chain `.split()` across different delimiters (a list has no
  `.split()`), so punctuation is normalized to `.` first, then split once.
- The empty-file guard has to run before `words[0]` and before any division,
  or an empty file raises `IndexError` then `ZeroDivisionError`.
