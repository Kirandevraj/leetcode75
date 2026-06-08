"""
374. Guess Number Higher or Lower
Difficulty: Easy
Category: Binary Search
https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. I pick a number from 1 to n, and you guess. Each
time you guess wrong, I tell you whether the number is higher or lower. You call
a pre-defined API int guess(int num) which returns: -1 if your guess is higher
than the picked number, 1 if lower, and 0 if equal. Return the number that I
picked.

Example 1:
  Input: n = 10, pick = 6
  Output: 6

Constraints:
  1 <= n <= 2^31 - 1
  1 <= pick <= n

Note: The `guess` API is provided by LeetCode at runtime.

Hints:
  - Binary search the range [1, n] using the guess feedback.
"""


# On LeetCode the guess(num) API is provided for you. Below is a local
# mock so this file runs: the test harness sets _pick before each call.
# Returns -1 if num > pick, 1 if num < pick, 0 if equal.
_pick = 0


def guess(num: int) -> int:
    if num > _pick:
        return -1
    if num < _pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [(10, 6), (1, 1), (2126753390, 1702766719)]
    passed = 0
    for n, pick in cases:
        globals()["_pick"] = pick
        try:
            got = s.guessNumber(n)
            ok = got == pick
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "n=", n, "=> got", repr(got), "| expected", repr(pick))
    print("{}/{} passed".format(passed, len(cases)))
