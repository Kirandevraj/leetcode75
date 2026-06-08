"""
2542. Maximum Subsequence Score
Difficulty: Medium
Category: Heap / Priority Queue
https://leetcode.com/problems/maximum-subsequence-score/

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n
and a positive integer k. You must choose a subsequence of indices from [0, n-1]
of length k. For chosen indices, your score is defined as: (sum of the selected
elements from nums1) multiplied by (the minimum of the selected elements from
nums2). Return the maximum possible score.

Example 1:
  Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
  Output: 12

Example 2:
  Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
  Output: 30

Constraints:
  n == nums1.length == nums2.length, 1 <= n <= 10^5
  0 <= nums1[i], nums2[j] <= 10^5, 1 <= k <= n

Hints:
  - Sort by nums2 descending; keep a min-heap of the k largest nums1 values.
"""


from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 3, 3, 2], [2, 1, 3, 4], 3), 12),
        (([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.maxScore(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
