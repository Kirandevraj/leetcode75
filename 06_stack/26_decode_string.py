"""
394. Decode String
Difficulty: Medium
Category: Stack
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string. The encoding rule is
k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. k is guaranteed to be a positive integer. You may
assume the input is always valid; there are no extra white spaces, brackets are
well-formed, etc. The test cases keep output lengths at most 10^5.

Example 1:
  Input: s = "3[a]2[bc]"
  Output: "aaabcbc"

Example 2:
  Input: s = "3[a2[c]]"
  Output: "accaccacc"

Example 3:
  Input: s = "2[abc]3[cd]ef"
  Output: "abcabccdcdcdef"

Constraints:
  1 <= s.length <= 30
  s consists of lowercase English letters, digits, and square brackets.
  s is guaranteed to be a valid input; 1 <= k <= 300.

Hints:
  - Use a stack of (previous string, repeat count); resolve on ']'.
"""


class Solution:
    def decodeString(self, s: str) -> str:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('3[a]2[bc]',), 'aaabcbc'),
        (('3[a2[c]]',), 'accaccacc'),
        (('2[abc]3[cd]ef',), 'abcabccdcdcdef'),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.decodeString(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
