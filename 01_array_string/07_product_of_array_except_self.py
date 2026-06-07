"""
238. Product of Array Except Self
Difficulty: Medium
Category: Array / String
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i]. The product is
guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in
O(n) time and without using the division operation.

Example 1:
  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]

Example 2:
  Input: nums = [-1,1,0,-3,3]
  Output: [0,0,9,0,0]

Constraints:
  2 <= nums.length <= 10^5
  -30 <= nums[i] <= 30

Hints:
  - Compute prefix products, then sweep right-to-left multiplying suffix products.
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        for i in range(len(nums)):
            if i > 0:
              prefix_product.append(prefix_product[i-1] * nums[i-1])
            else:
                prefix_product.append(1)

        answer = []
        right_pivot = 1
        for i in reversed(range(len(nums))):
            if i == len(nums)-1 :
                answer.append(prefix_product[i])
                right_pivot = right_pivot * nums[-1]
            else:
                answer.append(prefix_product[i] * right_pivot)
                right_pivot = right_pivot * nums[i]

        return answer[::-1]



if __name__ == "__main__":
    s = Solution()
    cases = [
        (([1, 2, 3, 4],), [24, 12, 8, 6]),
        (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0]),
    ]
    passed = 0
    for args, expected in cases:
        try:
            got = s.productExceptSelf(*args)
            ok = got == expected
        except Exception as e:
            got, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "input=" + repr(args), "=> got", repr(got), "| expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
