"""
399. Evaluate Division
Difficulty: Medium
Category: Graphs - DFS
https://leetcode.com/problems/evaluate-division/

You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent Ai / Bi = values[i].
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query: find the value of Cj / Dj. Return the answers to all queries. If a single
answer cannot be determined, return -1.0. The inputs are always valid; no
division by zero and no contradiction.

Example 1:
  Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
         queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
  Output: [6.0,0.5,-1.0,1.0,-1.0]

Constraints:
  1 <= equations.length <= 20, 1 <= queries.length <= 20
  Variable names are 1-5 lowercase letters; values in (0, 20].

Hints:
  - Model as a weighted graph; the query answer is the product of edge ratios on a path.
"""


from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], [6.0, 0.5, -1.0, 1.0, -1.0]),
    ]
    passed = 0
    for eq, vals, q, expected in cases:
        try:
            got = s.calcEquation(eq, vals, q)
            ok = len(got) == len(expected) and all(abs(x - y) < 1e-5 for x, y in zip(got, expected))
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
