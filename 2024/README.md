# Advent of Code 2024



As every year, shout out to the wonderful [AoC community on reddit](https://www.reddit.com/r/adventofcode/).

Overview of Problems in 2024:

* [Day 1 Python](day01/solution.py):

As always day01 is just warming up. Some regex and Counter did the trick.

<!-- * [Day 2 Python](day02/solution.py):

* [Day 3 Python](03/d03.py): using logical operators in regex (**I**)
* [Day 4 Python](04/d04.py): operations on numpy arrays (rotate, diagonals) (**I**)
* [Day 5 Python](05/d05.py): set operations (**R**) and writing custom comparator for functools.cmp_to_key (**R**)
* [Day 6 Python](06/d06.py): storing grids in dictionaries (**R**)
* [Day 7 Python](07/d07.py): BFS (**R**) and Python operator (**R**) for a solution that's inefficient, but works; recursion (**I**) for an improved and much faster solution
* [Day 8 Python](08/d08.py): set operations (**R**)
* [Day 9 Python](09/d09.py): OH GOSH, WHAT THE HELL WAS THAT. Spent far too many hours debugging a seemingly simple solution, ended up refreshing itertools.cycle (**R**), deques (**R**) and thinking with pointers (**R**) before figuring out where the bug was
* [Day 10 Python](10/d10.py): iterative DFS (**R**)
* [Day 11 Python](11/d11.py): that you don't have to store everything that you count, just like [twice](https://github.com/Leftfish/Advent-of-Code-2021/blob/main/06/d06.py) in [2021](https://github.com/Leftfish/Advent-of-Code-2021/blob/main/14/d14.py) (**R**)
* [Day 12 Python](12/d12.py): BFS (**R**), finding islands in 2d grid (**R**) and finding sides of a 2D polygon (**L**)
* [Day 13 Python](13/d13.py): linear algebra (**I**) and Cramer's rule (**L**)
* [Day 14 Python](14/d14.py): using modulo (**R**) and saving plots made in matplotlib (**L**) (which I tried in a buggy solution what didn't make it to the final one) -->
* [Day 15 Python](day15/solution.py):

For part1, In moving box, one trick of optimizing is just teleport the box to first free position we find. Its equivalent of shifting all the boxes.

For part2, Break the moves in horizontal and vertical direction. 

For horizontal it is simple, just shift the blocks using list comprehension. For vertical, use a DFS to find if block can move. Also keep list of blocks with coords. At end if blocks can move, use the list that was made and apply it.
One edge case I missed was, two blocks referencing same block and getting added to list twice. Added a check for that.