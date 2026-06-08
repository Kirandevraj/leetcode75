"""
283. Move Zeroes
Difficulty: Easy
Category: Two Pointers
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements. You must do this in place without
making a copy of the array.

Example 1:
  Input: nums = [0,1,0,3,12]
  Output: [1,3,12,0,0]

Constraints:
  1 <= nums.length <= 10^4
  -2^31 <= nums[i] <= 2^31 - 1

Hints:
  - Keep a write index for the next non-zero slot; swap non-zeros forward.
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([1, 2, 3], [1, 2, 3])]
    passed = 0
    for nums, expected in cases:
        arr = list(nums)
        try:
            s.moveZeroes(arr)
            ok = arr == expected
        except Exception as e:
            arr, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(arr), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
