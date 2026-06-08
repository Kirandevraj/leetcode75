"""
236. Lowest Common Ancestor of a Binary Tree
Difficulty: Medium
Category: Binary Tree - DFS
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p
and q. The LCA is the lowest node that has both p and q as descendants (a node
can be a descendant of itself). All node values are unique and p, q exist in the
tree.

Example 1:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  Output: 3

Example 2:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
  Output: 5

Constraints:
  The number of nodes is in the range [2, 10^5].
  -10^9 <= Node.val <= 10^9, all values unique. p != q, both exist.

Hints:
  - Recurse; if p and q split across left/right subtrees, this node is the LCA.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
    def find(root, val):
        if not root:
            return None
        if root.val == val:
            return root
        return find(root.left, val) or find(root.right, val)
    s = Solution()
    cases = [([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3), ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5)]
    passed = 0
    for vals, pv, qv, expected in cases:
        try:
            root = build(vals)
            node = s.lowestCommonAncestor(root, find(root, pv), find(root, qv))
            got = node.val if node else None
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "p,q=", (pv, qv), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
