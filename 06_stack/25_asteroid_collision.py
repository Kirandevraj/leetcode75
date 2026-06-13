"""
735. Asteroid Collision
Difficulty: Medium
Category: Stack
https://leetcode.com/problems/asteroid-collision/

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign its
direction (positive = right, negative = left). Each asteroid moves at the same
speed. Find out the state after all collisions. Two asteroids moving toward each
other: the smaller explodes; if both are the same size, both explode. Asteroids
moving the same direction never meet.

Example 1:
  Input: asteroids = [5,10,-5]
  Output: [5,10]

Example 2:
  Input: asteroids = [8,-8]
  Output: []

Example 3:
  Input: asteroids = [10,2,-5]
  Output: [10]

Constraints:
  2 <= asteroids.length <= 10^4
  -1000 <= asteroids[i] <= 1000
  asteroids[i] != 0

Hints:
  - Use a stack; a left-moving asteroid resolves collisions against the top.
"""


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        if len(stack) == 0:
                stack.append(asteroids[0])
        for i in range(1, len(asteroids)):
            alive = 1
            while asteroids[i] < 0 and alive == 1 and len(stack) != 0 and stack[-1] > 0:
                if abs(asteroids[i]) < stack[-1]:
                    alive = 0
                elif abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    alive = 0
            
            if alive:
                stack.append(asteroids[i])
        return stack
            


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([5, 10, -5],), [5, 10]),
        (([8, -8],), []),
        (([10, 2, -5],), [10]),
        (([-2, -1, 1, 2],), [-2, -1, 1, 2]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.asteroidCollision(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
