# Advent of Code 2020

Overview of Problems in 2020:

### [Day 11](day11/solution.py)

Part1 was easy enough, but runtime was 300ms. Implementing caching for neighbors reduced it to half.
For Part2, didn't need to anything extra, was able to get the answer in around 200ms.

### [Day 12](day12/solution.py)

Part 1 is again easy and straight forward. Direction shenanigans are done by module operation.

Part2, required vector rotation, since angles are multiples of 90°, we can avoid trigonometric functions, using complex algebra.

### [Day 13](day12/solution.py)

Part1 was straightforward, nothing to think there.

Part2 required to use Chinese remainder theorem, to find answer quickly. Hard part was figuring out the remainders. I used [this reference](https://www.geeksforgeeks.org/implementation-of-chinese-remainder-theorem-inverse-modulo-based-implementation/) to understand the theorem and how to implement it.
