"""
338. Counting Bits
Difficulty: Easy
Category: Bit Manipulation
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
  Input: n = 2
  Output: [0,1,1]

Example 2:
  Input: n = 5
  Output: [0,1,1,2,1,2]

Constraints:
  0 <= n <= 10^5

Hints:
  - ans[i] = ans[i >> 1] + (i & 1).
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((2,), [0, 1, 1]),
        ((5,), [0, 1, 1, 2, 1, 2]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.countBits(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
