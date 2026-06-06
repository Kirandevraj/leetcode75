"""
1431. Kids With the Greatest Number of Candies
Difficulty: Easy
Category: Array / String
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

There are n kids with candies. You are given an integer array candies, where
candies[i] is the number of candies the ith kid has, and an integer
extraCandies. Return a boolean array result of length n, where result[i] is
true if, after giving the ith kid all extraCandies, they will have the greatest
number of candies among all the kids, or false otherwise.

Example 1:
  Input: candies = [2,3,5,1,3], extraCandies = 3
  Output: [true,true,true,false,true]

Constraints:
  n == candies.length
  2 <= n <= 100
  1 <= candies[i] <= 100
  1 <= extraCandies <= 50

Hints:
  - Compare candies[i] + extraCandies against the current maximum.
"""


from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxim = max(candies)
        boolresult = []
        for i in candies:
            if i + extraCandies >= maxim:
                boolresult.append(True)
            else:
                boolresult.append(False)
        return boolresult


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([2, 3, 5, 1, 3], 3), [True, True, True, False, True]),
        (([4, 2, 1, 1, 2], 1), [True, False, False, False, False]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.kidsWithCandies(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(type(e).__name__), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
