"""
605. Can Place Flowers
Difficulty: Easy
Category: Array / String
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some plots are planted and some are not.
Flowers cannot be planted in adjacent plots. Given an integer array flowerbed
containing 0's (empty) and 1's (planted) and an integer n, return true if n new
flowers can be planted without violating the no-adjacent-flowers rule.

Example 1:
  Input: flowerbed = [1,0,0,0,1], n = 1
  Output: true

Example 2:
  Input: flowerbed = [1,0,0,0,1], n = 2
  Output: false

Constraints:
  1 <= flowerbed.length <= 2 * 10^4
  flowerbed[i] is 0 or 1.
  There are no two adjacent flowers in flowerbed.
  0 <= n <= flowerbed.length

Hints:
  - Greedily plant when a plot and both neighbors are empty (treat out-of-bounds as empty).
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
              left = (i == 0) or flowerbed[i-1] == 0
              right = (i == len(flowerbed)-1) or flowerbed[i+1] == 0
              if left and right:
                  flowerbed[i] = 1
                  n -= 1
        return n <= 0
        


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 0, 0, 0, 1], 1), True),
        (([1, 0, 0, 0, 1], 2), False),
        (([0], 0), True),
        (([0, 0, 0], 2), True),
        (([0, 0], 1), True),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.canPlaceFlowers(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
