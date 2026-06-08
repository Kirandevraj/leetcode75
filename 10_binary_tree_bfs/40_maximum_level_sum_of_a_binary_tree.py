"""
1161. Maximum Level Sum of a Binary Tree
Difficulty: Medium
Category: Binary Tree - BFS
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on. Return the smallest level x such that the sum of all
the values of nodes at level x is maximal.

Example 1:
  Input: root = [1,7,0,7,-8,null,null]
  Output: 2

Example 2:
  Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
  Output: 2

Constraints:
  The number of nodes is in the range [1, 10^4].
  -10^5 <= Node.val <= 10^5

Hints:
  - BFS by level summing values; remember the level of the maximum sum.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    def build(vals):
        if not vals:
            return None
        nodes = [None if v is None else TreeNode(v) for v in vals]
        kids = nodes[1:][::-1]
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return nodes[0]
    s = Solution()
    cases = [
        ([1, 7, 0, 7, -8, None, None], 2),
        ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2),
    ]
    passed = 0
    for vals, expected in cases:
        try:
            got = s.maxLevelSum(build(vals))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
