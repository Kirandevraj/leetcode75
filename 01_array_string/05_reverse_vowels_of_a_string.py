"""
345. Reverse Vowels of a String
Difficulty: Easy
Category: Array / String
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it. The
vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper
cases, more than once.

Example 1:
  Input: s = "IceCreAm"
  Output: "AceCreIm"

Example 2:
  Input: s = "leetcode"
  Output: "leotcede"

Constraints:
  1 <= s.length <= 3 * 10^5
  s consists of printable ASCII characters.

Hints:
  - Two pointers from both ends; swap when both point at vowels.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        # first solution
        vowels = 'aeiouAEIOU'
        # pos1 = 0
        # pos2 = len(s)
        s = list(s)
        # for i in range(pos1, len(s)):
        #     if pos2 < pos1:
        #         break
        #     if s[i] in vowels:
        #         pos1 = i
        #         for j in reversed(range(i, pos2)):
        #             if s[j] in vowels and i != j and i < j:
        #                 # print(s)
        #                 s[i], s[j] = s[j], s[i]
        #                 # print(s)
        #                 pos2 = j
        #                 break

        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] not in vowels:
                lo += 1
            elif s[hi] not in vowels:
                hi -= 1
            else:
                s[lo], s[hi] = s[hi], s[lo]
                lo += 1
                hi -= 1
        return "".join(s)

if __name__ == "__main__":
    s = Solution()
    cases = [
        (('IceCreAm',), 'AceCreIm'),
        (('leetcode',), 'leotcede'),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.reverseVowels(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(e), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
