# Shuting-Yard Algorithm

A mathematical expression parser and evaluator built in Python. Converts infix expressions (the way humans write math) into postfix notation using the Shunting-yard algorithm, then evaluates the result.

Supports multi-digit numbers, operator precedence, parentheses, exponentiation, and absolute value — all built from scratch.

---

## Features

- Parses and evaluates mathematical expressions from a string input
- Correct operator precedence (`*` and `/` before `+` and `-`)
- Supports parentheses for grouping
- Supports exponentiation (`^`)
- Supports `abs()` for absolute value
- Validates input and catches errors such as:
  - Invalid characters
  - Two operators in a row
  - Unbalanced parentheses
  - Expression ending in an operator

---

## Supported Operations

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `^` | Exponentiation |
| `abs(x)` | Absolute value |
| `(` `)` | Grouping |

---

## How to Run

```bash
python main.py
```

Then type a math expression when prompted:

```
3+5*2
> 13.0

(2+3)^2
> 25.0

abs(-7)+1
> 8.0
```

---

## How It Works

1. **Validation** — Scans the input for invalid characters, misplaced letters, double operators, and unbalanced parentheses
2. **Shunting-yard algorithm** — Converts the infix expression into postfix notation (Reverse Polish Notation), respecting operator precedence and associativity
3. **Evaluation** — Walks through the postfix stack and computes the final result

---

## About

Built at 15 years old, just a few months after learning Python. No tutorials, no teachers, no frameworks. Just wikipedia, trial and error.
