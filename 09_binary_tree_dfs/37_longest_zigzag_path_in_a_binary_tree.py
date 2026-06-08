"""
1372. Longest ZigZag Path in a Binary Tree
Difficulty: Medium
Category: Binary Tree - DFS
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

You are given the root of a binary tree. A ZigZag path is defined as follows:
choose any node and a direction (right or left); move to the child in that
direction, then alternate directions at each step. The zigzag length is the
number of nodes visited minus 1 (a single node has length 0). Return the longest
ZigZag path contained in that tree.

Example 1:
  Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
  Output: 3

Example 2:
  Input: root = [1,1,1,null,1,null,null,1,1,null,1]
  Output: 4

Constraints:
  The number of nodes is in the range [1, 5 * 10^4].
  1 <= Node.val <= 100

Hints:
  - DFS returning (left-going length, right-going length); flip direction on recurse.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
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
        ([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1], 3),
        ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
        ([1], 0),
    ]
    passed = 0
    for vals, expected in cases:
        try:
            got = s.longestZigZag(build(vals))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
