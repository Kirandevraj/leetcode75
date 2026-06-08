"""
2130. Maximum Twin Sum of a Linked List
Difficulty: Medium
Category: Linked List
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

In a linked list of size n (n is even), the ith node (0-indexed) is the twin of
the (n-1-i)th node. The twin sum is the sum of a node and its twin. Given the
head of a linked list with an even length, return the maximum twin sum.

Example 1:
  Input: head = [5,4,2,1]
  Output: 6

Example 2:
  Input: head = [4,2,2,3]
  Output: 7

Example 3:
  Input: head = [1,100000]
  Output: 100001

Constraints:
  The number of nodes is an even integer in the range [2, 10^5].
  1 <= Node.val <= 10^5

Hints:
  - Find the middle, reverse the second half, then pair-sum the two halves.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
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
        ([5, 4, 2, 1], 6),
        ([4, 2, 2, 3], 7),
        ([1, 100000], 100001),
    ]
    passed = 0
    for inp, expected in cases:
        try:
            got = s.pairSum(build(inp))
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(inp), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
