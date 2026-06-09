"""
11. Container With Most Water
Difficulty: Medium
Category: Two Pointers
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the
container holds the most water. Return the maximum amount of water it can store.

Example 1:
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49

Constraints:
  n == height.length
  2 <= n <= 10^5
  0 <= height[i] <= 10^4

Hints:
  - Two pointers at the ends; always move the shorter wall inward.
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        while (left != right):
            area = ((right - left) * min(height[left], height[right]))
            if area > maxarea:
                maxarea = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea



if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([1, 1],), 1),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.maxArea(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
