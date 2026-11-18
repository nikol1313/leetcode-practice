# LeetCode

[![tests](https://github.com/nikol1313/leetcode-practice/actions/workflows/tests.yml/badge.svg)](https://github.com/nikol1313/leetcode-practice/actions/workflows/tests.yml)

DSA practice in **Python** and **JavaScript**, organized by topic. Every solution is fully tested
(pytest + Vitest) and checked in CI.

## Setup

```bash
# Python (3.12+)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt

# JavaScript (Node 22+)
npm install
```

## Running tests and linters

```bash
# Python
pytest            # all tests
ruff check .      # lint

# JavaScript
npm test          # vitest run
npm run lint      # eslint
npm run format    # prettier --write
```

Run a single problem: `pytest problems/arrays_hashing/0001_two_sum` or
`npx vitest run problems/arrays_hashing/0001_two_sum`.

## Adding a problem

```bash
python scripts/new_problem.py 1 "two sum" arrays_hashing easy --lang both   # or --lang py / js
```

This copies `_template/` into `problems/<topic>/<NNNN>_<name>/` (only the files for the chosen
languages), fills in the README header, and adds a row to the table below. Then replace the stub
signature and the example test cases with the real ones.

Topics: `arrays_hashing`, `two_pointers`, `sliding_window`, `stack`, `binary_search`,
`linked_list`, `trees`, `graphs`, `dynamic_programming`, `greedy`.

## Progress

<!-- stats:start -->

**Easy:** 0 · **Medium:** 0 · **Hard:** 0 · **Total:** 0
<!-- stats:end -->

<!-- problems:start -->

| #   | Problem | Difficulty | Topic | Python | JavaScript |
| --- | ------- | ---------- | ----- | ------ | ---------- |

<!-- problems:end -->
