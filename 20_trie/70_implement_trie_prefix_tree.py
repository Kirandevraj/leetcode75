"""
208. Implement Trie (Prefix Tree)
Difficulty: Medium
Category: Trie
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. Implement the Trie
class:
  - Trie() initializes the trie object.
  - void insert(String word) inserts the string word into the trie.
  - boolean search(String word) returns true if word is in the trie.
  - boolean startsWith(String prefix) returns true if there is a previously
    inserted string word that has the prefix.

Example 1:
  Input: ["Trie","insert","search","search","startsWith","insert","search"]
         [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
  Output: [null,null,true,false,true,null,true]

Constraints:
  1 <= word.length, prefix.length <= 2000
  word and prefix consist only of lowercase English letters.
  At most 3 * 10^4 calls in total to insert, search, and startsWith.

Hints:
  - Each node holds child links and an end-of-word flag.
"""


class Trie:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    obj = Trie()
    ops = [
        ('insert', ['apple'], None),
        ('search', ['apple'], True),
        ('search', ['app'], False),
        ('startsWith', ['app'], True),
        ('insert', ['app'], None),
        ('search', ['app'], True),
    ]
    passed = total = 0
    for name, a, expected in ops:
        try:
            got = getattr(obj, name)(*a)
        except Exception as e:
            got = "<error: {}>".format(repr(e))
        if expected is None:
            print("CALL ", name + repr(tuple(a)), "=>", repr(got))
            continue
        total += 1
        ok = got == expected
        passed += ok
        print(("PASS" if ok else "FAIL"), name + repr(tuple(a)), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, total))
