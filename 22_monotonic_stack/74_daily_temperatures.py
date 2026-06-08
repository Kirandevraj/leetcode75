"""
739. Daily Temperatures
Difficulty: Medium
Category: Monotonic Stack
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.

Example 1:
  Input: temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]

Example 2:
  Input: temperatures = [30,40,50,60]
  Output: [1,1,1,0]

Example 3:
  Input: temperatures = [30,60,90]
  Output: [1,1,0]

Constraints:
  1 <= temperatures.length <= 10^5
  30 <= temperatures[i] <= 100

Hints:
  - Keep a decreasing stack of indices; resolve waits when a warmer day arrives.
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]),
        (([30, 40, 50, 60],), [1, 1, 1, 0]),
        (([30, 60, 90],), [1, 1, 0]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.dailyTemperatures(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
