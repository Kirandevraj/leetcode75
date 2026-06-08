"""
450. Delete Node in a BST
Difficulty: Medium
Category: Binary Search Tree
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.
Deletion is a two stage process: search for the node, then if found, delete it
while keeping the BST property.

Example 1:
  Input: root = [5,3,6,2,4,null,7], key = 3
  Output: [5,4,6,2,null,null,7]  (one valid answer)

Example 2:
  Input: root = [5,3,6,2,4,null,7], key = 0
  Output: [5,3,6,2,4,null,7]

Constraints:
  The number of nodes is in the range [0, 10^4].
  -10^5 <= Node.val <= 10^5, each value unique. -10^5 <= key <= 10^5

Hints:
  - When the node has two children, replace it with its in-order successor.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
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
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    s = Solution()
    cases = [([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7]), ([5, 3, 6, 2, 4, None, 7], 0, [2, 3, 4, 5, 6, 7])]
    passed = 0
    for vals, key, expected in cases:
        try:
            got = inorder(s.deleteNode(build(vals), key))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "key=", key, "=> inorder", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
