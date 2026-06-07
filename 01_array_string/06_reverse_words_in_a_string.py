"""
151. Reverse Words in a String
Difficulty: Medium
Category: Array / String
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words. A word is a maximal
substring of non-space characters. Return a string of the words in reverse
order concatenated by a single space. The input may contain leading/trailing
spaces or multiple spaces between words; the output should have words separated
by a single space with no extra spaces.

Example 1:
  Input: s = "the sky is blue"
  Output: "blue is sky the"

Example 2:
  Input: s = "  hello world  "
  Output: "world hello"

Constraints:
  1 <= s.length <= 10^4
  s contains English letters (upper/lower), digits, and spaces ' '.
  There is at least one word in s.

Hints:
  - Split on whitespace (dropping empties), reverse, join with a single space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        stripped_words = []
        for i in words:
          stripped_words.append(i.strip())
        return " ".join(stripped_words[::-1])


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('the sky is blue',), 'blue is sky the'),
        (('  hello world  ',), 'world hello'),
        (('a good   example',), 'example good a'),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.reverseWords(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
