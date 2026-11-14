# Making Change

## Description

This project is part of the Holberton School Interview Preparation curriculum.

The objective is to find the minimum number of coins needed to make a given amount using a list of available coin denominations.

The project focuses on problem-solving, algorithm optimization, and dynamic programming.

## Learning Objectives

- Understand the coin change problem.
- Apply dynamic programming to solve optimization problems.
- Find the minimum number of coins required for a given amount.
- Handle edge cases and impossible combinations.
- Understand time and space complexity.

## Requirements

- Python 3
- PEP 8 coding style
- All Python files must be executable.

## Files

| File | Description |
|---|---|
| `0-making_change.py` | Implements the `makeChange(coins, total)` function. |
| `README.md` | Project documentation. |

## Algorithm

The solution uses **Dynamic Programming** to calculate the minimum number of coins needed for each amount from 0 to the target total.

The function returns:

- The minimum number of coins if the total can be reached.
- `0` if the total is zero or negative.
- `-1` if the total cannot be reached.

**Time Complexity:** O(total × number of coin denominations)

**Space Complexity:** O(total)

## Usage

Import the function into a Python script:

```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
```

Expected output:

```text
7
-1
```

## Author

Dana Ibrahim Alsalman

Holberton School Student
