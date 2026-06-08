"""
746. Min Cost Climbing Stairs
Difficulty: Easy
Category: DP - 1D
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of the ith step on
a staircase. Once you pay the cost, you can either climb one or two steps. You
can either start from the step with index 0, or the step with index 1. Return the
minimum cost to reach the top of the floor (just past the last index).

Example 1:
  Input: cost = [10,15,20]
  Output: 15

Example 2:
  Input: cost = [1,100,1,1,1,100,1,1,100,1]
  Output: 6

Constraints:
  2 <= cost.length <= 1000
  0 <= cost[i] <= 999

Hints:
  - dp[i] = cost[i] + min(dp[i-1], dp[i-2]); answer is min of the last two.
"""


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([10, 15, 20],), 15),
        (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.minCostClimbingStairs(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
