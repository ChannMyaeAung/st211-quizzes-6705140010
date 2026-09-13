# AST Exercises

A collection of small Python exercises for the AST course (192-201), each
centered around a module plus a pytest/unittest test suite.

## Projects

- [`Bank/`](Bank/README.md) — bank account and grade lettering
- [`Roman/`](Roman/README.md) — Roman numeral to/from integer conversion

## Setup

Install the dependencies into the project's virtual environment:

```bash
python3 -m venv venv
venv/bin/python -m pip install pytest
```

## Running tests

Run a project's tests from its folder:

```bash
cd Bank && ../venv/bin/python -m pytest
cd Roman && ../venv/bin/python -m pytest
```

Or run everything from the root:

```bash
venv/bin/python -m pytest Bank Roman
```