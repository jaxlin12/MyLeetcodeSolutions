#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size = len(palindrome)
        j = size - 1
        ret = ""
        mid = size // 2
        for i in range(size):
            if palindrome[i] == 'a' or i == mid:
                continue
            else:
                ret = palindrome[:i] + 'a' + palindrome[i+1:]
                break
        if(ret == "" and size > 1):
            ret = palindrome[:-1] + 'b'
        return ret
                                                                 
# @lc code=end

