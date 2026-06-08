#!/usr/bin/env python3
"""Generate the LeetCode 75 study scaffold.

Creates one folder per category and one Python file per problem. Each file holds
the full problem statement (paraphrased), examples, constraints, hints and a
solution stub you can fill in. Also (re)writes README.md with a progress tracker.

Re-running is safe: by default existing solution files are NOT overwritten, so
your work is preserved. Pass --force to regenerate everything.
"""
from __future__ import annotations

import argparse
import os
import re
import textwrap

ROOT = os.path.dirname(os.path.abspath(__file__))

# Reusable node definitions injected into linked-list / tree problems.
# Real classes (not comments) so the files run standalone for testing. On
# LeetCode these are provided for you.
LISTNODE = """# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next"""

TREENODE = """# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right"""

# Each problem: (num, slug, title, difficulty, body, stub)
# `body` is the human-readable problem text. `stub` is the code skeleton.
CATEGORIES = [
    ("01_array_string", "Array / String", [
        (1768, "merge-strings-alternately", "Merge Strings Alternately", "Easy",
         """You are given two strings word1 and word2. Merge the strings by adding
letters in alternating order, starting with word1. If a string is longer than
the other, append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:
  Input: word1 = "abc", word2 = "pqr"
  Output: "apbqcr"

Example 2:
  Input: word1 = "ab", word2 = "pqrs"
  Output: "apbqrs"

Constraints:
  1 <= word1.length, word2.length <= 100
  word1 and word2 consist of lowercase English letters.

Hints:
  - Walk both strings with one index; append from each while it is in range.""",
         "class Solution:\n    def mergeAlternately(self, word1: str, word2: str) -> str:\n        pass"),

        (1071, "greatest-common-divisor-of-strings", "Greatest Common Divisor of Strings", "Easy",
         """For two strings s and t, we say "t divides s" if and only if s = t + t + ...
+ t (t concatenated with itself one or more times). Given two strings str1 and
str2, return the largest string x such that x divides both str1 and str2.

Example 1:
  Input: str1 = "ABCABC", str2 = "ABC"
  Output: "ABC"

Example 2:
  Input: str1 = "ABABAB", str2 = "ABAB"
  Output: "AB"

Example 3:
  Input: str1 = "LEET", str2 = "CODE"
  Output: ""

Constraints:
  1 <= str1.length, str2.length <= 1000
  str1 and str2 consist of English uppercase letters.

Hints:
  - A common divisor exists only if str1 + str2 == str2 + str1.
  - Its length is gcd(len(str1), len(str2)).""",
         "class Solution:\n    def gcdOfStrings(self, str1: str, str2: str) -> str:\n        pass"),

        (1431, "kids-with-the-greatest-number-of-candies", "Kids With the Greatest Number of Candies", "Easy",
         """There are n kids with candies. You are given an integer array candies, where
candies[i] is the number of candies the ith kid has, and an integer
extraCandies. Return a boolean array result of length n, where result[i] is
true if, after giving the ith kid all extraCandies, they will have the greatest
number of candies among all the kids, or false otherwise.

Example 1:
  Input: candies = [2,3,5,1,3], extraCandies = 3
  Output: [true,true,true,false,true]

Constraints:
  n == candies.length
  2 <= n <= 100
  1 <= candies[i] <= 100
  1 <= extraCandies <= 50

Hints:
  - Compare candies[i] + extraCandies against the current maximum.""",
         "from typing import List\n\n\nclass Solution:\n    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:\n        pass"),

        (605, "can-place-flowers", "Can Place Flowers", "Easy",
         """You have a long flowerbed in which some plots are planted and some are not.
Flowers cannot be planted in adjacent plots. Given an integer array flowerbed
containing 0's (empty) and 1's (planted) and an integer n, return true if n new
flowers can be planted without violating the no-adjacent-flowers rule.

Example 1:
  Input: flowerbed = [1,0,0,0,1], n = 1
  Output: true

Example 2:
  Input: flowerbed = [1,0,0,0,1], n = 2
  Output: false

Constraints:
  1 <= flowerbed.length <= 2 * 10^4
  flowerbed[i] is 0 or 1.
  There are no two adjacent flowers in flowerbed.
  0 <= n <= flowerbed.length

Hints:
  - Greedily plant when a plot and both neighbors are empty (treat out-of-bounds as empty).""",
         "from typing import List\n\n\nclass Solution:\n    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:\n        pass"),

        (345, "reverse-vowels-of-a-string", "Reverse Vowels of a String", "Easy",
         """Given a string s, reverse only all the vowels in the string and return it. The
vowels are 'a', 'e', 'i', 'o', 'u', and they can appear in both lower and upper
cases, more than once.

Example 1:
  Input: s = "IceCreAm"
  Output: "AceCreIm"

Example 2:
  Input: s = "leetcode"
  Output: "leotcede"

Constraints:
  1 <= s.length <= 3 * 10^5
  s consists of printable ASCII characters.

Hints:
  - Two pointers from both ends; swap when both point at vowels.""",
         "class Solution:\n    def reverseVowels(self, s: str) -> str:\n        pass"),

        (151, "reverse-words-in-a-string", "Reverse Words in a String", "Medium",
         """Given an input string s, reverse the order of the words. A word is a maximal
substring of non-space characters. Return a string of the words in reverse
order concatenated by a single space. The input may contain leading/trailing
spaces or multiple spaces between words; the output should have words separated
by a single space with no extra spaces.

Example 1:
  Input: s = "the sky is blue"
  Output: "blue is sky the"

Example 2:
  Input: s = "  hello world  "
  Output: "world hello"

Constraints:
  1 <= s.length <= 10^4
  s contains English letters (upper/lower), digits, and spaces ' '.
  There is at least one word in s.

Hints:
  - Split on whitespace (dropping empties), reverse, join with a single space.""",
         "class Solution:\n    def reverseWords(self, s: str) -> str:\n        pass"),

        (238, "product-of-array-except-self", "Product of Array Except Self", "Medium",
         """Given an integer array nums, return an array answer such that answer[i] is
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
  - Compute prefix products, then sweep right-to-left multiplying suffix products.""",
         "from typing import List\n\n\nclass Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        pass"),

        (334, "increasing-triplet-subsequence", "Increasing Triplet Subsequence", "Medium",
         """Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exist, return false.

Example 1:
  Input: nums = [1,2,3,4,5]
  Output: true

Example 2:
  Input: nums = [5,4,3,2,1]
  Output: false

Example 3:
  Input: nums = [2,1,5,0,4,6]
  Output: true (triplet (3,4,5) -> 0,4,6)

Constraints:
  1 <= nums.length <= 5 * 10^5
  -2^31 <= nums[i] <= 2^31 - 1

Hints:
  - Track the smallest and second-smallest seen so far; a third larger value wins.""",
         "from typing import List\n\n\nclass Solution:\n    def increasingTriplet(self, nums: List[int]) -> bool:\n        pass"),

        (443, "string-compression", "String Compression", "Medium",
         """Given an array of characters chars, compress it in place. For each group of
consecutive repeating characters: if the group length is 1, append the
character; otherwise append the character followed by the group length. Return
the new length of the array. You must use only constant extra space.

Example 1:
  Input: chars = ["a","a","b","b","c","c","c"]
  Output: 6, and chars becomes ["a","2","b","2","c","3"]

Example 2:
  Input: chars = ["a"]
  Output: 1, chars = ["a"]

Constraints:
  1 <= chars.length <= 2000
  chars[i] is a lowercase/uppercase letter, digit, or symbol.

Hints:
  - Use a read pointer to count runs and a write pointer to emit the result.""",
         "from typing import List\n\n\nclass Solution:\n    def compress(self, chars: List[str]) -> int:\n        pass"),
    ]),

    ("02_two_pointers", "Two Pointers", [
        (283, "move-zeroes", "Move Zeroes", "Easy",
         """Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements. You must do this in place without
making a copy of the array.

Example 1:
  Input: nums = [0,1,0,3,12]
  Output: [1,3,12,0,0]

Constraints:
  1 <= nums.length <= 10^4
  -2^31 <= nums[i] <= 2^31 - 1

Hints:
  - Keep a write index for the next non-zero slot; swap non-zeros forward.""",
         "from typing import List\n\n\nclass Solution:\n    def moveZeroes(self, nums: List[int]) -> None:\n        \"\"\"Do not return anything, modify nums in-place instead.\"\"\"\n        pass"),

        (392, "is-subsequence", "Is Subsequence", "Easy",
         """Given two strings s and t, return true if s is a subsequence of t, or false
otherwise. A subsequence of a string is a new string formed by deleting some
(possibly zero) characters without disturbing the relative positions of the
remaining characters.

Example 1:
  Input: s = "abc", t = "ahbgdc"
  Output: true

Example 2:
  Input: s = "axc", t = "ahbgdc"
  Output: false

Constraints:
  0 <= s.length <= 100
  0 <= t.length <= 10^4
  s and t consist only of lowercase English letters.

Hints:
  - Advance a pointer in s only when it matches the current char of t.""",
         "class Solution:\n    def isSubsequence(self, s: str, t: str) -> bool:\n        pass"),

        (11, "container-with-most-water", "Container With Most Water", "Medium",
         """You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the
container holds the most water. Return the maximum amount of water it can store.

Example 1:
  Input: height = [1,8,6,2,5,4,8,3,7]
  Output: 49

Constraints:
  n == height.length
  2 <= n <= 10^5
  0 <= height[i] <= 10^4

Hints:
  - Two pointers at the ends; always move the shorter wall inward.""",
         "from typing import List\n\n\nclass Solution:\n    def maxArea(self, height: List[int]) -> int:\n        pass"),

        (1679, "max-number-of-k-sum-pairs", "Max Number of K-Sum Pairs", "Medium",
         """You are given an integer array nums and an integer k. In one operation, you can
pick two numbers from the array whose sum equals k and remove them. Return the
maximum number of operations you can perform on the array.

Example 1:
  Input: nums = [1,2,3,4], k = 5
  Output: 2

Example 2:
  Input: nums = [3,1,3,4,3], k = 6
  Output: 1

Constraints:
  1 <= nums.length <= 10^5
  1 <= nums[i] <= 10^9
  1 <= k <= 10^9

Hints:
  - Sort and use two pointers, or count complements with a hash map.""",
         "from typing import List\n\n\nclass Solution:\n    def maxOperations(self, nums: List[int], k: int) -> int:\n        pass"),
    ]),

    ("03_sliding_window", "Sliding Window", [
        (643, "maximum-average-subarray-i", "Maximum Average Subarray I", "Easy",
         """You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer within 10^-5 of the actual
answer will be accepted.

Example 1:
  Input: nums = [1,12,-5,-6,50,3], k = 4
  Output: 12.75

Constraints:
  n == nums.length
  1 <= k <= n <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
  - Maintain a running window sum of size k; track its maximum.""",
         "from typing import List\n\n\nclass Solution:\n    def findMaxAverage(self, nums: List[int], k: int) -> float:\n        pass"),

        (1456, "maximum-number-of-vowels-in-a-substring-of-given-length",
         "Maximum Number of Vowels in a Substring of Given Length", "Medium",
         """Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k. Vowel letters are 'a', 'e', 'i', 'o', 'u'.

Example 1:
  Input: s = "abciiidef", k = 3
  Output: 3

Example 2:
  Input: s = "aeiou", k = 2
  Output: 2

Constraints:
  1 <= s.length <= 10^5
  s consists of lowercase English letters.
  1 <= k <= s.length

Hints:
  - Slide a window of size k, updating the vowel count as chars enter/leave.""",
         "class Solution:\n    def maxVowels(self, s: str, k: int) -> int:\n        pass"),

        (1004, "max-consecutive-ones-iii", "Max Consecutive Ones III", "Medium",
         """Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
  Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
  Output: 6

Example 2:
  Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
  Output: 10

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is 0 or 1.
  0 <= k <= nums.length

Hints:
  - Grow a window while it contains at most k zeros; shrink from the left otherwise.""",
         "from typing import List\n\n\nclass Solution:\n    def longestOnes(self, nums: List[int], k: int) -> int:\n        pass"),

        (1493, "longest-subarray-of-1s-after-deleting-one-element",
         "Longest Subarray of 1's After Deleting One Element", "Medium",
         """Given a binary array nums, you should delete one element from it. Return the
size of the longest non-empty subarray containing only 1's in the resulting
array. Return 0 if there is no such subarray.

Example 1:
  Input: nums = [1,1,0,1]
  Output: 3

Example 2:
  Input: nums = [0,1,1,1,0,1,1,0,1]
  Output: 5

Example 3:
  Input: nums = [1,1,1]
  Output: 2

Constraints:
  1 <= nums.length <= 10^5
  nums[i] is either 0 or 1.

Hints:
  - Sliding window allowing at most one zero; answer is window length minus one.""",
         "from typing import List\n\n\nclass Solution:\n    def longestSubarray(self, nums: List[int]) -> int:\n        pass"),
    ]),

    ("04_prefix_sum", "Prefix Sum", [
        (1732, "find-the-highest-altitude", "Find the Highest Altitude", "Easy",
         """There is a biker going on a road trip consisting of n + 1 points at different
altitudes. The biker starts at point 0 with altitude 0. You are given an integer
array gain of length n where gain[i] is the net gain in altitude between points
i and i + 1. Return the highest altitude of a point.

Example 1:
  Input: gain = [-5,1,5,0,-7]
  Output: 1

Example 2:
  Input: gain = [-4,-3,-2,-1,4,3,2]
  Output: 0

Constraints:
  n == gain.length
  1 <= n <= 100
  -100 <= gain[i] <= 100

Hints:
  - Track a running prefix sum and its maximum (starting at 0).""",
         "from typing import List\n\n\nclass Solution:\n    def largestAltitude(self, gain: List[int]) -> int:\n        pass"),

        (724, "find-pivot-index", "Find Pivot Index", "Easy",
         """Given an array of integers nums, calculate the pivot index. The pivot index is
where the sum of all numbers strictly to the left equals the sum of all numbers
strictly to the right. If the index is on the left edge, the left sum is 0.
Return the leftmost pivot index, or -1 if none exists.

Example 1:
  Input: nums = [1,7,3,6,5,6]
  Output: 3

Example 2:
  Input: nums = [1,2,3]
  Output: -1

Example 3:
  Input: nums = [2,1,-1]
  Output: 0

Constraints:
  1 <= nums.length <= 10^4
  -1000 <= nums[i] <= 1000

Hints:
  - For each i, left_sum and total give the right sum: total - left - nums[i].""",
         "from typing import List\n\n\nclass Solution:\n    def pivotIndex(self, nums: List[int]) -> int:\n        pass"),
    ]),

    ("05_hashmap_set", "Hash Map / Set", [
        (2215, "find-the-difference-of-two-arrays", "Find the Difference of Two Arrays", "Easy",
         """Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
size 2 where: answer[0] is a list of all distinct integers in nums1 not present
in nums2, and answer[1] is a list of all distinct integers in nums2 not present
in nums1. The integers in each list may be returned in any order.

Example 1:
  Input: nums1 = [1,2,3], nums2 = [2,4,6]
  Output: [[1,3],[4,6]]

Constraints:
  1 <= nums1.length, nums2.length <= 1000
  -1000 <= nums1[i], nums2[i] <= 1000

Hints:
  - Convert to sets and take set differences in both directions.""",
         "from typing import List\n\n\nclass Solution:\n    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:\n        pass"),

        (1207, "unique-number-of-occurrences", "Unique Number of Occurrences", "Easy",
         """Given an array of integers arr, return true if the number of occurrences of
each value in the array is unique, or false otherwise.

Example 1:
  Input: arr = [1,2,2,1,1,3]
  Output: true

Example 2:
  Input: arr = [1,2]
  Output: false

Constraints:
  1 <= arr.length <= 1000
  -1000 <= arr[i] <= 1000

Hints:
  - Count occurrences, then check the counts themselves are all distinct.""",
         "from typing import List\n\n\nclass Solution:\n    def uniqueOccurrences(self, arr: List[int]) -> bool:\n        pass"),

        (1657, "determine-if-two-strings-are-close", "Determine if Two Strings Are Close", "Medium",
         """Two strings are considered close if you can attain one from the other using:
(1) swapping any two existing characters' positions, or (2) transforming every
occurrence of one existing character into another existing character, and vice
versa. You can use the operations any number of times. Given two strings word1
and word2, return true if they are close, and false otherwise.

Example 1:
  Input: word1 = "abc", word2 = "bca"
  Output: true

Example 2:
  Input: word1 = "a", word2 = "aa"
  Output: false

Example 3:
  Input: word1 = "cabbba", word2 = "abbccc"
  Output: true

Constraints:
  1 <= word1.length, word2.length <= 10^5
  word1 and word2 contain only lowercase English letters.

Hints:
  - They must use the same set of characters and the same multiset of frequencies.""",
         "class Solution:\n    def closeStrings(self, word1: str, word2: str) -> bool:\n        pass"),

        (2352, "equal-row-and-column-pairs", "Equal Row and Column Pairs", "Medium",
         """Given a 0-indexed n x n integer matrix grid, return the number of pairs
(ri, cj) such that row ri and column cj are equal. A row and column pair is
considered equal if they contain the same elements in the same order.

Example 1:
  Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
  Output: 1

Example 2:
  Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
  Output: 3

Constraints:
  n == grid.length == grid[i].length
  1 <= n <= 200
  1 <= grid[i][j] <= 10^5

Hints:
  - Hash each row tuple; for each column tuple, count matching rows.""",
         "from typing import List\n\n\nclass Solution:\n    def equalPairs(self, grid: List[List[int]]) -> int:\n        pass"),
    ]),

    ("06_stack", "Stack", [
        (2390, "removing-stars-from-a-string", "Removing Stars From a String", "Medium",
         """You are given a string s, which contains stars '*'. In one operation you can
choose a star in s, remove the closest non-star character to its left, and
remove the star itself. Return the string after all stars have been removed. The
input guarantees the operation can always be performed and the result is unique.

Example 1:
  Input: s = "leet**cod*e"
  Output: "lecoe"

Example 2:
  Input: s = "erase*****"
  Output: ""

Constraints:
  1 <= s.length <= 10^5
  s consists of lowercase English letters and stars '*'.
  The operation above can be performed on s.

Hints:
  - Push letters on a stack; pop on each star.""",
         "class Solution:\n    def removeStars(self, s: str) -> str:\n        pass"),

        (735, "asteroid-collision", "Asteroid Collision", "Medium",
         """We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign its
direction (positive = right, negative = left). Each asteroid moves at the same
speed. Find out the state after all collisions. Two asteroids moving toward each
other: the smaller explodes; if both are the same size, both explode. Asteroids
moving the same direction never meet.

Example 1:
  Input: asteroids = [5,10,-5]
  Output: [5,10]

Example 2:
  Input: asteroids = [8,-8]
  Output: []

Example 3:
  Input: asteroids = [10,2,-5]
  Output: [10]

Constraints:
  2 <= asteroids.length <= 10^4
  -1000 <= asteroids[i] <= 1000
  asteroids[i] != 0

Hints:
  - Use a stack; a left-moving asteroid resolves collisions against the top.""",
         "from typing import List\n\n\nclass Solution:\n    def asteroidCollision(self, asteroids: List[int]) -> List[int]:\n        pass"),

        (394, "decode-string", "Decode String", "Medium",
         """Given an encoded string, return its decoded string. The encoding rule is
k[encoded_string], where the encoded_string inside the square brackets is being
repeated exactly k times. k is guaranteed to be a positive integer. You may
assume the input is always valid; there are no extra white spaces, brackets are
well-formed, etc. The test cases keep output lengths at most 10^5.

Example 1:
  Input: s = "3[a]2[bc]"
  Output: "aaabcbc"

Example 2:
  Input: s = "3[a2[c]]"
  Output: "accaccacc"

Example 3:
  Input: s = "2[abc]3[cd]ef"
  Output: "abcabccdcdcdef"

Constraints:
  1 <= s.length <= 30
  s consists of lowercase English letters, digits, and square brackets.
  s is guaranteed to be a valid input; 1 <= k <= 300.

Hints:
  - Use a stack of (previous string, repeat count); resolve on ']'.""",
         "class Solution:\n    def decodeString(self, s: str) -> str:\n        pass"),
    ]),

    ("07_queue", "Queue", [
        (933, "number-of-recent-calls", "Number of Recent Calls", "Easy",
         """You have a RecentCounter class which counts the number of recent requests
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
  - Keep a queue of timestamps; pop the front while it is < t - 3000.""",
         "from collections import deque\n\n\nclass RecentCounter:\n    def __init__(self):\n        pass\n\n    def ping(self, t: int) -> int:\n        pass\n\n\n# Your RecentCounter object will be instantiated and called as such:\n# obj = RecentCounter()\n# param_1 = obj.ping(t)"),

        (649, "dota2-senate", "Dota2 Senate", "Medium",
         """In the world of Dota2, there are two parties: the Radiant and the Dire. The
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
  - Two queues of indices; the smaller index bans first and re-queues at index + n.""",
         "class Solution:\n    def predictPartyVictory(self, senate: str) -> str:\n        pass"),
    ]),

    ("08_linked_list", "Linked List", [
        (2095, "delete-the-middle-node-of-a-linked-list", "Delete the Middle Node of a Linked List", "Medium",
         """You are given the head of a linked list. Delete the middle node and return the
head of the modified linked list. The middle node is the floor(n / 2)th node
(0-indexed) where n is the number of nodes. If there is only one node, the list
becomes empty.

Example 1:
  Input: head = [1,3,4,7,1,2,6]
  Output: [1,3,4,1,2,6]

Example 2:
  Input: head = [1,2,3,4]
  Output: [1,2,4]

Example 3:
  Input: head = [2,1]
  Output: [2]

Constraints:
  The number of nodes is in the range [1, 10^5].
  1 <= Node.val <= 10^5

Hints:
  - Slow/fast pointers; keep a pointer to the node before slow to unlink it.""",
         LISTNODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass"),

        (328, "odd-even-linked-list", "Odd Even Linked List", "Medium",
         """Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, the second even, and so on. Preserve the
relative order inside both the odd and even groups. Solve in O(1) extra space
and O(n) time.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [1,3,5,2,4]

Example 2:
  Input: head = [2,1,3,5,6,4,7]
  Output: [2,3,6,7,1,5,4]

Constraints:
  The number of nodes is in the range [0, 10^4].
  -10^6 <= Node.val <= 10^6

Hints:
  - Weave two chains (odd and even) then connect odd's tail to the even head.""",
         LISTNODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass"),

        (206, "reverse-linked-list", "Reverse Linked List", "Easy",
         """Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

Example 2:
  Input: head = [1,2]
  Output: [2,1]

Constraints:
  The number of nodes is in the range [0, 5000].
  -5000 <= Node.val <= 5000

Hints:
  - Iteratively flip each next pointer, tracking the previous node.""",
         LISTNODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        pass"),

        (2130, "maximum-twin-sum-of-a-linked-list", "Maximum Twin Sum of a Linked List", "Medium",
         """In a linked list of size n (n is even), the ith node (0-indexed) is the twin of
the (n-1-i)th node. The twin sum is the sum of a node and its twin. Given the
head of a linked list with an even length, return the maximum twin sum.

Example 1:
  Input: head = [5,4,2,1]
  Output: 6

Example 2:
  Input: head = [4,2,2,3]
  Output: 7

Example 3:
  Input: head = [1,100000]
  Output: 100001

Constraints:
  The number of nodes is an even integer in the range [2, 10^5].
  1 <= Node.val <= 10^5

Hints:
  - Find the middle, reverse the second half, then pair-sum the two halves.""",
         LISTNODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def pairSum(self, head: Optional[ListNode]) -> int:\n        pass"),
    ]),

    ("09_binary_tree_dfs", "Binary Tree - DFS", [
        (104, "maximum-depth-of-binary-tree", "Maximum Depth of Binary Tree", "Easy",
         """Given the root of a binary tree, return its maximum depth. A binary tree's
maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3

Example 2:
  Input: root = [1,null,2]
  Output: 2

Constraints:
  The number of nodes is in the range [0, 10^4].
  -100 <= Node.val <= 100

Hints:
  - depth(node) = 1 + max(depth(left), depth(right)).""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def maxDepth(self, root: Optional[TreeNode]) -> int:\n        pass"),

        (872, "leaf-similar-trees", "Leaf-Similar Trees", "Easy",
         """Consider all the leaves of a binary tree, from left to right; the values of
those leaves form a leaf value sequence. Two binary trees are considered
leaf-similar if their leaf value sequences are the same. Given the roots of two
binary trees root1 and root2, return true if they are leaf-similar.

Example 1:
  Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
         root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
  Output: true

Constraints:
  The number of nodes in each tree is in the range [1, 200].
  Both trees have values in the range [0, 200].

Hints:
  - DFS collecting leaves left-to-right for each tree, then compare sequences.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:\n        pass"),

        (1448, "count-good-nodes-in-binary-tree", "Count Good Nodes in Binary Tree", "Medium",
         """Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X. Return the number of
good nodes in the binary tree.

Example 1:
  Input: root = [3,1,4,3,null,1,5]
  Output: 4

Example 2:
  Input: root = [3,3,null,4,2]
  Output: 3

Example 3:
  Input: root = [1]
  Output: 1

Constraints:
  The number of nodes is in the range [1, 10^5].
  Each node's value is between [-10^4, 10^4].

Hints:
  - DFS carrying the max value seen so far on the path; count when node >= max.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def goodNodes(self, root: TreeNode) -> int:\n        pass"),

        (437, "path-sum-iii", "Path Sum III", "Medium",
         """Given the root of a binary tree and an integer targetSum, return the number of
paths where the sum of the values along the path equals targetSum. The path does
not need to start or end at the root or a leaf, but it must go downwards (i.e.,
travelling only from parent nodes to child nodes).

Example 1:
  Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
  Output: 3

Example 2:
  Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
  Output: 3

Constraints:
  The number of nodes is in the range [0, 1000].
  -10^9 <= Node.val <= 10^9
  -1000 <= targetSum <= 1000

Hints:
  - DFS with a running prefix sum and a hash map of prefix-sum counts.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:\n        pass"),

        (1372, "longest-zigzag-path-in-a-binary-tree", "Longest ZigZag Path in a Binary Tree", "Medium",
         """You are given the root of a binary tree. A ZigZag path is defined as follows:
choose any node and a direction (right or left); move to the child in that
direction, then alternate directions at each step. The zigzag length is the
number of nodes visited minus 1 (a single node has length 0). Return the longest
ZigZag path contained in that tree.

Example 1:
  Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
  Output: 3

Example 2:
  Input: root = [1,1,1,null,1,null,null,1,1,null,1]
  Output: 4

Constraints:
  The number of nodes is in the range [1, 5 * 10^4].
  1 <= Node.val <= 100

Hints:
  - DFS returning (left-going length, right-going length); flip direction on recurse.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def longestZigZag(self, root: Optional[TreeNode]) -> int:\n        pass"),

        (236, "lowest-common-ancestor-of-a-binary-tree", "Lowest Common Ancestor of a Binary Tree", "Medium",
         """Given a binary tree, find the lowest common ancestor (LCA) of two given nodes p
and q. The LCA is the lowest node that has both p and q as descendants (a node
can be a descendant of itself). All node values are unique and p, q exist in the
tree.

Example 1:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  Output: 3

Example 2:
  Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
  Output: 5

Constraints:
  The number of nodes is in the range [2, 10^5].
  -10^9 <= Node.val <= 10^9, all values unique. p != q, both exist.

Hints:
  - Recurse; if p and q split across left/right subtrees, this node is the LCA.""",
         TREENODE + "\n\n\nclass Solution:\n    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':\n        pass"),
    ]),

    ("10_binary_tree_bfs", "Binary Tree - BFS", [
        (199, "binary-tree-right-side-view", "Binary Tree Right Side View", "Medium",
         """Given the root of a binary tree, imagine yourself standing on the right side of
it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
  Input: root = [1,2,3,null,5,null,4]
  Output: [1,3,4]

Example 2:
  Input: root = [1,null,3]
  Output: [1,3]

Example 3:
  Input: root = []
  Output: []

Constraints:
  The number of nodes is in the range [0, 100].
  -100 <= Node.val <= 100

Hints:
  - BFS level by level; take the last node value of each level.""",
         TREENODE + "\n\n\nfrom typing import List, Optional\n\n\nclass Solution:\n    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:\n        pass"),

        (1161, "maximum-level-sum-of-a-binary-tree", "Maximum Level Sum of a Binary Tree", "Medium",
         """Given the root of a binary tree, the level of its root is 1, the level of its
children is 2, and so on. Return the smallest level x such that the sum of all
the values of nodes at level x is maximal.

Example 1:
  Input: root = [1,7,0,7,-8,null,null]
  Output: 2

Example 2:
  Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
  Output: 2

Constraints:
  The number of nodes is in the range [1, 10^4].
  -10^5 <= Node.val <= 10^5

Hints:
  - BFS by level summing values; remember the level of the maximum sum.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def maxLevelSum(self, root: Optional[TreeNode]) -> int:\n        pass"),
    ]),

    ("11_binary_search_tree", "Binary Search Tree", [
        (700, "search-in-a-binary-search-tree", "Search in a Binary Search Tree", "Easy",
         """You are given the root of a binary search tree (BST) and an integer val. Find
the node in the BST whose value equals val and return the subtree rooted at that
node. If such a node does not exist, return null.

Example 1:
  Input: root = [4,2,7,1,3], val = 2
  Output: [2,1,3]

Example 2:
  Input: root = [4,2,7,1,3], val = 5
  Output: []

Constraints:
  The number of nodes is in the range [1, 5000].
  1 <= Node.val <= 10^7, root is a valid BST. 1 <= val <= 10^7

Hints:
  - Walk left or right using the BST ordering until you find val or hit null.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:\n        pass"),

        (450, "delete-node-in-a-bst", "Delete Node in a BST", "Medium",
         """Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.
Deletion is a two stage process: search for the node, then if found, delete it
while keeping the BST property.

Example 1:
  Input: root = [5,3,6,2,4,null,7], key = 3
  Output: [5,4,6,2,null,null,7]  (one valid answer)

Example 2:
  Input: root = [5,3,6,2,4,null,7], key = 0
  Output: [5,3,6,2,4,null,7]

Constraints:
  The number of nodes is in the range [0, 10^4].
  -10^5 <= Node.val <= 10^5, each value unique. -10^5 <= key <= 10^5

Hints:
  - When the node has two children, replace it with its in-order successor.""",
         TREENODE + "\n\n\nfrom typing import Optional\n\n\nclass Solution:\n    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:\n        pass"),
    ]),

    ("12_graphs_dfs", "Graphs - DFS", [
        (841, "keys-and-rooms", "Keys and Rooms", "Medium",
         """There are n rooms labeled from 0 to n - 1 and all the rooms are locked except
for room 0. Your goal is to visit all the rooms. When you visit a room you may
find a set of distinct keys in it; each key has a number on it denoting which
room it unlocks. Given an array rooms where rooms[i] is the set of keys in room
i, return true if you can visit all the rooms, or false otherwise.

Example 1:
  Input: rooms = [[1],[2],[3],[]]
  Output: true

Example 2:
  Input: rooms = [[1,3],[3,0,1],[2],[0]]
  Output: false

Constraints:
  n == rooms.length, 2 <= n <= 1000
  0 <= rooms[i].length <= 1000, sum of lengths <= 3000
  0 <= rooms[i][j] < n, all values of a room are unique.

Hints:
  - DFS/BFS from room 0, collecting keys; check if every room was visited.""",
         "from typing import List\n\n\nclass Solution:\n    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:\n        pass"),

        (547, "number-of-provinces", "Number of Provinces", "Medium",
         """There are n cities. Some of them are connected, while some are not. A province
is a group of directly or indirectly connected cities and no other cities
outside of the group. You are given an n x n matrix isConnected where
isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and 0 otherwise. Return the total number of provinces.

Example 1:
  Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
  Output: 2

Example 2:
  Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
  Output: 3

Constraints:
  1 <= n <= 200
  n == isConnected.length == isConnected[i].length
  isConnected[i][j] is 1 or 0; isConnected[i][i] == 1; symmetric.

Hints:
  - Count connected components via DFS or union-find.""",
         "from typing import List\n\n\nclass Solution:\n    def findCircleNum(self, isConnected: List[List[int]]) -> int:\n        pass"),

        (1466, "reorder-routes-to-make-all-paths-lead-to-the-city-zero",
         "Reorder Routes to Make All Paths Lead to the City Zero", "Medium",
         """There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is
only one way to travel between two different cities (this forms a tree). Roads
are represented by connections where connections[i] = [a, b] is a directed road
from city a to city b. This year there will be a big event in city 0. Return the
minimum number of edges that need to be reversed so that each city can reach
city 0.

Example 1:
  Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
  Output: 3

Example 2:
  Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
  Output: 2

Constraints:
  2 <= n <= 5 * 10^4
  connections.length == n - 1
  connections[i].length == 2, 0 <= a, b <= n - 1, a != b

Hints:
  - Build an undirected graph tagging original direction; DFS from 0 and count edges pointing away.""",
         "from typing import List\n\n\nclass Solution:\n    def minReorder(self, n: int, connections: List[List[int]]) -> int:\n        pass"),

        (399, "evaluate-division", "Evaluate Division", "Medium",
         """You are given an array of variable pairs equations and an array of real numbers
values, where equations[i] = [Ai, Bi] and values[i] represent Ai / Bi = values[i].
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
query: find the value of Cj / Dj. Return the answers to all queries. If a single
answer cannot be determined, return -1.0. The inputs are always valid; no
division by zero and no contradiction.

Example 1:
  Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
         queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
  Output: [6.0,0.5,-1.0,1.0,-1.0]

Constraints:
  1 <= equations.length <= 20, 1 <= queries.length <= 20
  Variable names are 1-5 lowercase letters; values in (0, 20].

Hints:
  - Model as a weighted graph; the query answer is the product of edge ratios on a path.""",
         "from typing import List\n\n\nclass Solution:\n    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:\n        pass"),
    ]),

    ("13_graphs_bfs", "Graphs - BFS", [
        (1926, "nearest-exit-from-entrance-in-maze", "Nearest Exit from Entrance in Maze", "Medium",
         """You are given an m x n matrix maze (0-indexed) with empty cells (represented as
'.') and walls (represented as '+'). You are also given the entrance, where
entrance = [row, col]. In one step you can move one cell up, down, left or right.
You cannot step into a wall or outside the maze. Your goal is to find the nearest
exit: an empty cell at the border of the maze that is not the entrance. Return
the number of steps to the nearest exit, or -1 if none exists.

Example 1:
  Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
         entrance = [1,2]
  Output: 1

Example 2:
  Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
  Output: 2

Constraints:
  maze.length == m, maze[i].length == n, 1 <= m, n <= 100
  Each cell is '.' or '+'; entrance is an empty cell.

Hints:
  - BFS from the entrance; the first border empty cell reached is the answer.""",
         "from typing import List\n\n\nclass Solution:\n    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:\n        pass"),

        (994, "rotting-oranges", "Rotting Oranges", "Medium",
         """You are given an m x n grid where each cell can have one of three values: 0 (an
empty cell), 1 (a fresh orange), or 2 (a rotten orange). Every minute, any fresh
orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return
the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
  Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
  Output: 4

Example 2:
  Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
  Output: -1

Example 3:
  Input: grid = [[0,2]]
  Output: 0

Constraints:
  m == grid.length, n == grid[i].length, 1 <= m, n <= 10
  grid[i][j] is 0, 1, or 2.

Hints:
  - Multi-source BFS starting from all rotten oranges; track elapsed minutes.""",
         "from typing import List\n\n\nclass Solution:\n    def orangesRotting(self, grid: List[List[int]]) -> int:\n        pass"),
    ]),

    ("14_heap_priority_queue", "Heap / Priority Queue", [
        (215, "kth-largest-element-in-an-array", "Kth Largest Element in an Array", "Medium",
         """Given an integer array nums and an integer k, return the kth largest element in
the array. Note that it is the kth largest element in the sorted order, not the
kth distinct element. Can you solve it without sorting?

Example 1:
  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5

Example 2:
  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
  Output: 4

Constraints:
  1 <= k <= nums.length <= 10^5
  -10^4 <= nums[i] <= 10^4

Hints:
  - Maintain a min-heap of size k, or use quickselect for O(n) average.""",
         "from typing import List\n\n\nclass Solution:\n    def findKthLargest(self, nums: List[int], k: int) -> int:\n        pass"),

        (2336, "smallest-number-in-infinite-set", "Smallest Number in Infinite Set", "Medium",
         """You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
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
  - Track a threshold integer plus a min-heap/set of added-back values below it.""",
         "import heapq\n\n\nclass SmallestInfiniteSet:\n    def __init__(self):\n        pass\n\n    def popSmallest(self) -> int:\n        pass\n\n    def addBack(self, num: int) -> None:\n        pass\n\n\n# obj = SmallestInfiniteSet()\n# param_1 = obj.popSmallest()\n# obj.addBack(num)"),

        (2542, "maximum-subsequence-score", "Maximum Subsequence Score", "Medium",
         """You are given two 0-indexed integer arrays nums1 and nums2 of equal length n
and a positive integer k. You must choose a subsequence of indices from [0, n-1]
of length k. For chosen indices, your score is defined as: (sum of the selected
elements from nums1) multiplied by (the minimum of the selected elements from
nums2). Return the maximum possible score.

Example 1:
  Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
  Output: 12

Example 2:
  Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
  Output: 30

Constraints:
  n == nums1.length == nums2.length, 1 <= n <= 10^5
  0 <= nums1[i], nums2[j] <= 10^5, 1 <= k <= n

Hints:
  - Sort by nums2 descending; keep a min-heap of the k largest nums1 values.""",
         "from typing import List\n\n\nclass Solution:\n    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:\n        pass"),

        (2462, "total-cost-to-hire-k-workers", "Total Cost to Hire K Workers", "Medium",
         """You are given a 0-indexed integer array costs where costs[i] is the cost of
hiring the ith worker. You are also given two integers k and candidates. You
want to hire exactly k workers according to the following rules: run k hiring
sessions; in each session choose the worker with the lowest cost from either the
first `candidates` workers or the last `candidates` workers (by smallest index
on ties). Return the total cost to hire exactly k workers.

Example 1:
  Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
  Output: 11

Example 2:
  Input: costs = [1,2,4,1], k = 3, candidates = 3
  Output: 4

Constraints:
  1 <= costs.length <= 10^5, 1 <= costs[i] <= 10^5
  1 <= k, candidates <= costs.length

Hints:
  - Two min-heaps for the front and back candidate windows; refill from the middle.""",
         "from typing import List\n\n\nclass Solution:\n    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:\n        pass"),
    ]),

    ("15_binary_search", "Binary Search", [
        (374, "guess-number-higher-or-lower", "Guess Number Higher or Lower", "Easy",
         """We are playing the Guess Game. I pick a number from 1 to n, and you guess. Each
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
  - Binary search the range [1, n] using the guess feedback.""",
         "# On LeetCode the guess(num) API is provided for you. Below is a local\n# mock so this file runs: the test harness sets _pick before each call.\n# Returns -1 if num > pick, 1 if num < pick, 0 if equal.\n_pick = 0\n\n\ndef guess(num: int) -> int:\n    if num > _pick:\n        return -1\n    if num < _pick:\n        return 1\n    return 0\n\n\nclass Solution:\n    def guessNumber(self, n: int) -> int:\n        pass"),

        (2300, "successful-pairs-of-spells-and-potions", "Successful Pairs of Spells and Potions", "Medium",
         """You are given two positive integer arrays spells and potions, of length n and m
respectively, where spells[i] represents the strength of the ith spell and
potions[j] represents the strength of the jth potion. You are also given an
integer success. A spell and potion pair is considered successful if the product
of their strengths is at least success. Return an integer array pairs of length
n where pairs[i] is the number of potions that will form a successful pair with
the ith spell.

Example 1:
  Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
  Output: [4,0,3]

Example 2:
  Input: spells = [3,1,2], potions = [8,5,8], success = 16
  Output: [2,0,2]

Constraints:
  n == spells.length, m == potions.length, 1 <= n, m <= 10^5
  1 <= spells[i], potions[i] <= 10^5, 1 <= success <= 10^10

Hints:
  - Sort potions; for each spell binary-search the minimum qualifying potion.""",
         "from typing import List\n\n\nclass Solution:\n    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:\n        pass"),

        (162, "find-peak-element", "Find Peak Element", "Medium",
         """A peak element is an element that is strictly greater than its neighbors. Given
a 0-indexed integer array nums, find a peak element, and return its index. If
the array contains multiple peaks, return the index to any of the peaks. You may
imagine that nums[-1] = nums[n] = -infinity. You must write an algorithm that
runs in O(log n) time.

Example 1:
  Input: nums = [1,2,3,1]
  Output: 2

Example 2:
  Input: nums = [1,2,1,3,5,6,4]
  Output: 5 (or 1)

Constraints:
  1 <= nums.length <= 1000
  -2^31 <= nums[i] <= 2^31 - 1
  nums[i] != nums[i + 1] for all valid i.

Hints:
  - Binary search: move toward the larger neighbor; you always climb to a peak.""",
         "from typing import List\n\n\nclass Solution:\n    def findPeakElement(self, nums: List[int]) -> int:\n        pass"),

        (875, "koko-eating-bananas", "Koko Eating Bananas", "Medium",
         """Koko loves to eat bananas. There are n piles of bananas, the ith pile has
piles[i] bananas. The guards have gone and will come back in h hours. Koko
decides her bananas-per-hour eating speed k. Each hour, she chooses a pile and
eats k bananas from it. If the pile has fewer than k bananas, she eats all of
them and will not eat any more during this hour. Return the minimum integer k
such that she can eat all the bananas within h hours.

Example 1:
  Input: piles = [3,6,7,11], h = 8
  Output: 4

Example 2:
  Input: piles = [30,11,23,4,20], h = 5
  Output: 30

Example 3:
  Input: piles = [30,11,23,4,20], h = 6
  Output: 23

Constraints:
  1 <= piles.length <= 10^4, piles.length <= h <= 10^9
  1 <= piles[i] <= 10^9

Hints:
  - Binary search speed k in [1, max(piles)]; hours = sum(ceil(p / k)).""",
         "from typing import List\n\n\nclass Solution:\n    def minEatingSpeed(self, piles: List[int], h: int) -> int:\n        pass"),
    ]),

    ("16_backtracking", "Backtracking", [
        (17, "letter-combinations-of-a-phone-number", "Letter Combinations of a Phone Number", "Medium",
         """Given a string containing digits from 2-9 inclusive, return all possible letter
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
  - Backtrack over each digit's letters, building the combination one char at a time.""",
         "from typing import List\n\n\nclass Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        pass"),

        (216, "combination-sum-iii", "Combination Sum III", "Medium",
         """Find all valid combinations of k numbers that sum up to n such that the
following conditions are true: only numbers 1 through 9 are used, and each number
is used at most once. Return a list of all possible valid combinations. The list
must not contain the same combination twice, and the combinations may be returned
in any order.

Example 1:
  Input: k = 3, n = 7
  Output: [[1,2,4]]

Example 2:
  Input: k = 3, n = 9
  Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
  Input: k = 4, n = 1
  Output: []

Constraints:
  2 <= k <= 9
  1 <= n <= 60

Hints:
  - Backtrack choosing increasing digits; prune when sum or count exceeds the target.""",
         "from typing import List\n\n\nclass Solution:\n    def combinationSum3(self, k: int, n: int) -> List[List[int]]:\n        pass"),
    ]),

    ("17_dp_1d", "DP - 1D", [
        (1137, "n-th-tribonacci-number", "N-th Tribonacci Number", "Easy",
         """The Tribonacci sequence Tn is defined as follows: T0 = 0, T1 = 1, T2 = 1, and
Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. Given n, return the value of Tn.

Example 1:
  Input: n = 4
  Output: 4

Example 2:
  Input: n = 25
  Output: 1389537

Constraints:
  0 <= n <= 37
  The answer is guaranteed to fit within a 32-bit integer.

Hints:
  - Roll three variables forward; no need for a full DP array.""",
         "class Solution:\n    def tribonacci(self, n: int) -> int:\n        pass"),

        (746, "min-cost-climbing-stairs", "Min Cost Climbing Stairs", "Easy",
         """You are given an integer array cost where cost[i] is the cost of the ith step on
a staircase. Once you pay the cost, you can either climb one or two steps. You
can either start from the step with index 0, or the step with index 1. Return the
minimum cost to reach the top of the floor (just past the last index).

Example 1:
  Input: cost = [10,15,20]
  Output: 15

Example 2:
  Input: cost = [1,100,1,1,1,100,1,1,100,1]
  Output: 6

Constraints:
  2 <= cost.length <= 1000
  0 <= cost[i] <= 999

Hints:
  - dp[i] = cost[i] + min(dp[i-1], dp[i-2]); answer is min of the last two.""",
         "from typing import List\n\n\nclass Solution:\n    def minCostClimbingStairs(self, cost: List[int]) -> int:\n        pass"),

        (198, "house-robber", "House Robber", "Medium",
         """You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night. Given an integer array nums representing the amount of money
of each house, return the maximum amount of money you can rob tonight without
alerting the police.

Example 1:
  Input: nums = [1,2,3,1]
  Output: 4

Example 2:
  Input: nums = [2,7,9,3,1]
  Output: 12

Constraints:
  1 <= nums.length <= 100
  0 <= nums[i] <= 400

Hints:
  - dp[i] = max(dp[i-1], dp[i-2] + nums[i]); track two rolling values.""",
         "from typing import List\n\n\nclass Solution:\n    def rob(self, nums: List[int]) -> int:\n        pass"),

        (790, "domino-and-tromino-tiling", "Domino and Tromino Tiling", "Medium",
         """You have two types of tiles: a 2 x 1 domino shape and a tromino shape (an
L-shape covering three cells). You may rotate these shapes. Given an integer n,
return the number of ways to tile a 2 x n board. Since the answer may be very
large, return it modulo 10^9 + 7. Two tilings are different if and only if there
are two 4-directionally adjacent cells on the board such that exactly one of the
tilings has both cells covered by the same tile.

Example 1:
  Input: n = 3
  Output: 5

Example 2:
  Input: n = 1
  Output: 1

Constraints:
  1 <= n <= 1000

Hints:
  - Recurrence: f(n) = 2*f(n-1) + f(n-3), all modulo 1e9+7.""",
         "class Solution:\n    def numTilings(self, n: int) -> int:\n        pass"),
    ]),

    ("18_dp_multidimensional", "DP - Multidimensional", [
        (62, "unique-paths", "Unique Paths", "Medium",
         """There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at
any point in time. Given the two integers m and n, return the number of possible
unique paths that the robot can take to reach the bottom-right corner.

Example 1:
  Input: m = 3, n = 7
  Output: 28

Example 2:
  Input: m = 3, n = 2
  Output: 3

Constraints:
  1 <= m, n <= 100

Hints:
  - dp[i][j] = dp[i-1][j] + dp[i][j-1]; a single row suffices for O(n) space.""",
         "class Solution:\n    def uniquePaths(self, m: int, n: int) -> int:\n        pass"),

        (1143, "longest-common-subsequence", "Longest Common Subsequence", "Medium",
         """Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0. A subsequence of a
string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining
characters. A common subsequence of two strings is a subsequence that is common
to both strings.

Example 1:
  Input: text1 = "abcde", text2 = "ace"
  Output: 3

Example 2:
  Input: text1 = "abc", text2 = "abc"
  Output: 3

Example 3:
  Input: text1 = "abc", text2 = "def"
  Output: 0

Constraints:
  1 <= text1.length, text2.length <= 1000
  text1 and text2 consist of only lowercase English characters.

Hints:
  - Classic 2D DP: match -> diagonal + 1, else max of left/up.""",
         "class Solution:\n    def longestCommonSubsequence(self, text1: str, text2: str) -> int:\n        pass"),

        (714, "best-time-to-buy-and-sell-stock-with-transaction-fee",
         "Best Time to Buy and Sell Stock with Transaction Fee", "Medium",
         """You are given an array prices where prices[i] is the price of a given stock on
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
  - Track two states: max cash holding no stock vs. holding stock.""",
         "from typing import List\n\n\nclass Solution:\n    def maxProfit(self, prices: List[int], fee: int) -> int:\n        pass"),

        (72, "edit-distance", "Edit Distance", "Medium",
         """Given two strings word1 and word2, return the minimum number of operations
required to convert word1 to word2. You have the following three operations
permitted on a word: insert a character, delete a character, or replace a
character.

Example 1:
  Input: word1 = "horse", word2 = "ros"
  Output: 3

Example 2:
  Input: word1 = "intention", word2 = "execution"
  Output: 5

Constraints:
  0 <= word1.length, word2.length <= 500
  word1 and word2 consist of lowercase English letters.

Hints:
  - dp[i][j] = matched diagonal, else 1 + min(insert, delete, replace).""",
         "class Solution:\n    def minDistance(self, word1: str, word2: str) -> int:\n        pass"),
    ]),

    ("19_bit_manipulation", "Bit Manipulation", [
        (338, "counting-bits", "Counting Bits", "Easy",
         """Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
  Input: n = 2
  Output: [0,1,1]

Example 2:
  Input: n = 5
  Output: [0,1,1,2,1,2]

Constraints:
  0 <= n <= 10^5

Hints:
  - ans[i] = ans[i >> 1] + (i & 1).""",
         "from typing import List\n\n\nclass Solution:\n    def countBits(self, n: int) -> List[int]:\n        pass"),

        (136, "single-number", "Single Number", "Easy",
         """Given a non-empty array of integers nums, every element appears twice except for
one. Find that single one. You must implement a solution with a linear runtime
complexity and use only constant extra space.

Example 1:
  Input: nums = [2,2,1]
  Output: 1

Example 2:
  Input: nums = [4,1,2,1,2]
  Output: 4

Example 3:
  Input: nums = [1]
  Output: 1

Constraints:
  1 <= nums.length <= 3 * 10^4
  -3 * 10^4 <= nums[i] <= 3 * 10^4
  Each element appears twice except for one which appears once.

Hints:
  - XOR all numbers; pairs cancel, leaving the unique value.""",
         "from typing import List\n\n\nclass Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        pass"),

        (1318, "minimum-flips-to-make-a-or-b-equal-to-c", "Minimum Flips to Make a OR b Equal to c", "Medium",
         """Given 3 positive numbers a, b and c. Return the minimum flips required in some
bits of a and b to make ( a OR b == c ). (bitwise OR operation). A flip
operation consists of changing any single bit 1 to 0 or changing any single bit
0 to 1 in their binary representation.

Example 1:
  Input: a = 2, b = 6, c = 5
  Output: 3

Example 2:
  Input: a = 4, b = 2, c = 7
  Output: 1

Example 3:
  Input: a = 1, b = 2, c = 3
  Output: 0

Constraints:
  1 <= a, b, c <= 10^9

Hints:
  - For each bit: if c-bit is 0, flip every set bit in a and b; if 1, flip if both are 0.""",
         "class Solution:\n    def minFlips(self, a: int, b: int, c: int) -> int:\n        pass"),
    ]),

    ("20_trie", "Trie", [
        (208, "implement-trie-prefix-tree", "Implement Trie (Prefix Tree)", "Medium",
         """A trie (pronounced as "try") or prefix tree is a tree data structure used to
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
  - Each node holds child links and an end-of-word flag.""",
         "class Trie:\n    def __init__(self):\n        pass\n\n    def insert(self, word: str) -> None:\n        pass\n\n    def search(self, word: str) -> bool:\n        pass\n\n    def startsWith(self, prefix: str) -> bool:\n        pass\n\n\n# obj = Trie()\n# obj.insert(word)\n# param_2 = obj.search(word)\n# param_3 = obj.startsWith(prefix)"),

        (1268, "search-suggestions-system", "Search Suggestions System", "Medium",
         """You are given an array of strings products and a string searchWord. Design a
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
  - Sort products, then binary-search the prefix range, or use a trie.""",
         "from typing import List\n\n\nclass Solution:\n    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:\n        pass"),
    ]),

    ("21_intervals", "Intervals", [
        (435, "non-overlapping-intervals", "Non-overlapping Intervals", "Medium",
         """Given an array of intervals where intervals[i] = [starti, endi], return the
minimum number of intervals you need to remove to make the rest of the intervals
non-overlapping. Note that intervals which only touch at a point are
non-overlapping.

Example 1:
  Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
  Output: 1

Example 2:
  Input: intervals = [[1,2],[1,2],[1,2]]
  Output: 2

Example 3:
  Input: intervals = [[1,2],[2,3]]
  Output: 0

Constraints:
  1 <= intervals.length <= 10^5
  intervals[i].length == 2
  -5 * 10^4 <= starti < endi <= 5 * 10^4

Hints:
  - Greedy: sort by end, keep intervals that start at or after the last kept end.""",
         "from typing import List\n\n\nclass Solution:\n    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:\n        pass"),

        (452, "minimum-number-of-arrows-to-burst-balloons", "Minimum Number of Arrows to Burst Balloons", "Medium",
         """There are some spherical balloons taped onto a flat wall. The balloons are
given as an array points where points[i] = [xstart, xend] denotes a balloon
whose horizontal diameter stretches between xstart and xend. An arrow shot
vertically at x bursts a balloon if xstart <= x <= xend. Return the minimum
number of arrows that must be shot to burst all balloons.

Example 1:
  Input: points = [[10,16],[2,8],[1,6],[7,12]]
  Output: 2

Example 2:
  Input: points = [[1,2],[3,4],[5,6],[7,8]]
  Output: 4

Example 3:
  Input: points = [[1,2],[2,3],[3,4],[4,5]]
  Output: 2

Constraints:
  1 <= points.length <= 10^5
  points[i].length == 2, -2^31 <= xstart < xend <= 2^31 - 1

Hints:
  - Sort by end; shoot at each end, skipping balloons that overlap the current arrow.""",
         "from typing import List\n\n\nclass Solution:\n    def findMinArrowShots(self, points: List[List[int]]) -> int:\n        pass"),
    ]),

    ("22_monotonic_stack", "Monotonic Stack", [
        (739, "daily-temperatures", "Daily Temperatures", "Medium",
         """Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. If there is no future day for
which this is possible, keep answer[i] == 0 instead.

Example 1:
  Input: temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]

Example 2:
  Input: temperatures = [30,40,50,60]
  Output: [1,1,1,0]

Example 3:
  Input: temperatures = [30,60,90]
  Output: [1,1,0]

Constraints:
  1 <= temperatures.length <= 10^5
  30 <= temperatures[i] <= 100

Hints:
  - Keep a decreasing stack of indices; resolve waits when a warmer day arrives.""",
         "from typing import List\n\n\nclass Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        pass"),

        (901, "online-stock-span", "Online Stock Span", "Medium",
         """Design an algorithm that collects daily price quotes for some stock and returns
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
  - Monotonic stack of (price, span); collapse smaller-or-equal prices into the span.""",
         "class StockSpanner:\n    def __init__(self):\n        pass\n\n    def next(self, price: int) -> int:\n        pass\n\n\n# obj = StockSpanner()\n# param_1 = obj.next(price)"),
    ]),
]


# ---------------------------------------------------------------------------
# Test-block generators. Each returns the full `if __name__ == "__main__":`
# block (as source text) appended to a problem file. Every per-case run is
# wrapped in try/except so an unfinished stub prints FAIL instead of crashing.
# ---------------------------------------------------------------------------

_RUN_FOOTER = [
    '        passed += ok',
    '        print(("PASS" if ok else "FAIL"), "input=" + repr(args),'
    ' "=> got", repr(got), "| expected", repr(expected))',
    '    print("{}/{} passed".format(passed, len(cases)))',
]

TREE_BUILDER = [
    '    def build(vals):',
    '        if not vals:',
    '            return None',
    '        nodes = [None if v is None else TreeNode(v) for v in vals]',
    '        kids = nodes[1:][::-1]',
    '        for node in nodes:',
    '            if node:',
    '                if kids:',
    '                    node.left = kids.pop()',
    '                if kids:',
    '                    node.right = kids.pop()',
    '        return nodes[0]',
]


def default_main(method, cases, unordered=False, approx=False):
    lines = ['if __name__ == "__main__":', '    s = Solution()']
    if unordered:
        lines += [
            '    def _norm(x):',
            '        return sorted((_norm(i) for i in x), key=repr)'
            ' if isinstance(x, list) else x',
        ]
    lines.append('    cases = [')
    for case in cases:
        lines.append('        ' + repr(case) + ',')
    lines += ['    ]', '    passed = 0', '    for args, expected in cases:', '        try:']
    lines.append('            got = s.{}(*args)'.format(method))
    if approx:
        lines.append('            ok = abs(got - expected) < 1e-5')
    elif unordered:
        lines.append('            ok = _norm(got) == _norm(expected)')
    else:
        lines.append('            ok = got == expected')
    lines += [
        '        except Exception as e:',
        '            got, ok = "<error: {}>".format(repr(e)), False',
    ]
    lines += _RUN_FOOTER
    return "\n".join(lines)


def ll_main(method, cases, result='list'):
    lines = ['if __name__ == "__main__":',
             '    def build(vals):',
             '        dummy = ListNode()',
             '        cur = dummy',
             '        for v in vals:',
             '            cur.next = ListNode(v)',
             '            cur = cur.next',
             '        return dummy.next',
             '    def to_list(node):',
             '        out = []',
             '        while node:',
             '            out.append(node.val)',
             '            node = node.next',
             '        return out',
             '    s = Solution()',
             '    cases = [']
    for case in cases:
        lines.append('        ' + repr(case) + ',')
    lines += ['    ]', '    passed = 0', '    for inp, expected in cases:', '        try:']
    if result == 'list':
        lines.append('            got = to_list(s.{}(build(inp)))'.format(method))
    else:
        lines.append('            got = s.{}(build(inp))'.format(method))
    lines += [
        '            ok = got == expected',
        '        except Exception as e:',
        '            got, ok = "<error: {}>".format(repr(e)), False',
        '        passed += ok',
        '        print(("PASS" if ok else "FAIL"), "input=" + repr(inp),'
        ' "=> got", repr(got), "| expected", repr(expected))',
        '    print("{}/{} passed".format(passed, len(cases)))',
    ]
    return "\n".join(lines)


def tree_main(method, cases, extra_args=False):
    lines = ['if __name__ == "__main__":'] + TREE_BUILDER + ['    s = Solution()', '    cases = [']
    for case in cases:
        lines.append('        ' + repr(case) + ',')
    lines += ['    ]', '    passed = 0']
    if extra_args:
        lines += ['    for vals, arg, expected in cases:', '        try:',
                  '            got = s.{}(build(vals), arg)'.format(method)]
    else:
        lines += ['    for vals, expected in cases:', '        try:',
                  '            got = s.{}(build(vals))'.format(method)]
    lines += [
        '            ok = got == expected',
        '        except Exception as e:',
        '            got, ok = "<error: {}>".format(repr(e)), False',
        '        passed += ok',
        '        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))',
        '    print("{}/{} passed".format(passed, len(cases)))',
    ]
    return "\n".join(lines)


def design_main(classname, ops):
    """ops: list of (method_name, args_list, expected_or_None)."""
    lines = ['if __name__ == "__main__":', '    obj = {}()'.format(classname), '    ops = [']
    for op in ops:
        lines.append('        ' + repr(op) + ',')
    lines += [
        '    ]',
        '    passed = total = 0',
        '    for name, a, expected in ops:',
        '        try:',
        '            got = getattr(obj, name)(*a)',
        '        except Exception as e:',
        '            got = "<error: {}>".format(repr(e))',
        '        if expected is None:',
        '            print("CALL ", name + repr(tuple(a)), "=>", repr(got))',
        '            continue',
        '        total += 1',
        '        ok = got == expected',
        '        passed += ok',
        '        print(("PASS" if ok else "FAIL"), name + repr(tuple(a)),'
        ' "=> got", repr(got), "| expected", repr(expected))',
        '    print("{}/{} passed".format(passed, total))',
    ]
    return "\n".join(lines)


# Per-problem test blocks, keyed by LeetCode problem number.
TESTS = {
    # ---- Array / String ----
    1768: default_main("mergeAlternately", [(("abc", "pqr"), "apbqcr"), (("ab", "pqrs"), "apbqrs"), (("a", "b"), "ab")]),
    1071: default_main("gcdOfStrings", [(("ABCABC", "ABC"), "ABC"), (("ABABAB", "ABAB"), "AB"), (("LEET", "CODE"), "")]),
    1431: default_main("kidsWithCandies", [(([2, 3, 5, 1, 3], 3), [True, True, True, False, True]), (([4, 2, 1, 1, 2], 1), [True, False, False, False, False])]),
    605: default_main("canPlaceFlowers", [(([1, 0, 0, 0, 1], 1), True), (([1, 0, 0, 0, 1], 2), False), (([0], 0), True)]),
    345: default_main("reverseVowels", [(("IceCreAm",), "AceCreIm"), (("leetcode",), "leotcede")]),
    151: default_main("reverseWords", [(("the sky is blue",), "blue is sky the"), (("  hello world  ",), "world hello"), (("a good   example",), "example good a")]),
    238: default_main("productExceptSelf", [(([1, 2, 3, 4],), [24, 12, 8, 6]), (([-1, 1, 0, -3, 3],), [0, 0, 9, 0, 0])]),
    334: default_main("increasingTriplet", [(([1, 2, 3, 4, 5],), True), (([5, 4, 3, 2, 1],), False), (([2, 1, 5, 0, 4, 6],), True)]),
    443: ('if __name__ == "__main__":\n'
          '    s = Solution()\n'
          '    cases = [\n'
          '        (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),\n'
          '        (["a"], 1, ["a"]),\n'
          '        (["a"] + ["b"] * 12, 4, ["a", "b", "1", "2"]),\n'
          '    ]\n'
          '    passed = 0\n'
          '    for chars, klen, expected in cases:\n'
          '        arr = list(chars)\n'
          '        try:\n'
          '            k = s.compress(arr)\n'
          '            ok = k == klen and arr[:k] == expected\n'
          '        except Exception as e:\n'
          '            k, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "=> returned", repr(k),\n'
          '              "| array[:k] expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),

    # ---- Two Pointers ----
    283: ('if __name__ == "__main__":\n'
          '    s = Solution()\n'
          '    cases = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([1, 2, 3], [1, 2, 3])]\n'
          '    passed = 0\n'
          '    for nums, expected in cases:\n'
          '        arr = list(nums)\n'
          '        try:\n'
          '            s.moveZeroes(arr)\n'
          '            ok = arr == expected\n'
          '        except Exception as e:\n'
          '            arr, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "=> got", repr(arr), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),
    392: default_main("isSubsequence", [(("abc", "ahbgdc"), True), (("axc", "ahbgdc"), False), (("", "abc"), True)]),
    11: default_main("maxArea", [(([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49), (([1, 1],), 1)]),
    1679: default_main("maxOperations", [(([1, 2, 3, 4], 5), 2), (([3, 1, 3, 4, 3], 6), 1)]),

    # ---- Sliding Window ----
    643: default_main("findMaxAverage", [(([1, 12, -5, -6, 50, 3], 4), 12.75), (([5], 1), 5.0)], approx=True),
    1456: default_main("maxVowels", [(("abciiidef", 3), 3), (("aeiou", 2), 2), (("leetcode", 3), 2)]),
    1004: default_main("longestOnes", [(([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6), (([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10)]),
    1493: default_main("longestSubarray", [(([1, 1, 0, 1],), 3), (([0, 1, 1, 1, 0, 1, 1, 0, 1],), 5), (([1, 1, 1],), 2)]),

    # ---- Prefix Sum ----
    1732: default_main("largestAltitude", [(([-5, 1, 5, 0, -7],), 1), (([-4, -3, -2, -1, 4, 3, 2],), 0)]),
    724: default_main("pivotIndex", [(([1, 7, 3, 6, 5, 6],), 3), (([1, 2, 3],), -1), (([2, 1, -1],), 0)]),

    # ---- Hash Map / Set ----
    2215: ('if __name__ == "__main__":\n'
           '    s = Solution()\n'
           '    cases = [(([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]]), (([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []])]\n'
           '    passed = 0\n'
           '    for args, expected in cases:\n'
           '        try:\n'
           '            got = s.findDifference(*args)\n'
           '            ok = len(got) == 2 and sorted(got[0]) == sorted(expected[0]) and sorted(got[1]) == sorted(expected[1])\n'
           '        except Exception as e:\n'
           '            got, ok = "<error: {}>".format(repr(e)), False\n'
           '        passed += ok\n'
           '        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))\n'
           '    print("{}/{} passed".format(passed, len(cases)))'),
    1207: default_main("uniqueOccurrences", [(([1, 2, 2, 1, 1, 3],), True), (([1, 2],), False), (([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],), True)]),
    1657: default_main("closeStrings", [(("abc", "bca"), True), (("a", "aa"), False), (("cabbba", "abbccc"), True)]),
    2352: default_main("equalPairs", [(([[3, 2, 1], [1, 7, 6], [2, 7, 7]],), 1), (([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],), 3)]),

    # ---- Stack ----
    2390: default_main("removeStars", [(("leet**cod*e",), "lecoe"), (("erase*****",), "")]),
    735: default_main("asteroidCollision", [(([5, 10, -5],), [5, 10]), (([8, -8],), []), (([10, 2, -5],), [10]), (([-2, -1, 1, 2],), [-2, -1, 1, 2])]),
    394: default_main("decodeString", [(("3[a]2[bc]",), "aaabcbc"), (("3[a2[c]]",), "accaccacc"), (("2[abc]3[cd]ef",), "abcabccdcdcdef")]),

    # ---- Queue ----
    933: design_main("RecentCounter", [("ping", [1], 1), ("ping", [100], 2), ("ping", [3001], 3), ("ping", [3002], 3)]),
    649: default_main("predictPartyVictory", [(("RD",), "Radiant"), (("RDD",), "Dire")]),

    # ---- Linked List ----
    2095: ll_main("deleteMiddle", [([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]), ([1, 2, 3, 4], [1, 2, 4]), ([2, 1], [2]), ([1], [])]),
    328: ll_main("oddEvenList", [([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]), ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])]),
    206: ll_main("reverseList", [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])]),
    2130: ll_main("pairSum", [([5, 4, 2, 1], 6), ([4, 2, 2, 3], 7), ([1, 100000], 100001)], result='scalar'),

    # ---- Binary Tree - DFS ----
    104: tree_main("maxDepth", [([3, 9, 20, None, None, 15, 7], 3), ([1, None, 2], 2), ([], 0)]),
    872: ('if __name__ == "__main__":\n'
          + "\n".join(TREE_BUILDER) + "\n"
          '    s = Solution()\n'
          '    cases = [\n'
          '        ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True),\n'
          '        ([1, 2, 3], [1, 3, 2], False),\n'
          '        ([1], [1], True),\n'
          '    ]\n'
          '    passed = 0\n'
          '    for a, b, expected in cases:\n'
          '        try:\n'
          '            got = s.leafSimilar(build(a), build(b))\n'
          '            ok = got == expected\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),
    1448: tree_main("goodNodes", [([3, 1, 4, 3, None, 1, 5], 4), ([3, 3, None, 4, 2], 3), ([1], 1)]),
    437: tree_main("pathSum", [([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3), ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3)], extra_args=True),
    1372: tree_main("longestZigZag", [([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1], 3), ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4), ([1], 0)]),
    236: ('if __name__ == "__main__":\n'
          + "\n".join(TREE_BUILDER) + "\n"
          '    def find(root, val):\n'
          '        if not root:\n'
          '            return None\n'
          '        if root.val == val:\n'
          '            return root\n'
          '        return find(root.left, val) or find(root.right, val)\n'
          '    s = Solution()\n'
          '    cases = [([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3), ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5)]\n'
          '    passed = 0\n'
          '    for vals, pv, qv, expected in cases:\n'
          '        try:\n'
          '            root = build(vals)\n'
          '            node = s.lowestCommonAncestor(root, find(root, pv), find(root, qv))\n'
          '            got = node.val if node else None\n'
          '            ok = got == expected\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "p,q=", (pv, qv), "=> got", repr(got), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),

    # ---- Binary Tree - BFS ----
    199: tree_main("rightSideView", [([1, 2, 3, None, 5, None, 4], [1, 3, 4]), ([1, None, 3], [1, 3]), ([], [])]),
    1161: tree_main("maxLevelSum", [([1, 7, 0, 7, -8, None, None], 2), ([989, None, 10250, 98693, -89388, None, None, None, -32127], 2)]),

    # ---- Binary Search Tree ----
    700: ('if __name__ == "__main__":\n'
          + "\n".join(TREE_BUILDER) + "\n"
          '    s = Solution()\n'
          '    cases = [([4, 2, 7, 1, 3], 2, 2), ([4, 2, 7, 1, 3], 5, None)]\n'
          '    passed = 0\n'
          '    for vals, val, expected in cases:\n'
          '        try:\n'
          '            res = s.searchBST(build(vals), val)\n'
          '            got = res.val if res else None\n'
          '            ok = got == expected\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "val=", val, "=> got", repr(got), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),
    450: ('if __name__ == "__main__":\n'
          + "\n".join(TREE_BUILDER) + "\n"
          '    def inorder(node):\n'
          '        return inorder(node.left) + [node.val] + inorder(node.right) if node else []\n'
          '    s = Solution()\n'
          '    cases = [([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7]), ([5, 3, 6, 2, 4, None, 7], 0, [2, 3, 4, 5, 6, 7])]\n'
          '    passed = 0\n'
          '    for vals, key, expected in cases:\n'
          '        try:\n'
          '            got = inorder(s.deleteNode(build(vals), key))\n'
          '            ok = got == expected\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "key=", key, "=> inorder", repr(got), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),

    # ---- Graphs - DFS ----
    841: default_main("canVisitAllRooms", [(([[1], [2], [3], []],), True), (([[1, 3], [3, 0, 1], [2], [0]],), False)]),
    547: default_main("findCircleNum", [(([[1, 1, 0], [1, 1, 0], [0, 0, 1]],), 2), (([[1, 0, 0], [0, 1, 0], [0, 0, 1]],), 3)]),
    1466: default_main("minReorder", [((6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3), ((5, [[1, 0], [1, 2], [3, 2], [3, 4]]), 2)]),
    399: ('if __name__ == "__main__":\n'
          '    s = Solution()\n'
          '    cases = [\n'
          '        ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]], [6.0, 0.5, -1.0, 1.0, -1.0]),\n'
          '    ]\n'
          '    passed = 0\n'
          '    for eq, vals, q, expected in cases:\n'
          '        try:\n'
          '            got = s.calcEquation(eq, vals, q)\n'
          '            ok = len(got) == len(expected) and all(abs(x - y) < 1e-5 for x, y in zip(got, expected))\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "=> got", repr(got), "| expected", repr(expected))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),

    # ---- Graphs - BFS ----
    1926: default_main("nearestExit", [(([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]), 1), (([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]), 2), (([[".", "+"]], [0, 0]), -1)]),
    994: default_main("orangesRotting", [(([[2, 1, 1], [1, 1, 0], [0, 1, 1]],), 4), (([[2, 1, 1], [0, 1, 1], [1, 0, 1]],), -1), (([[0, 2]],), 0)]),

    # ---- Heap / Priority Queue ----
    215: default_main("findKthLargest", [(([3, 2, 1, 5, 6, 4], 2), 5), (([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)]),
    2336: design_main("SmallestInfiniteSet", [("addBack", [2], None), ("popSmallest", [], 1), ("popSmallest", [], 2), ("popSmallest", [], 3), ("addBack", [1], None), ("popSmallest", [], 1), ("popSmallest", [], 4), ("popSmallest", [], 5)]),
    2542: default_main("maxScore", [(([1, 3, 3, 2], [2, 1, 3, 4], 3), 12), (([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30)]),
    2462: default_main("totalCost", [(([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4), 11), (([1, 2, 4, 1], 3, 3), 4)]),

    # ---- Binary Search ----
    374: ('if __name__ == "__main__":\n'
          '    s = Solution()\n'
          '    cases = [(10, 6), (1, 1), (2126753390, 1702766719)]\n'
          '    passed = 0\n'
          '    for n, pick in cases:\n'
          '        globals()["_pick"] = pick\n'
          '        try:\n'
          '            got = s.guessNumber(n)\n'
          '            ok = got == pick\n'
          '        except Exception as e:\n'
          '            got, ok = "<error: {}>".format(repr(e)), False\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), "n=", n, "=> got", repr(got), "| expected", repr(pick))\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),
    2300: default_main("successfulPairs", [(([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3]), (([3, 1, 2], [8, 5, 8], 16), [2, 0, 2])]),
    162: ('if __name__ == "__main__":\n'
          '    s = Solution()\n'
          '    cases = [[1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [1], [1, 2]]\n'
          '    passed = 0\n'
          '    for nums in cases:\n'
          '        try:\n'
          '            i = s.findPeakElement(nums)\n'
          '            left = nums[i - 1] if i > 0 else float("-inf")\n'
          '            right = nums[i + 1] if i + 1 < len(nums) else float("-inf")\n'
          '            ok = nums[i] > left and nums[i] > right\n'
          '            detail = "index " + repr(i)\n'
          '        except Exception as e:\n'
          '            ok, detail = False, "<error: {}>".format(repr(e))\n'
          '        passed += ok\n'
          '        print(("PASS" if ok else "FAIL"), repr(nums), "=>", detail)\n'
          '    print("{}/{} passed".format(passed, len(cases)))'),
    875: default_main("minEatingSpeed", [(([3, 6, 7, 11], 8), 4), (([30, 11, 23, 4, 20], 5), 30), (([30, 11, 23, 4, 20], 6), 23)]),

    # ---- Backtracking ----
    17: default_main("letterCombinations", [(("23",), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]), (("",), []), (("2",), ["a", "b", "c"])], unordered=True),
    216: default_main("combinationSum3", [((3, 7), [[1, 2, 4]]), ((3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]), ((4, 1), [])], unordered=True),

    # ---- DP - 1D ----
    1137: default_main("tribonacci", [((4,), 4), ((25,), 1389537), ((0,), 0), ((1,), 1)]),
    746: default_main("minCostClimbingStairs", [(([10, 15, 20],), 15), (([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],), 6)]),
    198: default_main("rob", [(([1, 2, 3, 1],), 4), (([2, 7, 9, 3, 1],), 12)]),
    790: default_main("numTilings", [((3,), 5), ((1,), 1), ((5,), 24)]),

    # ---- DP - Multidimensional ----
    62: default_main("uniquePaths", [((3, 7), 28), ((3, 2), 3)]),
    1143: default_main("longestCommonSubsequence", [(("abcde", "ace"), 3), (("abc", "abc"), 3), (("abc", "def"), 0)]),
    714: default_main("maxProfit", [(([1, 3, 2, 8, 4, 9], 2), 8), (([1, 3, 7, 5, 10, 3], 3), 6)]),
    72: default_main("minDistance", [(("horse", "ros"), 3), (("intention", "execution"), 5)]),

    # ---- Bit Manipulation ----
    338: default_main("countBits", [((2,), [0, 1, 1]), ((5,), [0, 1, 1, 2, 1, 2])]),
    136: default_main("singleNumber", [(([2, 2, 1],), 1), (([4, 1, 2, 1, 2],), 4), (([1],), 1)]),
    1318: default_main("minFlips", [((2, 6, 5), 3), ((4, 2, 7), 1), ((1, 2, 3), 0)]),

    # ---- Trie ----
    208: design_main("Trie", [("insert", ["apple"], None), ("search", ["apple"], True), ("search", ["app"], False), ("startsWith", ["app"], True), ("insert", ["app"], None), ("search", ["app"], True)]),
    1268: default_main("suggestedProducts", [((["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"), [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]])]),

    # ---- Intervals ----
    435: default_main("eraseOverlapIntervals", [(([[1, 2], [2, 3], [3, 4], [1, 3]],), 1), (([[1, 2], [1, 2], [1, 2]],), 2), (([[1, 2], [2, 3]],), 0)]),
    452: default_main("findMinArrowShots", [(([[10, 16], [2, 8], [1, 6], [7, 12]],), 2), (([[1, 2], [3, 4], [5, 6], [7, 8]],), 4), (([[1, 2], [2, 3], [3, 4], [4, 5]],), 2)]),

    # ---- Monotonic Stack ----
    739: default_main("dailyTemperatures", [(([73, 74, 75, 71, 69, 72, 76, 73],), [1, 1, 4, 2, 1, 1, 0, 0]), (([30, 40, 50, 60],), [1, 1, 1, 0]), (([30, 60, 90],), [1, 1, 0])]),
    901: design_main("StockSpanner", [("next", [100], 1), ("next", [80], 1), ("next", [60], 1), ("next", [70], 2), ("next", [60], 1), ("next", [75], 4), ("next", [85], 6)]),
}


def build_file(num, slug, title, difficulty, category, body, stub):
    docstring = '"""\n{num}. {title}\nDifficulty: {diff}\nCategory: {cat}\nhttps://leetcode.com/problems/{slug}/\n\n{body}\n"""'.format(
        num=num, title=title, diff=difficulty, cat=category, slug=slug, body=body.strip())
    test = TESTS.get(num, 'if __name__ == "__main__":\n    # TODO: add quick sanity checks\n    pass')
    return docstring + "\n\n\n" + stub + "\n\n\n" + test + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true",
                        help="overwrite existing solution files")
    parser.add_argument("--seq-prefix", action="store_true", default=True,
                        help="prefix files with a global 01..75 sequence number")
    args = parser.parse_args()

    seq = 0
    rows = []  # (seq, num, title, difficulty, category, relpath)
    for folder, category, problems in CATEGORIES:
        folder_path = os.path.join(ROOT, folder)
        os.makedirs(folder_path, exist_ok=True)
        for num, slug, title, difficulty, body, stub in problems:
            seq += 1
            fname = "{:02d}_{}.py".format(seq, slug.replace("-", "_"))
            fpath = os.path.join(folder_path, fname)
            relpath = os.path.join(folder, fname)
            rows.append((seq, num, title, difficulty, category, relpath))
            if os.path.exists(fpath) and not args.force:
                continue
            with open(fpath, "w") as fh:
                fh.write(build_file(num, slug, title, difficulty, category, body, stub))

    write_readme(rows)
    print("Generated {} problems across {} categories.".format(seq, len(CATEGORIES)))


def write_readme(rows):
    lines = []
    lines.append("# LeetCode 75\n")
    lines.append("A self-contained scaffold for working through the "
                 "[LeetCode 75](https://leetcode.com/studyplan/leetcode-75/) "
                 "study plan one problem at a time.\n")
    lines.append("Each problem lives in its own Python file with the full prompt, "
                 "examples, constraints, a hint, and a solution stub. Fill in the "
                 "`Solution` method, then run the file directly to test.\n")
    lines.append("## How to use\n")
    lines.append("1. Pick the next unchecked problem below.")
    lines.append("2. Open its file and read the docstring (the full problem).")
    lines.append("3. Implement the stub, then run `python <path-to-file>.py`.")
    lines.append("4. Check it off here.")
    lines.append("5. Re-running `python generate.py` will NOT overwrite your work "
                 "(use `--force` to reset).\n")
    lines.append("## Progress\n")

    done = 0
    total = len(rows)
    lines.append("`{}/{}` complete\n".format(done, total))

    current_cat = None
    for seq, num, title, difficulty, category, relpath in rows:
        if category != current_cat:
            current_cat = category
            lines.append("\n### {}\n".format(category))
            lines.append("| # | Problem | Difficulty | File |")
            lines.append("|---|---------|------------|------|")
        lines.append("| {} | [{}. {}](https://leetcode.com/problems/{}/) | {} | `{}` |".format(
            seq, num, title,
            relpath.split("/")[-1].split("_", 1)[1].replace(".py", "").replace("_", "-"),
            difficulty, relpath))

    lines.append("")
    with open(os.path.join(ROOT, "README.md"), "w") as fh:
        fh.write("\n".join(lines))


if __name__ == "__main__":
    main()
