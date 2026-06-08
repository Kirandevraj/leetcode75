"""
841. Keys and Rooms
Difficulty: Medium
Category: Graphs - DFS
https://leetcode.com/problems/keys-and-rooms/

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
for room 0. Your goal is to visit all the rooms. When you visit a room you may
find a set of distinct keys in it; each key has a number on it denoting which
room it unlocks. Given an array rooms where rooms[i] is the set of keys in room
i, return true if you can visit all the rooms, or false otherwise.

Example 1:
  Input: rooms = [[1],[2],[3],[]]
  Output: true

Example 2:
  Input: rooms = [[1,3],[3,0,1],[2],[0]]
  Output: false

Constraints:
  n == rooms.length, 2 <= n <= 1000
  0 <= rooms[i].length <= 1000, sum of lengths <= 3000
  0 <= rooms[i][j] < n, all values of a room are unique.

Hints:
  - DFS/BFS from room 0, collecting keys; check if every room was visited.
"""


from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([[1], [2], [3], []],), True),
        (([[1, 3], [3, 0, 1], [2], [0]],), False),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.canVisitAllRooms(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
