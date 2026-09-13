# Bank

A set of Python exercises for the AST course: a bank account class and a
letter-grading function, each with tests.

## Files

- `bank.py` — `BankAccount` class with deposit/withdraw and balance tracking
- `grades.py` — `letter_grade(score)` returning a letter grade for 0–100
- `test_bank.py` — pytest tests for `BankAccount`
- `test_grades.py` — pytest tests for `letter_grade`, including boundary and error cases
- `test_dependent.py` — pytest tests that share a single `BankAccount` instance

## Usage

```python
from bank import BankAccount

account = BankAccount(100)
account.deposit(50)     # 150
account.withdraw(30)    # 120
```

```python
from grades import letter_grade

letter_grade(85)    # "A"
letter_grade(59)    # "F"
```

## Behavior

### BankAccount

- `deposit(amount)` adds to the balance and returns it; raises `ValueError` for
  non-positive amounts
- `withdraw(amount)` subtracts from the balance and returns it; raises
  `ValueError` if the amount exceeds the current balance

### letter_grade

| Score  | Grade |
|--------|-------|
| 80–100 | A     |
| 70–79  | B     |
| 60–69  | C     |
| 0–59   | F     |

Scores outside 0–100 raise `ValueError`. Tests cover the exact boundaries
(e.g. 80 is an A, 79 is a B).

## Running tests

```bash
python -m pytest           # from this folder
../venv/bin/python -m pytest
```