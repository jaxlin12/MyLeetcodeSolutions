#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dictionary = {}
        for char in s:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1
        odd = 0
        for item in dictionary:
            odd += (dictionary[item] % 2)
        if odd == 0:
            return len(s)
        return len(s) - odd + 1

# @lc code=end

