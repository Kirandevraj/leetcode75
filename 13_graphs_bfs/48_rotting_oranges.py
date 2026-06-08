"""
994. Rotting Oranges
Difficulty: Medium
Category: Graphs - BFS
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values: 0 (an
empty cell), 1 (a fresh orange), or 2 (a rotten orange). Every minute, any fresh
orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return
the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
  Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
  Output: 4

Example 2:
  Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
  Output: -1

Example 3:
  Input: grid = [[0,2]]
  Output: 0

Constraints:
  m == grid.length, n == grid[i].length, 1 <= m, n <= 10
  grid[i][j] is 0, 1, or 2.

Hints:
  - Multi-source BFS starting from all rotten oranges; track elapsed minutes.
"""


from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4),
        (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1),
        (([[0, 2]],), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.orangesRotting(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
