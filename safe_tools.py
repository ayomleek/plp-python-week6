"""safe_tools.py - small helper functions that never crash on bad input."""


def safe_divide(a, b):
    """Return a / b, or a message if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    """Convert text to a whole number, or return a message if it can't be done."""
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    """Return learner[key], or a message if the key is missing."""
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


# ---- Tests ----
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))