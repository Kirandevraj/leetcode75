"""
198. House Robber
Difficulty: Medium
Category: DP - 1D
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night. Given an integer array nums representing the amount of money
of each house, return the maximum amount of money you can rob tonight without
alerting the police.

Example 1:
  Input: nums = [1,2,3,1]
  Output: 4

Example 2:
  Input: nums = [2,7,9,3,1]
  Output: 12

Constraints:
  1 <= nums.length <= 100
  0 <= nums[i] <= 400

Hints:
  - dp[i] = max(dp[i-1], dp[i-2] + nums[i]); track two rolling values.
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 2, 3, 1],), 4),
        (([2, 7, 9, 3, 1],), 12),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.rob(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
