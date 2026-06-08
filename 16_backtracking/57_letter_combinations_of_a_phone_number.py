"""
17. Letter Combinations of a Phone Number
Difficulty: Medium
Category: Backtracking
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order. A
mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
  2->abc 3->def 4->ghi 5->jkl 6->mno 7->pqrs 8->tuv 9->wxyz

Example 1:
  Input: digits = "23"
  Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
  Input: digits = ""
  Output: []

Example 3:
  Input: digits = "2"
  Output: ["a","b","c"]

Constraints:
  0 <= digits.length <= 4
  digits[i] is a digit in the range ['2', '9'].

Hints:
  - Backtrack over each digit's letters, building the combination one char at a time.
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass


if __name__ == "__main__":
    s = Solution()
    def _norm(x):
        return sorted((_norm(i) for i in x), key=repr) if isinstance(x, list) else x
    cases = [
        (('23',), ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        (('',), []),
        (('2',), ['a', 'b', 'c']),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.letterCombinations(*args)
            ok = _norm(got) == _norm(expected)
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
