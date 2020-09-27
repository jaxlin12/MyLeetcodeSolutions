#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        rev = s[i:]
        rev = rev[::-1]
        return rev + self.shortestPalindrome(s[:i]) + s[i:]
        
# @lc code=end

