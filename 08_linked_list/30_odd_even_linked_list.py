"""
328. Odd Even Linked List
Difficulty: Medium
Category: Linked List
https://leetcode.com/problems/odd-even-linked-list/

Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, the second even, and so on. Preserve the
relative order inside both the odd and even groups. Solve in O(1) extra space
and O(n) time.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [1,3,5,2,4]

Example 2:
  Input: head = [2,1,3,5,6,4,7]
  Output: [2,3,6,7,1,5,4]

Constraints:
  The number of nodes is in the range [0, 10^4].
  -10^6 <= Node.val <= 10^6

Hints:
  - Weave two chains (odd and even) then connect odd's tail to the even head.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
    ]
    passed = 0
    for inp, expected in cases:
        try:
            got = to_list(s.oddEvenList(build(inp)))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(inp), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
