"""
547. Number of Provinces
Difficulty: Medium
Category: Graphs - DFS
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. A province
is a group of directly or indirectly connected cities and no other cities
outside of the group. You are given an n x n matrix isConnected where
isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and 0 otherwise. Return the total number of provinces.

Example 1:
  Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
  Output: 2

Example 2:
  Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
  Output: 3

Constraints:
  1 <= n <= 200
  n == isConnected.length == isConnected[i].length
  isConnected[i][j] is 1 or 0; isConnected[i][i] == 1; symmetric.

Hints:
  - Count connected components via DFS or union-find.
"""


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[1, 1, 0], [1, 1, 0], [0, 0, 1]],), 2),
        (([[1, 0, 0], [0, 1, 0], [0, 0, 1]],), 3),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.findCircleNum(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
