"""
2352. Equal Row and Column Pairs
Difficulty: Medium
Category: Hash Map / Set
https://leetcode.com/problems/equal-row-and-column-pairs/

Given a 0-indexed n x n integer matrix grid, return the number of pairs
(ri, cj) such that row ri and column cj are equal. A row and column pair is
considered equal if they contain the same elements in the same order.

Example 1:
  Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
  Output: 1

Example 2:
  Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
  Output: 3

Constraints:
  n == grid.length == grid[i].length
  1 <= n <= 200
  1 <= grid[i][j] <= 10^5

Hints:
  - Hash each row tuple; for each column tuple, count matching rows.
"""


from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[3, 2, 1], [1, 7, 6], [2, 7, 7]],), 1),
        (([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],), 3),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.equalPairs(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
