"""
1448. Count Good Nodes in Binary Tree
Difficulty: Medium
Category: Binary Tree - DFS
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X. Return the number of
good nodes in the binary tree.

Example 1:
  Input: root = [3,1,4,3,null,1,5]
  Output: 4

Example 2:
  Input: root = [3,3,null,4,2]
  Output: 3

Example 3:
  Input: root = [1]
  Output: 1

Constraints:
  The number of nodes is in the range [1, 10^5].
  Each node's value is between [-10^4, 10^4].

Hints:
  - DFS carrying the max value seen so far on the path; count when node >= max.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
        ([3, 1, 4, 3, None, 1, 5], 4),
        ([3, 3, None, 4, 2], 3),
        ([1], 1),
    ]
    passed = 0
    for vals, expected in cases:
        try:
            got = s.goodNodes(build(vals))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
