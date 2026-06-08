"""
215. Kth Largest Element in an Array
Difficulty: Medium
Category: Heap / Priority Queue
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in
the array. Note that it is the kth largest element in the sorted order, not the
kth distinct element. Can you solve it without sorting?

Example 1:
  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5

Example 2:
  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
  Output: 4

Constraints:
  1 <= k <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
  - Maintain a min-heap of size k, or use quickselect for O(n) average.
"""


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([3, 2, 1, 5, 6, 4], 2), 5),
        (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.findKthLargest(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
