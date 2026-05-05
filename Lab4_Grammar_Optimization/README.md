# Lab 4 - Elimination of Ambiguity, Left Recursion and Left Factoring

## Aim
To eliminate left recursion and perform left factoring.

## Algorithm
1. Identify left recursion A → Aα | β
2. Convert:
   A → βA'
   A' → αA' | ε
3. Apply left factoring if needed

## Input
A → A a | b

## Output
A → bA'
A' → aA' | ε

## Result
Grammar optimized successfully.
