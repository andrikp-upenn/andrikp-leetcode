# 🧩 Valid Sudoku

## 📝 Problem Description
Given a `9 x 9` Sudoku board, determine if it is valid based on the following rules:

1. Each **row** must contain the digits `1-9` without duplicates.
2. Each **column** must contain the digits `1-9` without duplicates.
3. Each of the nine **3 x 3 sub-boxes** must contain the digits `1-9` without duplicates.

Return `true` if the board is valid, otherwise return `false`.

> **Note:** A board does not need to be full or solvable to be valid.

## 🔍 Approach
- Initialize a set for each of the 9 rows, 9 columns, and 9 sub-boxes to track seen digits.
- Iterate over every cell in the board. Skip cells containing `'.'`.
- For each digit, check if it already exists in its corresponding row set, column set, or sub-box set.
- If a duplicate is found in any of the three, return `False`.
- Map each cell `(i, j)` to its sub-box using integer division: `(i // 3, j // 3)`.
- If no duplicates are found after traversing the entire board, return `True`.

## 💡 Key Concepts
- Hash Sets for O(1) duplicate detection
- Sub-box indexing via integer division `(i // 3, j // 3)`
- Single-pass traversal of the entire board

## 📈 Complexity
- **Time:** O(n²) — we visit every cell in the n×n board once
- **Space:** O(n) — we store up to n values across each of the n rows, n columns, and n sub-boxes (27 sets total, each of size ≤ n)

## ✅ Status
- [x] Solved
- **Language:** Python