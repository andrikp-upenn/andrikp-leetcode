# 🧮 Two Sum

## 📝 Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

## 🔍 Approach
- Create a hashmap to store seen values and their indices.
- For each number, check if `target - number` exists in the map.
- If it does, return the indices.

## 💡 Key Concepts
- Hash Maps / Dictionaries
- Single pass traversal
- Constant time lookups

## 📈 Complexity
- Time: O(n)
- Space: O(n)

## ✅ Status
- [x] Solved
- Language: C++
