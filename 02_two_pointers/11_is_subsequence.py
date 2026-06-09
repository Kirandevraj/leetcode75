"""
392. Is Subsequence
Difficulty: Easy
Category: Two Pointers
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false
otherwise. A subsequence of a string is a new string formed by deleting some
(possibly zero) characters without disturbing the relative positions of the
remaining characters.

Example 1:
  Input: s = "abc", t = "ahbgdc"
  Output: true

Example 2:
  Input: s = "axc", t = "ahbgdc"
  Output: false

Constraints:
  0 <= s.length <= 100
  0 <= t.length <= 10^4
  s and t consist only of lowercase English letters.

Hints:
  - Advance a pointer in s only when it matches the current char of t.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        
        if i == len(s):
            return True
        return False
                


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('abc', 'ahbgdc'), True),
        (('axc', 'ahbgdc'), False),
        (('', 'abc'), True),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.isSubsequence(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
