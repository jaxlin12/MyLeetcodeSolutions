#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""
        elif size == 1:
            return strs[0]
        prefix = ""
        min_size = min(len(strs[0]), len(strs[1]))
        for i in range(min_size):
            if strs[0][i] == strs[1][i]:
                prefix = prefix + strs[0][i]
            else:
                break
        
        for i in range(2, size):
            str_size = len(strs[i])
            if prefix == "" or str_size == 0:
                return ""
            min_size = min(len(prefix), str_size)
            prefix = prefix[:min_size]
            for j in range(min_size):
                if prefix[j] == strs[i][j]:
                    continue
                else:
                    prefix = prefix[:j]
                    break

        return prefix
                
# @lc code=end

