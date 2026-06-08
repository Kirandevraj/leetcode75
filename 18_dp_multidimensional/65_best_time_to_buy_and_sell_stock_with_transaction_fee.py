"""
714. Best Time to Buy and Sell Stock with Transaction Fee
Difficulty: Medium
Category: DP - Multidimensional
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

You are given an array prices where prices[i] is the price of a given stock on
the ith day, and an integer fee representing a transaction fee. Find the maximum
profit you can achieve. You may complete as many transactions as you like, but
you need to pay the transaction fee for each transaction. Note: You may not
engage in multiple transactions simultaneously (you must sell before you buy
again).

Example 1:
  Input: prices = [1,3,2,8,4,9], fee = 2
  Output: 8

Example 2:
  Input: prices = [1,3,7,5,10,3], fee = 3
  Output: 6

Constraints:
  1 <= prices.length <= 5 * 10^4
  1 <= prices[i] < 5 * 10^4, 0 <= fee < 5 * 10^4

Hints:
  - Track two states: max cash holding no stock vs. holding stock.
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 3, 2, 8, 4, 9], 2), 8),
        (([1, 3, 7, 5, 10, 3], 3), 6),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.maxProfit(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
