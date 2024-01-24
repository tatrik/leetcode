"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

from typing import Tuple


class Solution:
    def longest_palindrome(self, s: str) -> str:
        start, end = 0, 0

        def expand_around_center(left: int, right: int) -> Tuple[int, int]:
            nonlocal start, end
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left) > (end - start):
                    start, end = left, right
                left -= 1
                right += 1

        for i in range(len(s)):
            expand_around_center(i,i)
            expand_around_center(i,i+1)

        return s[start:end+1]
