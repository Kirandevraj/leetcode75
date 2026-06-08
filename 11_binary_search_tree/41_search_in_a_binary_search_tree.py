"""
700. Search in a Binary Search Tree
Difficulty: Easy
Category: Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val. Find
the node in the BST whose value equals val and return the subtree rooted at that
node. If such a node does not exist, return null.

Example 1:
  Input: root = [4,2,7,1,3], val = 2
  Output: [2,1,3]

Example 2:
  Input: root = [4,2,7,1,3], val = 5
  Output: []

Constraints:
  The number of nodes is in the range [1, 5000].
  1 <= Node.val <= 10^7, root is a valid BST. 1 <= val <= 10^7

Hints:
  - Walk left or right using the BST ordering until you find val or hit null.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
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
    cases = [([4, 2, 7, 1, 3], 2, 2), ([4, 2, 7, 1, 3], 5, None)]
    passed = 0
    for vals, val, expected in cases:
        try:
            res = s.searchBST(build(vals), val)
            got = res.val if res else None
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "val=", val, "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
