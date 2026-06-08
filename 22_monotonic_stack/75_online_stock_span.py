"""
901. Online Stock Span
Difficulty: Medium
Category: Monotonic Stack
https://leetcode.com/problems/online-stock-span/

Design an algorithm that collects daily price quotes for some stock and returns
the span of that stock's price for the current day. The span of the stock's
price in one day is the maximum number of consecutive days (starting from that
day and going backward) for which the stock price was less than or equal to the
price of that day. Implement the StockSpanner class:
  - StockSpanner() initializes the object of the class.
  - int next(int price) returns the span of the stock's price given that today's
    price is price.

Example 1:
  Input: ["StockSpanner","next","next","next","next","next","next","next"]
         [[],[100],[80],[60],[70],[60],[75],[85]]
  Output: [null,1,1,1,2,1,4,6]

Constraints:
  1 <= price <= 10^5
  At most 10^4 calls will be made to next.

Hints:
  - Monotonic stack of (price, span); collapse smaller-or-equal prices into the span.
"""


class StockSpanner:
    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


# obj = StockSpanner()
# param_1 = obj.next(price)


if __name__ == "__main__":
    obj = StockSpanner()
    ops = [
        ('next', [100], 1),
        ('next', [80], 1),
        ('next', [60], 1),
        ('next', [70], 2),
        ('next', [60], 1),
        ('next', [75], 4),
        ('next', [85], 6),
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
