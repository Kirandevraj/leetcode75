"""
872. Leaf-Similar Trees
Difficulty: Easy
Category: Binary Tree - DFS
https://leetcode.com/problems/leaf-similar-trees/

Consider all the leaves of a binary tree, from left to right; the values of
those leaves form a leaf value sequence. Two binary trees are considered
leaf-similar if their leaf value sequences are the same. Given the roots of two
binary trees root1 and root2, return true if they are leaf-similar.

Example 1:
  Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
         root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
  Output: true

Constraints:
  The number of nodes in each tree is in the range [1, 200].
  Both trees have values in the range [0, 200].

Hints:
  - DFS collecting leaves left-to-right for each tree, then compare sequences.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
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
        ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True),
        ([1, 2, 3], [1, 3, 2], False),
        ([1], [1], True),
    ]
    passed = 0
    for a, b, expected in cases:
        try:
            got = s.leafSimilar(build(a), build(b))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
