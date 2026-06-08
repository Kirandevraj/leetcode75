"""
216. Combination Sum III
Difficulty: Medium
Category: Backtracking
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the
following conditions are true: only numbers 1 through 9 are used, and each number
is used at most once. Return a list of all possible valid combinations. The list
must not contain the same combination twice, and the combinations may be returned
in any order.

Example 1:
  Input: k = 3, n = 7
  Output: [[1,2,4]]

Example 2:
  Input: k = 3, n = 9
  Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
  Input: k = 4, n = 1
  Output: []

Constraints:
  2 <= k <= 9
  1 <= n <= 60

Hints:
  - Backtrack choosing increasing digits; prune when sum or count exceeds the target.
"""


from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()
    def _norm(x):
        return sorted((_norm(i) for i in x), key=repr) if isinstance(x, list) else x
    cases = [
        ((3, 7), [[1, 2, 4]]),
        ((3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        ((4, 1), []),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.combinationSum3(*args)
            ok = _norm(got) == _norm(expected)
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
