"""
2390. Removing Stars From a String
Difficulty: Medium
Category: Stack
https://leetcode.com/problems/removing-stars-from-a-string/

You are given a string s, which contains stars '*'. In one operation you can
choose a star in s, remove the closest non-star character to its left, and
remove the star itself. Return the string after all stars have been removed. The
input guarantees the operation can always be performed and the result is unique.

Example 1:
  Input: s = "leet**cod*e"
  Output: "lecoe"

Example 2:
  Input: s = "erase*****"
  Output: ""

Constraints:
  1 <= s.length <= 10^5
  s consists of lowercase English letters and stars '*'.
  The operation above can be performed on s.

Hints:
  - Push letters on a stack; pop on each star.
"""


class Solution:
    def removeStars(self, s: str) -> str:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('leet**cod*e',), 'lecoe'),
        (('erase*****',), ''),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.removeStars(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
