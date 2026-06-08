"""
2462. Total Cost to Hire K Workers
Difficulty: Medium
Category: Heap / Priority Queue
https://leetcode.com/problems/total-cost-to-hire-k-workers/

You are given a 0-indexed integer array costs where costs[i] is the cost of
hiring the ith worker. You are also given two integers k and candidates. You
want to hire exactly k workers according to the following rules: run k hiring
sessions; in each session choose the worker with the lowest cost from either the
first `candidates` workers or the last `candidates` workers (by smallest index
on ties). Return the total cost to hire exactly k workers.

Example 1:
  Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
  Output: 11

Example 2:
  Input: costs = [1,2,4,1], k = 3, candidates = 3
  Output: 4

Constraints:
  1 <= costs.length <= 10^5, 1 <= costs[i] <= 10^5
  1 <= k, candidates <= costs.length

Hints:
  - Two min-heaps for the front and back candidate windows; refill from the middle.
"""


from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4), 11),
        (([1, 2, 4, 1], 3, 3), 4),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.totalCost(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
