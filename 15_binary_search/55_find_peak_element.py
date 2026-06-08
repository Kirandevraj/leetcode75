"""
162. Find Peak Element
Difficulty: Medium
Category: Binary Search
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors. Given
a 0-indexed integer array nums, find a peak element, and return its index. If
the array contains multiple peaks, return the index to any of the peaks. You may
imagine that nums[-1] = nums[n] = -infinity. You must write an algorithm that
runs in O(log n) time.

Example 1:
  Input: nums = [1,2,3,1]
  Output: 2

Example 2:
  Input: nums = [1,2,1,3,5,6,4]
  Output: 5 (or 1)

Constraints:
  1 <= nums.length <= 1000
  -2^31 <= nums[i] <= 2^31 - 1
  nums[i] != nums[i + 1] for all valid i.

Hints:
  - Binary search: move toward the larger neighbor; you always climb to a peak.
"""


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [[1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [1], [1, 2]]
    passed = 0
    for nums in cases:
        try:
            i = s.findPeakElement(nums)
            left = nums[i - 1] if i > 0 else float("-inf")
            right = nums[i + 1] if i + 1 < len(nums) else float("-inf")
            ok = nums[i] > left and nums[i] > right
            detail = "index " + repr(i)
        except Exception as e:
            ok, detail = False, "<error: {}>".format(repr(e))
        passed += ok
        print(("PASS" if ok else "FAIL"), repr(nums), "=>", detail)
    print("{}/{} passed".format(passed, len(cases)))
