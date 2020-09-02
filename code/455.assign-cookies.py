#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        i = len(g)-1
        j = len(s)-1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                i -=1
                j -= 1
            else:
                i -= 1
        return count

        
# @lc code=end

