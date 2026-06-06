"""
1071. Greatest Common Divisor of Strings
Difficulty: Easy
Category: Array / String
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if s = t + t + ...
+ t (t concatenated with itself one or more times). Given two strings str1 and
str2, return the largest string x such that x divides both str1 and str2.

Example 1:
  Input: str1 = "ABCABC", str2 = "ABC"
  Output: "ABC"

Example 2:
  Input: str1 = "ABABAB", str2 = "ABAB"
  Output: "AB"

Example 3:
  Input: str1 = "LEET", str2 = "CODE"
  Output: ""

Constraints:
  1 <= str1.length, str2.length <= 1000
  str1 and str2 consist of English uppercase letters.

Hints:
  - A common divisor exists only if str1 + str2 == str2 + str1.
  - Its length is gcd(len(str1), len(str2)).
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # String with minimum length
        if len(str1) < len(str2):
          minlenstr = str1
          maxlenstr = str2
        else:
            minlenstr = str2
            maxlenstr = str1

        matchedsubstr = ''
        finalmatchedsubstr = ''
        # for i in range(len(minlenstr)):
        i = 0
        for j in range(i+1, len(minlenstr)+1):
            substr = minlenstr[i:j]

            if substr in maxlenstr:
                if len(substr) > len(matchedsubstr):
                  matchedsubstr = substr

                  if (len(minlenstr) % len(matchedsubstr) == 0 ) and ( len(maxlenstr) % len(matchedsubstr) == 0):
                      if ((len(minlenstr) // len(matchedsubstr)) * matchedsubstr == minlenstr) and ((len(maxlenstr) // len(matchedsubstr)) * matchedsubstr == maxlenstr):
                          if len(finalmatchedsubstr) < len(matchedsubstr):
                              finalmatchedsubstr = matchedsubstr
      
        return finalmatchedsubstr


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('ABCABC', 'ABC'), 'ABC'),
        (('ABABAB', 'ABAB'), 'AB'),
        (('LEET', 'CODE'), ''),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.gcdOfStrings(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(type(e).__name__), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
