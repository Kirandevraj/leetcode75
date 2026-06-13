"""
1732. Find the Highest Altitude
Difficulty: Easy
Category: Prefix Sum
https://leetcode.com/problems/find-the-highest-altitude/

There is a biker going on a road trip consisting of n + 1 points at different
altitudes. The biker starts at point 0 with altitude 0. You are given an integer
array gain of length n where gain[i] is the net gain in altitude between points
i and i + 1. Return the highest altitude of a point.

Example 1:
  Input: gain = [-5,1,5,0,-7]
  Output: 1

Example 2:
  Input: gain = [-4,-3,-2,-1,4,3,2]
  Output: 0

Constraints:
  n == gain.length
  1 <= n <= 100
  -100 <= gain[i] <= 100

Hints:
  - Track a running prefix sum and its maximum (starting at 0).
"""


from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        highest_alt = 0
        for i in range(len(gain)):
            prefix_sum += gain[i]
            if prefix_sum > highest_alt:
                # print(highest_alt)
                highest_alt = prefix_sum
        return highest_alt



if __name__ == "__main__":
    s = Solution()
    cases = [
        (([-5, 1, 5, 0, -7],), 1),
        (([-4, -3, -2, -1, 4, 3, 2],), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.largestAltitude(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
