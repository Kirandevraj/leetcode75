"""
2336. Smallest Number in Infinite Set
Difficulty: Medium
Category: Heap / Priority Queue
https://leetcode.com/problems/smallest-number-in-infinite-set/

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
  - SmallestInfiniteSet() initializes the set to contain all positive integers.
  - int popSmallest() removes and returns the smallest integer in the set.
  - void addBack(int num) adds num back into the set, if it is not already there.

Example 1:
  Input: ["SmallestInfiniteSet","addBack","popSmallest","popSmallest",
          "popSmallest","addBack","popSmallest","popSmallest","popSmallest"]
         [[],[2],[],[],[],[1],[],[],[]]
  Output: [null,null,1,2,3,null,1,4,5]

Constraints:
  1 <= num <= 1000
  At most 1000 calls total to popSmallest and addBack.

Hints:
  - Track a threshold integer plus a min-heap/set of added-back values below it.
"""


import heapq


class SmallestInfiniteSet:
    def __init__(self):
        pass

    def popSmallest(self) -> int:
        pass

    def addBack(self, num: int) -> None:
        pass


# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    ops = [
        ('addBack', [2], None),
        ('popSmallest', [], 1),
        ('popSmallest', [], 2),
        ('popSmallest', [], 3),
        ('addBack', [1], None),
        ('popSmallest', [], 1),
        ('popSmallest', [], 4),
        ('popSmallest', [], 5),
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
