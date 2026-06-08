"""
1318. Minimum Flips to Make a OR b Equal to c
Difficulty: Medium
Category: Bit Manipulation
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

Given 3 positive numbers a, b and c. Return the minimum flips required in some
bits of a and b to make ( a OR b == c ). (bitwise OR operation). A flip
operation consists of changing any single bit 1 to 0 or changing any single bit
0 to 1 in their binary representation.

Example 1:
  Input: a = 2, b = 6, c = 5
  Output: 3

Example 2:
  Input: a = 4, b = 2, c = 7
  Output: 1

Example 3:
  Input: a = 1, b = 2, c = 3
  Output: 0

Constraints:
  1 <= a, b, c <= 10^9

Hints:
  - For each bit: if c-bit is 0, flip every set bit in a and b; if 1, flip if both are 0.
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((2, 6, 5), 3),
        ((4, 2, 7), 1),
        ((1, 2, 3), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.minFlips(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
