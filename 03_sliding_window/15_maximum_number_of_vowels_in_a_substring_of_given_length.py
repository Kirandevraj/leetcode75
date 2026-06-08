"""
1456. Maximum Number of Vowels in a Substring of Given Length
Difficulty: Medium
Category: Sliding Window
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k. Vowel letters are 'a', 'e', 'i', 'o', 'u'.

Example 1:
  Input: s = "abciiidef", k = 3
  Output: 3

Example 2:
  Input: s = "aeiou", k = 2
  Output: 2

Constraints:
  1 <= s.length <= 10^5
  s consists of lowercase English letters.
  1 <= k <= s.length

Hints:
  - Slide a window of size k, updating the vowel count as chars enter/leave.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('abciiidef', 3), 3),
        (('aeiou', 2), 2),
        (('leetcode', 3), 2),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.maxVowels(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
