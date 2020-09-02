#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # if len(s) <= 1:
        #     return False
        # T = [-1 for c in s]
        # pos = 0
        # for i in range(1, len(s)):
        #     if s[i] == s[pos]:
        #         T[i] = T[pos]
        #     else:
        #         T[i] = pos
        #         pos = T[pos]
        #         while pos >= 0 and s[i] != s[pos]:
        #             pos = T[pos]
        #     pos += 1
        # lens = len(s) - pos
        # if lens == 0 or len(s) % lens != 0 or len(s) == lens:
        #     return False
        # return True
        
        return s in (s+s)[1:-1]

# @lc code=end

