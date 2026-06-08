"""
1004. Max Consecutive Ones III
Difficulty: Medium
Category: Sliding Window
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
  Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
  Output: 6

Example 2:
  Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
  Output: 10

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is 0 or 1.
  0 <= k <= nums.length

Hints:
  - Grow a window while it contains at most k zeros; shrink from the left otherwise.
"""


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
        (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.longestOnes(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
