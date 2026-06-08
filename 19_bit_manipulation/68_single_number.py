"""
136. Single Number
Difficulty: Easy
Category: Bit Manipulation
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for
one. Find that single one. You must implement a solution with a linear runtime
complexity and use only constant extra space.

Example 1:
  Input: nums = [2,2,1]
  Output: 1

Example 2:
  Input: nums = [4,1,2,1,2]
  Output: 4

Example 3:
  Input: nums = [1]
  Output: 1

Constraints:
  1 <= nums.length <= 3 * 10^4
  -3 * 10^4 <= nums[i] <= 3 * 10^4
  Each element appears twice except for one which appears once.

Hints:
  - XOR all numbers; pairs cancel, leaving the unique value.
"""


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([2, 2, 1],), 1),
        (([4, 1, 2, 1, 2],), 4),
        (([1],), 1),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.singleNumber(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
