"""
933. Number of Recent Calls
Difficulty: Easy
Category: Queue
https://leetcode.com/problems/number-of-recent-calls/

You have a RecentCounter class which counts the number of recent requests
within a certain time frame. Implement the RecentCounter class:
  - RecentCounter() initializes the counter with zero recent requests.
  - int ping(int t) adds a new request at time t (in ms), then returns the
    number of requests that happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t.

Example 1:
  Input: ["RecentCounter","ping","ping","ping","ping"]
         [[],[1],[100],[3001],[3002]]
  Output: [null,1,2,3,3]

Constraints:
  1 <= t <= 10^9
  Each test case calls ping with strictly increasing t.
  At most 10^4 calls will be made to ping.

Hints:
  - Keep a queue of timestamps; pop the front while it is < t - 3000.
"""


from collections import deque


class RecentCounter:
    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


if __name__ == "__main__":
    obj = RecentCounter()
    ops = [
        ('ping', [1], 1),
        ('ping', [100], 2),
        ('ping', [3001], 3),
        ('ping', [3002], 3),
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
