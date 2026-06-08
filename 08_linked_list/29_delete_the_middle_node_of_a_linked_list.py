"""
2095. Delete the Middle Node of a Linked List
Difficulty: Medium
Category: Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

You are given the head of a linked list. Delete the middle node and return the
head of the modified linked list. The middle node is the floor(n / 2)th node
(0-indexed) where n is the number of nodes. If there is only one node, the list
becomes empty.

Example 1:
  Input: head = [1,3,4,7,1,2,6]
  Output: [1,3,4,1,2,6]

Example 2:
  Input: head = [1,2,3,4]
  Output: [1,2,4]

Example 3:
  Input: head = [2,1]
  Output: [2]

Constraints:
  The number of nodes is in the range [1, 10^5].
  1 <= Node.val <= 10^5

Hints:
  - Slow/fast pointers; keep a pointer to the node before slow to unlink it.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    def build(vals):
        dummy = ListNode()
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out
    s = Solution()
    cases = [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([2, 1], [2]),
        ([1], []),
    ]
    passed = 0
    for inp, expected in cases:
        try:
            got = to_list(s.deleteMiddle(build(inp)))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(inp), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
