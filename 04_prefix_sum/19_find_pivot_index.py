"""
724. Find Pivot Index
Difficulty: Easy
Category: Prefix Sum
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index. The pivot index is
where the sum of all numbers strictly to the left equals the sum of all numbers
strictly to the right. If the index is on the left edge, the left sum is 0.
Return the leftmost pivot index, or -1 if none exists.

Example 1:
  Input: nums = [1,7,3,6,5,6]
  Output: 3

Example 2:
  Input: nums = [1,2,3]
  Output: -1

Example 3:
  Input: nums = [2,1,-1]
  Output: 0

Constraints:
  1 <= nums.length <= 10^4
  -1000 <= nums[i] <= 1000

Hints:
  - For each i, left_sum and total give the right sum: total - left - nums[i].
"""


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 7, 3, 6, 5, 6],), 3),
        (([1, 2, 3],), -1),
        (([2, 1, -1],), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.pivotIndex(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
