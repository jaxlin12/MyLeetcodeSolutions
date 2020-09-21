#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if (d[i-len(w)] or i-len(w) == -1) and w == s[i-len(w)+1:i+1]:
                    d[i] = True
                    break
        return d[-1]
        
# @lc code=end

