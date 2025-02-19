# Advent of Code 2024

As every year, shout out to the wonderful [AoC community on reddit](https://www.reddit.com/r/adventofcode/).

Overview of Problems in 2024:

### [Day 1](day01/solution.py)

As always day1 is just warming up. Some regex and Counter did the trick.

### [Day 2](day02/solution.py)

For Part1, Checking monotonicity on diffs worked.

For Part2, just iterate, remove number and check. Not complicated.

### [Day 3](day03/solution.py)

Regex did the trick, no surprises here.

### [Day 4](day04/solution.py)

For Part1, find every `X` and search in all eight directions.

For Part2, find every `A` and search diagonally for `MAS` or `SAM`

### [Day 5](day05/solution.py)

Wanted to write a custom comparator using `functools.cmp_to_key` but was not able to get it working. 
At the end went with dictionary and O[n^2] loop.

For Part2, swap and check if report is safe, using the code from Part1.

### [Day 6](day06/solution.py)

Part1 was simple enough, move around the grid until you exit. Didn't do any optimization since simulating one step at a time is good enough.

For Part2, answer is to put obstacle on each point of original guard path and check if path is looped. Did some optimizations:
- First optimization, don't start for checking path loop from start but just before the obstacle position. It is because after obstacle path is going to change, hence why check from start. It bought my brute force approach time from ~10s to 2.5s. But my challenge was to get a solution under 1s.
- Second optimization, only save visited states at turns during loop check. This bought the runtime to around ~0.5s.
- Third Optimization, instead of visiting every point in grid, teleport to stones, bought the runtime to approx 0.060s.

### [Day 7](day07/solution.py)

At high level, this is just about permutations.

For Part1, just did a brute force on permutations using recursion.

For Part2, brute also worked, but it took long enough 3-4s to get an answer. Got a hint from reddit, though wasn't looking for it. Instead of starting from first number, start from last, it will prune lot of unwanted branches a lot faster. 

### [Day 8](08/solution.py)

It was easy enough, required some set operations, thats all.

### [Day 9](day09/solution.py)

Part1 was okay, got it right in first try.

Solving Part2 was not hard for me. Hard part was optimizing it to run in <1s. I had to create a custom class to code clean and understandable. There were two optimization I did:
- First, kept empty length pre calculated instead of calculating every time
- Second, kept track of fully filled blocks. This bought runtime to 0.45s, which is okay.
- I got inspired by this [O[n] solution](https://www.reddit.com/r/adventofcode/comments/1hab624/2024_day_9_part_2_best_i_can_do_is_ond_log_n_is/) instead O[nlog(n)], this bought it to ~0.040s, i.e 10x speedup.


### [Day 10](day10/solution.py)

DFS worked. And like a [common meme on reddit](https://www.reddit.com/r/adventofcode/comments/1haulfr/2024_day_10_part_2_when_your_first_attempt_at/), I did Part2 before Part1.

### [Day 11](day11/solution.py)

Part1, did an brute force and got an answer quickly.

Part2, after seeing my code running for 20-30mins i realized brute force is not going to work. First I started with storing transformations, then the number of stones which did the trick.

### [Day 12](day12/solution.py)

For Part1, I implemented a simple DFS, and counted the boundaries and number of points.

For Part2, I counted the corners. Took some time to think on how to count concave corners.

### [Day 13](day13/solution.py)

This was easy, i didn't went for brute force. It was simple pair of linear equations solved by linear algebra [I used that] or Cramer's rule.

### [Day 14](day14/solution.py)

Part1 is straightforward, nothing much to say here.
Part2, I implemented in two ways, one is iterating every second and checking for horizontal lines.

Another idea, i got from reddit is find the offset of horizontal and vertical lines, and use loop or [chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) to find N that will have these offsets at first occurrence i.e

```
N = x_offset * a % 101
N = y_offset * b % 103
```

### [Day 15](day15/solution.py)

For part1, In moving box, one trick of optimizing is just teleport the box to first free position we find. Its equivalent of shifting all the boxes.

For part2, Break the moves in horizontal and vertical direction. 

For horizontal it is simple, just shift the blocks using list comprehension. For vertical, use a DFS to find if block can move. Also keep list of blocks with coords. At end if blocks can move, use the list that was made and apply it.
One edge case I missed was, two blocks referencing same block and getting added to list twice. Added a check for that.


### [Day 16](day16/solution.py)

Since we know the start and end node, I used Astar algorithm. Idea is to use manhattan distance as heuristic metric and step and turn cost as actual cost. 

For part2, I had to think and try out the modifications, at end figured out that I am keeping single source value for every destination, changing that to list helped to keep track of multiple looping paths with same cost.


### [Day 17](day17/solution.py)

Part 1, was easy enough, nothing hard there.

Part2, had me up for multiple days. First I was trying brute force, but then quickly realized, it is not going to work and especially with < 1s challenge. Got some hints from reddit to look into what program does actually. 

```py
while True:
    regB = (regA % 8) ^ 1
    regC = regA // (2**regB)
    regB = regB ^ regC ^ 6
    regA = regA // 8

    output.append(regB % 8)
    if regA == 0:
        break
```

Even after understanding the program took me some time to get the code working.


### [Day 18](day18/solution.py)

This day is very simple, I used my Day16 A* search code. Later realized cost is always 1 and heuristics is just adding more calculations and is not actually need. 

For Part2, first I iterated over the input to get the correct answer, but then saw that it is taking a lot of time. I was thinking of adding memoization, but smart folks on reddit suggested to try binary search, which reduced my time from 18s to few milliseconds.


### [Day 19](day19/solution.py)

I was on wrong track, tried using lot of logic for backtracking etc. Got some hints from reddit to use a recursive solution, which clicked with me.
For Part2, I had to use a memoization to get the result quickly. Later I combined both part1 and part2 into single function.


### [Day 22](day22/solution.py)

Problem was easy, main challenge was to reduce the runtime under 1s. My time is almost 1.2s after all the optimizations I can think of or people did on reddit. I guess it is one of those problems where you have to live with it.


### [Day 23](day23/solution.py)

Part1, was okay, was able to work out the solution after thinking for a while.

For part2, i had the basic brute force method in mind. After some research and hints on reddit found out about Bron-Kerbosch algorithm for finding maximal cliques in the graph. Largest Maximal clique was our answer.

Basic implementation of algo, gave the correct answer but was taking around 220ms. Found out about speeding up the algo using pivots to reduce number of vertices we need to process. This reduced the runtime to around 8.2ms.
