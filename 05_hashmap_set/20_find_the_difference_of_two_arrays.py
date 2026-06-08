"""
2215. Find the Difference of Two Arrays
Difficulty: Easy
Category: Hash Map / Set
https://leetcode.com/problems/find-the-difference-of-two-arrays/

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
size 2 where: answer[0] is a list of all distinct integers in nums1 not present
in nums2, and answer[1] is a list of all distinct integers in nums2 not present
in nums1. The integers in each list may be returned in any order.

Example 1:
  Input: nums1 = [1,2,3], nums2 = [2,4,6]
  Output: [[1,3],[4,6]]

Constraints:
  1 <= nums1.length, nums2.length <= 1000
  -1000 <= nums1[i], nums2[i] <= 1000

Hints:
  - Convert to sets and take set differences in both directions.
"""


from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [(([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]]), (([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []])]
    passed = 0
    for args, expected in cases:
        try:
            got = s.findDifference(*args)
            ok = len(got) == 2 and sorted(got[0]) == sorted(expected[0]) and sorted(got[1]) == sorted(expected[1])
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
