"""
1493. Longest Subarray of 1's After Deleting One Element
Difficulty: Medium
Category: Sliding Window
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array nums, you should delete one element from it. Return the
size of the longest non-empty subarray containing only 1's in the resulting
array. Return 0 if there is no such subarray.

Example 1:
  Input: nums = [1,1,0,1]
  Output: 3

Example 2:
  Input: nums = [0,1,1,1,0,1,1,0,1]
  Output: 5

Example 3:
  Input: nums = [1,1,1]
  Output: 2

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.

Hints:
  - Sliding window allowing at most one zero; answer is window length minus one.
"""


from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        zero_count = 0
        best = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                right += 1
            else:
                right += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            current = right - left
            if current > best:
                best = current
      
        return best-1
                



if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 1, 0, 1],), 3),
        (([0, 1, 1, 1, 0, 1, 1, 0, 1],), 5),
        (([1, 1, 1],), 2),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.longestSubarray(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
