"""
1143. Longest Common Subsequence
Difficulty: Medium
Category: DP - Multidimensional
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0. A subsequence of a
string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining
characters. A common subsequence of two strings is a subsequence that is common
to both strings.

Example 1:
  Input: text1 = "abcde", text2 = "ace"
  Output: 3

Example 2:
  Input: text1 = "abc", text2 = "abc"
  Output: 3

Example 3:
  Input: text1 = "abc", text2 = "def"
  Output: 0

Constraints:
  1 <= text1.length, text2.length <= 1000
  text1 and text2 consist of only lowercase English characters.

Hints:
  - Classic 2D DP: match -> diagonal + 1, else max of left/up.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('abcde', 'ace'), 3),
        (('abc', 'abc'), 3),
        (('abc', 'def'), 0),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.longestCommonSubsequence(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
