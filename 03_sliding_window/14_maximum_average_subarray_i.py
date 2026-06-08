"""
643. Maximum Average Subarray I
Difficulty: Easy
Category: Sliding Window
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer within 10^-5 of the actual
answer will be accepted.

Example 1:
  Input: nums = [1,12,-5,-6,50,3], k = 4
  Output: 12.75

Constraints:
  n == nums.length
  1 <= k <= n <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
  - Maintain a running window sum of size k; track its maximum.
"""


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 12, -5, -6, 50, 3], 4), 12.75),
        (([5], 1), 5.0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.findMaxAverage(*args)
            ok = abs(got - expected) < 1e-5
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
