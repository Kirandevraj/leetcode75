
"""
1657. Determine if Two Strings Are Close
Difficulty: Medium
Category: Hash Map / Set
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using:
(1) swapping any two existing characters' positions, or (2) transforming every
occurrence of one existing character into another existing character, and vice
versa. You can use the operations any number of times. Given two strings word1
and word2, return true if they are close, and false otherwise.

Example 1:
  Input: word1 = "abc", word2 = "bca"
  Output: true

Example 2:
  Input: word1 = "a", word2 = "aa"
  Output: false

Example 3:
  Input: word1 = "cabbba", word2 = "abbccc"
  Output: true

Constraints:
  1 <= word1.length, word2.length <= 10^5
  word1 and word2 contain only lowercase English letters.

Hints:
  - They must use the same set of characters and the same multiset of frequencies.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_dictionary = {}
        for i in word1:
            word1_dictionary[i] = word1_dictionary.get(i, 0) + 1
        word2_dictionary = {}
        for i in word2:
            word2_dictionary[i] = word2_dictionary.get(i, 0) + 1
        
        
        for i in word1_dictionary.keys():
            if i not in word2_dictionary.keys():
                return False
        
        return sorted(word1_dictionary.values()) == sorted(word2_dictionary.values())

if __name__ == "__main__":
    s = Solution()
    cases = [
        (('abc', 'bca'), True),
        (('a', 'aa'), False),
        (('cabbba', 'abbccc'), True),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.closeStrings(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
