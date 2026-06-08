"""
1268. Search Suggestions System
Difficulty: Medium
Category: Trie
https://leetcode.com/problems/search-suggestions-system/

You are given an array of strings products and a string searchWord. Design a
system that suggests at most three product names from products after each
character of searchWord is typed. Suggested products should have common prefix
with searchWord. If there are more than three products with a common prefix
return the three lexicographically minimums products. Return a list of lists of
the suggested products after each character of searchWord is typed.

Example 1:
  Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
         searchWord = "mouse"
  Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],
           ["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Constraints:
  1 <= products.length <= 1000, 1 <= products[i].length <= 3000
  1 <= sum of products[i].length <= 2 * 10^4
  All products are unique; products[i] and searchWord are lowercase letters.

Hints:
  - Sort products, then binary-search the prefix range, or use a trie.
"""


from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        pass


if __name__ == "__main__":
    s = Solution()
    cases = [
        ((['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'), [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.suggestedProducts(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
