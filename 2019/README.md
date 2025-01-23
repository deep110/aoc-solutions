# Advent of Code 2019

Overview of Problems in 2019:

### [Day 3](day03/solution.py)

My first solution was to add all points in a set and take intersection with points of other wire. This took around 75ms. 
On subreddit, I found this [blog](https://emlun.se/advent-of-code-2019/2020/08/26/followup-day03-revisited.html) which explains how to solve for intersection of segments directly and also why that is faster than taking every point. It reduced my runtime to ~35ms.
There’s one more trick we can use to go even faster, though: we don’t need to test every pair of line segments. Instead, we can split the first wire into the line segments parallel with the x axis, and the ones parallel with the y axis. We can then sort each vector by y and x coordinate, respectively. This allows us to binary search for just the range of segments that have a chance to intersect the other wire. I haven't implemented this yet.
