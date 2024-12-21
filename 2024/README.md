# Advent of Code 2024

As every year, shout out to the wonderful [AoC community on reddit](https://www.reddit.com/r/adventofcode/).

Overview of Problems in 2024:

### [Day 1 Python](day01/solution.py)

As always day1 is just warming up. Some regex and Counter did the trick.

### [Day 2 Python](day02/solution.py)

For Part1, Checking monotonicity on diffs worked.

For Part2, just iterate, remove number and check. Not complicated.

### [Day 3 Python](day03/solution.py)

Regex did the trick, no surprises here.

### [Day 4 Python](day04/solution.py)

For Part1, find every `X` and search in all eight directions.

For Part2, find every `A` and search diagonally for `MAS` or `SAM`

### [Day 5 Python](day05/solution.py)

Wanted to write a custom comparator using `functools.cmp_to_key` but was not able to get it working. 
At the end went with dictionary and O[n^2] loop.

For Part2, swap and check if report is safe, using the code from Part1.

### [Day 6 Python](day06/solution.py)

Part1 was simple enough, move around the grid until you exit. Didn't do any optimization since simulating one step at a time is good enough.

For Part2, answer is to put obstacle on each point of original guard path and check if path is looped. Did some optimizations:
- First optimization, don't start for checking path loop from start but just before the obstacle position. It is because after obstacle path is going to change, hence why check from start. It bought my brute force approach time from ~10s to 2.5s. But my challenge was to get a solution under 1s.
- Second optimization, only save visited states at turns during loop check. This bought the runtime to around ~0.5s. Not very happy but good enough.

There is one optimization that can be done, is instead of going 1 step at a time, teleport to turns. My challenge was done, and I did not had enough motivation to do this.

### [Day 7 Python](day07/solution.py)

At high level, this is just about permutations.

For Part1, just did a brute force on permutations using recursion.

For Part2, brute also worked, but it took long enough 3-4s to get an answer. Got a hint from reddit, though wasn't looking for it. Instead of starting from first number, start from last, it will prune lot of unwanted branches a lot faster. 

### [Day 8 Python](08/solution.py)

It was easy enough, required some set operations, thats all.

### [Day 9 Python](day09/solution.py)

Part1 was okay, got it right in first try.

Solving Part2 was not hard for me. Hard part was optimizing it to run in <1s. I had to create a custom class to code clean and understandable. There were two optimization I did:
- First, kept empty length pre calculated instead of calculating every time
- Second, kept track of fully filled blocks.
Still my solution takes around 0.45s, I am not happy with this runtime, but don't have motivation to rethink it. People on reddit have given a [O[n] solution](https://www.reddit.com/r/adventofcode/comments/1hab624/2024_day_9_part_2_best_i_can_do_is_ond_log_n_is/) instead O[nlog(n)].


### [Day 10 Python](day10/solution.py)

DFS worked. And like a [common meme on reddit](https://www.reddit.com/r/adventofcode/comments/1haulfr/2024_day_10_part_2_when_your_first_attempt_at/), I did Part2 before Part1.

### [Day 11 Python](day11/solution.py)

Part1, did an brute force and got an answer quickly.

Part2, after seeing my code running for 20-30mins i realized brute force is not going to work. First I started with storing transformations, then the number of stones which did the trick.

<!-- * [Day 12 Python](12/d12.py): BFS (**R**), finding islands in 2d grid (**R**) and finding sides of a 2D polygon (**L**) -->

### [Day 13 Python](day13/solution.py)

This was easy, i didn't went for brute force. It was simple pair of linear equations solved by linear algebra [I used that] or Cramer's rule.

### [Day 14 Python](day14/solution.py)

Part1 is straightforward, nothing much to say here.
Part2, I implemented in two ways, one is iterating every second and checking for horizontal lines.

Another idea, i got from reddit is find the offset of horizontal and vertical lines, and use loop or [chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) to find N that will have these offsets at first occurrence i.e

```
N = x_offset * a % 101
N = y_offset * b % 103
```

### [Day 15 Python](day15/solution.py)

For part1, In moving box, one trick of optimizing is just teleport the box to first free position we find. Its equivalent of shifting all the boxes.

For part2, Break the moves in horizontal and vertical direction. 

For horizontal it is simple, just shift the blocks using list comprehension. For vertical, use a DFS to find if block can move. Also keep list of blocks with coords. At end if blocks can move, use the list that was made and apply it.
One edge case I missed was, two blocks referencing same block and getting added to list twice. Added a check for that.


### [Day 17 Python](day17/solution.py)

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