"""
649. Dota2 Senate
Difficulty: Medium
Category: Queue
https://leetcode.com/problems/dota2-senate/

In the world of Dota2, there are two parties: the Radiant and the Dire. The
senate consists of senators from both parties, given as a string senate where
'R' is Radiant and 'D' is Dire. In each round, every senator (in order) may ban
one senator from the opposing side from all future rounds. A banned senator
loses all rights. The procedure repeats until one party is exhausted. Return the
party that will finally announce victory: "Radiant" or "Dire".

Example 1:
  Input: senate = "RD"
  Output: "Radiant"

Example 2:
  Input: senate = "RDD"
  Output: "Dire"

Constraints:
  1 <= senate.length <= 10^4
  senate[i] is either 'R' or 'D'.

Hints:
  - Two queues of indices; the smaller index bans first and re-queues at index + n.
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rqueue = []
        dqueue = []
        for pos, i in enumerate(senate):
            if i == 'R':
                rqueue.append(pos)
            elif i == 'D':
                dqueue.append(pos)
        
        pos += 1
        while len(rqueue) != 0 and len(dqueue) != 0:
            rpos = rqueue.pop(0)
            dpos = dqueue.pop(0)

            if rpos < dpos:
                rqueue.append(pos)
            else:
                dqueue.append(pos)
            pos += 1
        if len(rqueue) != 0:
            return 'Radiant'
        else:
            return 'Dire'


if __name__ == "__main__":
    s = Solution()
    cases = [
        (('RD',), 'Radiant'),
        (('RDD',), 'Dire'),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.predictPartyVictory(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
