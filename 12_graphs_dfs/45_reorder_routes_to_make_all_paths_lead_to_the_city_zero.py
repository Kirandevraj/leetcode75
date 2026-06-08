"""
1466. Reorder Routes to Make All Paths Lead to the City Zero
Difficulty: Medium
Category: Graphs - DFS
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
only one way to travel between two different cities (this forms a tree). Roads
are represented by connections where connections[i] = [a, b] is a directed road
from city a to city b. This year there will be a big event in city 0. Return the
minimum number of edges that need to be reversed so that each city can reach
city 0.

Example 1:
  Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
  Output: 3

Example 2:
  Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
  Output: 2

Constraints:
  2 <= n <= 5 * 10^4
  connections.length == n - 1
  connections[i].length == 2, 0 <= a, b <= n - 1, a != b

Hints:
  - Build an undirected graph tagging original direction; DFS from 0 and count edges pointing away.
"""


from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3),
        ((5, [[1, 0], [1, 2], [3, 2], [3, 4]]), 2),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.minReorder(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
