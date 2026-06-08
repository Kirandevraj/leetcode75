"""
1926. Nearest Exit from Entrance in Maze
Difficulty: Medium
Category: Graphs - BFS
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

You are given an m x n matrix maze (0-indexed) with empty cells (represented as
'.') and walls (represented as '+'). You are also given the entrance, where
entrance = [row, col]. In one step you can move one cell up, down, left or right.
You cannot step into a wall or outside the maze. Your goal is to find the nearest
exit: an empty cell at the border of the maze that is not the entrance. Return
the number of steps to the nearest exit, or -1 if none exists.

Example 1:
  Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
         entrance = [1,2]
  Output: 1

Example 2:
  Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
  Output: 2

Constraints:
  maze.length == m, maze[i].length == n, 1 <= m, n <= 100
  Each cell is '.' or '+'; entrance is an empty cell.

Hints:
  - BFS from the entrance; the first border empty cell reached is the answer.
"""


from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([['+', '+', '.', '+'], ['.', '.', '.', '+'], ['+', '+', '+', '.']], [1, 2]), 1),
        (([['+', '+', '+'], ['.', '.', '.'], ['+', '+', '+']], [1, 0]), 2),
        (([['.', '+']], [0, 0]), -1),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.nearestExit(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
