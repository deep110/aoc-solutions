# Advent of Code 2020

Overview of Problems in 2020:

### [Day 11](day11/solution.py)

Part1 was easy enough, but runtime was 300ms. Implementing caching for neighbors reduced it to half.
For Part2, didn't need to anything extra, was able to get the answer in around 200ms.

### [Day 12](day12/solution.py)

Part 1 is again easy and straight forward. Direction shenanigans are done by module operation.

Part2, required vector rotation, since angles are multiples of 90°, we can avoid trigonometric functions, using complex algebra.

### [Day 13](day13/solution.py)

Part1 was straightforward, nothing to think there.

Part2 required to use Chinese remainder theorem, to find answer quickly. Hard part was figuring out the remainders. I used [this reference](https://www.geeksforgeeks.org/implementation-of-chinese-remainder-theorem-inverse-modulo-based-implementation/) to understand the theorem and how to implement it.


### [Day 14](day14/solution.py)

For Part2, I am iterating over total number of combinations, ie 2 ^ (number_X), and filling each number's binary representation into locations of X. No need of recursion.


### [Day 17](day17/solution.py)

While a solution for both parts using a state and grid and just lists was easy enough to add, it took 1.7s to complete both parts.
Then I saw few [solutions on reddit](https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/), lot of people using python recommend using dict and key being tuple of indexes. 

In my own input, only about 4% of the 3D space ended up being active, and 2% of my 4D space ends up being active. This means that holding a dense vector of all possible active points (which will be (6+8+6)^n) is up to 98% wasteful. Hence dict is very memory efficient, if you only need to keep track of active coordinates.

Also, we are doing reverse, instead of looping on each coordinate and finding active neighbors, we are
looking into each active coordinate and adding 1 to each neighbor.
This also helps to speed up a lot, because state change requires some minimum active neighbors to be present, so we only loop on coordinates which has at least 1 active neighbor.
