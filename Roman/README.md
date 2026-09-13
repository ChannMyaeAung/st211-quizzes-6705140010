# Roman Numeral Converter

A Python module that converts between Roman numerals and integers, with strict
validation of canonical Roman numeral rules.

## Files

- `roman.py` — converter implementation (`roman_to_integer`, `integer_to_roman`)
- `test_roman.py` — pytest test suite covering valid and invalid inputs

## Usage

### As a module

```python
from roman import roman_to_integer, integer_to_roman

roman_to_integer("XIV")      # 14
integer_to_roman(2026)       # "MMXXVI"
```

### Interactive CLI

Run the script directly for a prompt/answer loop:

```bash
python roman.py
```

## Validation rules

- Accepts lower- and uppercase input
- Rejects empty strings and non-Roman characters
- `V`, `L`, and `D` may not repeat
- `I`, `X`, `C`, and `M` may not repeat more than 3 times
- Only the 6 standard subtractive pairs are allowed: `IV`, `IX`, `XL`, `XC`, `CD`, `CM`
- Result must be in the range 1–3999
- Non-canonical formats (e.g. `IIV`, `CMCC`) are rejected by re-encoding the result

## Running tests

```bash
python -m pytest
```