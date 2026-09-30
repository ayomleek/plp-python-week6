# PLP Python Week 6 – Error Handling with try/except

## Files

- `safe_tools.py` – three functions (`safe_divide`, `safe_number`, `get_field`) that use `try`/`except` so bad input returns a friendly message instead of crashing.
- `unbreakable.py` – a program that reads user input and keeps running without crashing by handling errors with `try`/`except`.

## Why can the `if` check not catch `abc` on its own?

An `if` check only tests a condition on a value that already exists, but `int("abc")` fails at the moment of conversion, before the `if` ever runs, so Python raises a `ValueError` and the program crashes. A `try`/`except` block is needed because it catches the error while it is happening, and an `if` cannot anticipate every kind of bad input.

## How to run

```bash
python safe_tools.py
python unbreakable.py
```