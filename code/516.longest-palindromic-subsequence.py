#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def DP(self, s, i, j):
        if self.memory[i][j] != -1:
            return self.memory[i][j]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            self.memory[i][j] = self.DP(s, i+1, j-1) + 2
        else:
            self.memory[i][j] = max(self.DP(s, i+1, j), self.DP(s, i, j-1))
        return self.memory[i][j]
        

    def longestPalindromeSubseq(self, s: str) -> int:
        self.memory = []
        for i in range(len(s)):
            self.memory.append([-1]*len(s))
        return self.DP(s, 0, len(s)-1)
        
# @lc code=end

