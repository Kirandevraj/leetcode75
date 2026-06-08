"""
72. Edit Distance
Difficulty: Medium
Category: DP - Multidimensional
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2. You have the following three operations
permitted on a word: insert a character, delete a character, or replace a
character.

Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3

Example 2:
  Input: word1 = "intention", word2 = "execution"
  Output: 5

Constraints:
  0 <= word1.length, word2.length <= 500
  word1 and word2 consist of lowercase English letters.

Hints:
  - dp[i][j] = matched diagonal, else 1 + min(insert, delete, replace).
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('horse', 'ros'), 3),
        (('intention', 'execution'), 5),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.minDistance(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
