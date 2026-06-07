"""
1768. Merge Strings Alternately
Difficulty: Easy
Category: Array / String
https://leetcode.com/problems/merge-strings-alternately/

You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer than
the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
  Input: word1 = "abc", word2 = "pqr"
  Output: "apbqcr"

Example 2:
  Input: word1 = "ab", word2 = "pqrs"
  Output: "apbqrs"

Constraints:
  1 <= word1.length, word2.length <= 100
  word1 and word2 consist of lowercase English letters.

Hints:
  - Walk both strings with one index; append from each while it is in range.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = len(word1)
        flag = 1
        if minlen > len(word2):
            minlen = len(word2)
            flag = 2
        final = ''
        for i in range(minlen):
            # print(final, i)
            final += word1[i] + word2[i]
        if flag == 2:
            final += word1[i+1:]
        else:
            final += word2[i+1:]
        return final


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('abc', 'pqr'), 'apbqcr'),
        (('ab', 'pqrs'), 'apbqrs'),
        (('a', 'b'), 'ab'),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.mergeAlternately(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
