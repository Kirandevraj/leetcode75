"""
2300. Successful Pairs of Spells and Potions
Difficulty: Medium
Category: Binary Search
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

You are given two positive integer arrays spells and potions, of length n and m
respectively, where spells[i] represents the strength of the ith spell and
potions[j] represents the strength of the jth potion. You are also given an
integer success. A spell and potion pair is considered successful if the product
of their strengths is at least success. Return an integer array pairs of length
n where pairs[i] is the number of potions that will form a successful pair with
the ith spell.

Example 1:
  Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
  Output: [4,0,3]

Example 2:
  Input: spells = [3,1,2], potions = [8,5,8], success = 16
  Output: [2,0,2]

Constraints:
  n == spells.length, m == potions.length, 1 <= n, m <= 10^5
  1 <= spells[i], potions[i] <= 10^5, 1 <= success <= 10^10

Hints:
  - Sort potions; for each spell binary-search the minimum qualifying potion.
"""


from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3]),
        (([3, 1, 2], [8, 5, 8], 16), [2, 0, 2]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.successfulPairs(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
