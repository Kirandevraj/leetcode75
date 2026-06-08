"""
435. Non-overlapping Intervals
Difficulty: Medium
Category: Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals where intervals[i] = [starti, endi], return the
minimum number of intervals you need to remove to make the rest of the intervals
non-overlapping. Note that intervals which only touch at a point are
non-overlapping.

Example 1:
  Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
  Output: 1

Example 2:
  Input: intervals = [[1,2],[1,2],[1,2]]
  Output: 2

Example 3:
  Input: intervals = [[1,2],[2,3]]
  Output: 0

Constraints:
  1 <= intervals.length <= 10^5
  intervals[i].length == 2
  -5 * 10^4 <= starti < endi <= 5 * 10^4

Hints:
  - Greedy: sort by end, keep intervals that start at or after the last kept end.
"""


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
        (([[1, 2], [1, 2], [1, 2]],), 2),
        (([[1, 2], [2, 3]],), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.eraseOverlapIntervals(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
