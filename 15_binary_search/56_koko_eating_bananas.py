"""
875. Koko Eating Bananas
Difficulty: Medium
Category: Binary Search
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours. Koko
decides her bananas-per-hour eating speed k. Each hour, she chooses a pile and
eats k bananas from it. If the pile has fewer than k bananas, she eats all of
them and will not eat any more during this hour. Return the minimum integer k
such that she can eat all the bananas within h hours.

Example 1:
  Input: piles = [3,6,7,11], h = 8
  Output: 4

Example 2:
  Input: piles = [30,11,23,4,20], h = 5
  Output: 30

Example 3:
  Input: piles = [30,11,23,4,20], h = 6
  Output: 23

Constraints:
  1 <= piles.length <= 10^4, piles.length <= h <= 10^9
  1 <= piles[i] <= 10^9

Hints:
  - Binary search speed k in [1, max(piles)]; hours = sum(ceil(p / k)).
"""


from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30),
        (([30, 11, 23, 4, 20], 6), 23),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.minEatingSpeed(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
