"""
334. Increasing Triplet Subsequence
Difficulty: Medium
Category: Array / String
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exist, return false.

Example 1:
  Input: nums = [1,2,3,4,5]
  Output: true

Example 2:
  Input: nums = [5,4,3,2,1]
  Output: false

Example 3:
  Input: nums = [2,1,5,0,4,6]
  Output: true (triplet (3,4,5) -> 0,4,6)

Constraints:
  1 <= nums.length <= 5 * 10^5
  -2^31 <= nums[i] <= 2^31 - 1

Hints:
  - Track the smallest and second-smallest seen so far; a third larger value wins.
"""


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 2, 3, 4, 5],), True),
        (([5, 4, 3, 2, 1],), False),
        (([2, 1, 5, 0, 4, 6],), True),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.increasingTriplet(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
