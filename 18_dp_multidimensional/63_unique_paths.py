"""
62. Unique Paths
Difficulty: Medium
Category: DP - Multidimensional
https://leetcode.com/problems/unique-paths/

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at
any point in time. Given the two integers m and n, return the number of possible
unique paths that the robot can take to reach the bottom-right corner.

Example 1:
  Input: m = 3, n = 7
  Output: 28

Example 2:
  Input: m = 3, n = 2
  Output: 3

Constraints:
  1 <= m, n <= 100

Hints:
  - dp[i][j] = dp[i-1][j] + dp[i][j-1]; a single row suffices for O(n) space.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((3, 7), 28),
        ((3, 2), 3),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.uniquePaths(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
