"""
443. String Compression
Difficulty: Medium
Category: Array / String
https://leetcode.com/problems/string-compression/

Given an array of characters chars, compress it in place. For each group of
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
  - Use a read pointer to count runs and a write pointer to emit the result.
"""


from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        
        curr_count = 1
        curr_char = chars[0]
        curr_pos = 0

        for i in range(1, len(chars)):
            if chars[i] == curr_char:
                curr_count += 1
            else:
                # final_list.append(curr_char)
                chars[curr_pos] = curr_char
                if curr_count > 1:
                    for j in range(len(str(curr_count))):
                        chars[curr_pos + 1 + j] = list(str(curr_count))[j]
                    curr_pos += 2 + j
                else:
                    curr_pos += 1
                curr_char = chars[i]
                curr_count = 1

        chars[curr_pos] = curr_char
        
        if curr_count > 1:
            for i in range(len(str(curr_count))):
                chars[curr_pos + 1 + i] = list(str(curr_count))[i]
            # print(chars)
            return len(chars[:curr_pos + 1 + i]) + 1
        # print(chars)
        return len(chars[:curr_pos + 1])

                


if __name__ == "__main__":
    s = Solution()
    cases = [
        (["a", "a", "b", "b", "c", "c", "c"], 6, ["a", "2", "b", "2", "c", "3"]),
        (["a"], 1, ["a"]),
        (["a"] + ["b"] * 12, 4, ["a", "b", "1", "2"]),
    ]
    passed = 0
    for chars, klen, expected in cases:
        arr = list(chars)
        try:
            k = s.compress(arr)
            ok = k == klen and arr[:k] == expected
        except Exception as e:
            k, ok = "<error: {}>".format(repr(e)), False
        passed += ok
        print(("PASS" if ok else "FAIL"), "=> returned", repr(k),
              "| array[:k] expected", repr(expected))
    print("{}/{} passed".format(passed, len(cases)))
