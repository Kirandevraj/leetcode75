"""
1207. Unique Number of Occurrences
Difficulty: Easy
Category: Hash Map / Set
https://leetcode.com/problems/unique-number-of-occurrences/

Given an array of integers arr, return true if the number of occurrences of
each value in the array is unique, or false otherwise.

Example 1:
  Input: arr = [1,2,2,1,1,3]
  Output: true

Example 2:
  Input: arr = [1,2]
  Output: false

Constraints:
  1 <= arr.length <= 1000
  -1000 <= arr[i] <= 1000

Hints:
  - Count occurrences, then check the counts themselves are all distinct.
"""


from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
        if len(set(counts.values())) == len(counts.values()):
            return True
        else:
            return False
            


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 2, 2, 1, 1, 3],), True),
        (([1, 2],), False),
        (([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],), True),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.uniqueOccurrences(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
