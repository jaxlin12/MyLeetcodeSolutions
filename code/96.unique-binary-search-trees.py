#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        self.save = [None] * (n+1)
        return self.dfs(1, n+1)
        
    def dfs(self, start, end):
        if start == end:
            return 1
        if self.save[end - start] != None:
            return self.save[end - start]
        self.save[end - start] = 0
        for i in range(start, end):
            self.save[end - start] += self.dfs(start, i) * self.dfs(i+1, end)
        return self.save[end - start]
# @lc code=end

