"""
1137. N-th Tribonacci Number
Difficulty: Easy
Category: DP - 1D
https://leetcode.com/problems/n-th-tribonacci-number/

The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and
Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. Given n, return the value of Tn.

Example 1:
  Input: n = 4
  Output: 4

Example 2:
  Input: n = 25
  Output: 1389537

Constraints:
  0 <= n <= 37
  The answer is guaranteed to fit within a 32-bit integer.

Hints:
  - Roll three variables forward; no need for a full DP array.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((4,), 4),
        ((25,), 1389537),
        ((0,), 0),
        ((1,), 1),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.tribonacci(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
