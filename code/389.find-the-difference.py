#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s:
            ans ^= ord(c)
        for c in t:
            ans ^= ord(c)           
        return chr(ans)  
# @lc code=end

