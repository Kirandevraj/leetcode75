"""
790. Domino and Tromino Tiling
Difficulty: Medium
Category: DP - 1D
https://leetcode.com/problems/domino-and-tromino-tiling/

You have two types of tiles: a 2 x 1 domino shape and a tromino shape (an
L-shape covering three cells). You may rotate these shapes. Given an integer n,
return the number of ways to tile a 2 x n board. Since the answer may be very
large, return it modulo 10^9 + 7. Two tilings are different if and only if there
are two 4-directionally adjacent cells on the board such that exactly one of the
tilings has both cells covered by the same tile.

Example 1:
  Input: n = 3
  Output: 5

Example 2:
  Input: n = 1
  Output: 1

Constraints:
  1 <= n <= 1000

Hints:
  - Recurrence: f(n) = 2*f(n-1) + f(n-3), all modulo 1e9+7.
"""


class Solution:
    def numTilings(self, n: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((3,), 5),
        ((1,), 1),
        ((5,), 24),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.numTilings(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
