"""
452. Minimum Number of Arrows to Burst Balloons
Difficulty: Medium
Category: Intervals
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

There are some spherical balloons taped onto a flat wall. The balloons are
given as an array points where points[i] = [xstart, xend] denotes a balloon
whose horizontal diameter stretches between xstart and xend. An arrow shot
vertically at x bursts a balloon if xstart <= x <= xend. Return the minimum
number of arrows that must be shot to burst all balloons.

Example 1:
  Input: points = [[10,16],[2,8],[1,6],[7,12]]
  Output: 2

Example 2:
  Input: points = [[1,2],[3,4],[5,6],[7,8]]
  Output: 4

Example 3:
  Input: points = [[1,2],[2,3],[3,4],[4,5]]
  Output: 2

Constraints:
  1 <= points.length <= 10^5
  points[i].length == 2, -2^31 <= xstart < xend <= 2^31 - 1

Hints:
  - Sort by end; shoot at each end, skipping balloons that overlap the current arrow.
"""


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[10, 16], [2, 8], [1, 6], [7, 12]],), 2),
        (([[1, 2], [3, 4], [5, 6], [7, 8]],), 4),
        (([[1, 2], [2, 3], [3, 4], [4, 5]],), 2),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.findMinArrowShots(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
