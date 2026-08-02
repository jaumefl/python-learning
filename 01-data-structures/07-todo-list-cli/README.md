# To-do List CLI

A menu-driven to-do list that survives between runs. On launch it loads tasks
from `tasks.txt`; every add or delete saves straight back, so the file always
matches what's in memory. Add a task, delete one by its number, or quit:
re-run and the list is still there. Handles the ugly inputs: missing file on
first run, empty file, out-of-range numbers, and non-numeric input.

## Concepts I used

- a plain `list` as the data store: `tasks.append(text)` to add,
  `del tasks[i]` to remove by position
- `enumerate(tasks, start=1)` to number tasks 1-based for display while the
  list stays 0-based underneath
- file persistence: `save_tasks` does `"\n".join(tasks)` then `f.write(...)`;
  `load_tasks` does `f.read().strip()` then `.split("\n")`
- `try / except FileNotFoundError` so the first run (no file yet) returns `[]`
  instead of crashing
- `try / except ValueError` around `int(input())` to survive non-numeric input
- range check `if n < 1 or n > len(tasks)` before indexing

## What I learned

The save/load round-trip has a trap I didn't see coming. `"\n".join([])`
writes an empty string, and `"".split("\n")` reads back `[""]`  (a list with
one blank item, not an empty list) so an empty to-do list printed a phantom
`1. ` row. Fixed it by `.strip()`-ing the file content and returning `[]` when
it's empty, only splitting when there's real content. I also first reached for
`f.readline()`, which grabs only the first line, so every task after the first
vanished — `f.read()` reads the whole file.

The other lesson was delete-by-position vs delete-by-value. `.remove(x)` scans
for the first item equal to `x`, so if two tasks share the same text it deletes
the wrong one; `del tasks[i]` targets the exact slot the user picked. 