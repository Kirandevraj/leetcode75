"""
199. Binary Tree Right Side View
Difficulty: Medium
Category: Binary Tree - BFS
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of
it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
  Input: root = [1,2,3,null,5,null,4]
  Output: [1,3,4]

Example 2:
  Input: root = [1,null,3]
  Output: [1,3]

Example 3:
  Input: root = []
  Output: []

Constraints:
  The number of nodes is in the range [0, 100].
  -100 <= Node.val <= 100

Hints:
  - BFS level by level; take the last node value of each level.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ]
    passed = 0
    for vals, expected in cases:
        try:
            got = s.rightSideView(build(vals))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
