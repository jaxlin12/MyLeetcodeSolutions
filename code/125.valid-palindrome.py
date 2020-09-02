#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        size = len(s)
        if size == 0 or size == 1:
            return True
        
        i = 0
        j = size-1
        while i < j:
            while i < j and not s[i].isdigit() and not s[i].isalpha():
                i = i + 1
            while i < j and not s[j].isdigit() and not s[j].isalpha():
                j = j - 1
            if s[i].upper() != s[j].upper():
                return False
            i = i + 1
            j = j - 1
        return True


# @lc code=end

