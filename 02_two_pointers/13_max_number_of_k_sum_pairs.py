"""
1679. Max Number of K-Sum Pairs
Difficulty: Medium
Category: Two Pointers
https://leetcode.com/problems/max-number-of-k-sum-pairs/

You are given an integer array nums and an integer k. In one operation, you can
pick two numbers from the array whose sum equals k and remove them. Return the
maximum number of operations you can perform on the array.

Example 1:
  Input: nums = [1,2,3,4], k = 5
  Output: 2

Example 2:
  Input: nums = [3,1,3,4,3], k = 6
  Output: 1

Constraints:
  1 <= nums.length <= 10^5
  1 <= nums[i] <= 10^9
  1 <= k <= 10^9

Hints:
  - Sort and use two pointers, or count complements with a hash map.
"""


from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        pairs = 0
        L = 0
        R = len(nums) - 1
        while (L < R):
            if (nums[L] + nums[R] == k):
                pairs += 1
                R -= 1
                L += 1
            elif (nums[L] + nums[R] > k):
                R -= 1
            else:
                L += 1
        return pairs


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 2, 3, 4], 5), 2),
        (([3, 1, 3, 4, 3], 6), 1),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.maxOperations(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
