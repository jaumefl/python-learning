# Word Frequency Counter

Reads a text file, cleans up the words, counts how often each one appears, and
prints them from most to least frequent. Words are lowercased and stripped of
leading/trailing punctuation so `The`, `the`, and `the.` all count as one word.
Built it twice: first by hand with a plain dict, then refactored to
`collections.Counter`. The manual version is kept as a comment to show the
before/after.

## Concepts I used

- `with open("sample.txt", encoding="utf-8") as file:` — a context manager that
  closes the file for me; `encoding="utf-8"` fixes the mojibake I got on Windows
- `.read()` and `.split()` to turn the file into a list of words, `.lower()` to
  normalize case
- `str.strip(string.punctuation)` to shave punctuation off each word
- dict counting with `counts[word] = counts.get(word, 0) + 1`
- `sorted(counts.items(), key=lambda x: x[1], reverse=True)` to order by count
- list comprehensions: `[word.strip(...) for word in text.split()]` and a filter
  `[word for word in words if word]` to drop empties
- `collections.Counter(words)` and `.most_common()` as the upgrade

## What I learned

The core trick is `counts.get(word, 0)` — it hands back the current count or `0`
if the word is new, which replaces a clumsy if/else. The bigger lesson was that
string and sort operations return a *new* value: `text.strip(...)` and
`sorted(...)` do nothing unless I catch the result with `=`. Two of my bugs were
exactly that, plus one missing `()` on `.lower` that turned my string into a
method object. `Counter` then collapsed my whole counting loop and manual sort
into `Counter(words)` and `.most_common()` — same result, a dict subclass under
the hood. Also learned `open()` defaults to a non-UTF-8 encoding on Windows,
which is why an em dash showed up as garbage until I set `encoding` explicitly.
