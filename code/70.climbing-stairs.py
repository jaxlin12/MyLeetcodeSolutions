#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
#Top-Down Approach:
    # def DP(self, n):
    #     if self.ways[n] != None:
    #         return self.ways[n]
    #     if n == 0:
    #         self.ways[n] = 0
    #         return 0
    #     elif n == 1:
    #         self.ways[n] = 1
    #         return 1
    #     elif n == 2:
    #         self.ways[n] = 2
    #         return 2

    #     self.ways[n] = self.DP(n-1) + self.DP(n-2)
    #     return self.ways[n]

    # def climbStairs(self, n: int) -> int:
    #     self.ways = [None] * (n+1)
    #     return self.DP(n)
        
#Bottom-up Approach:
    def climbStairs(self, n: int) -> int:
        
        ways = [0] * (n+1)
        ways[1] = 1
        if n > 1:
            ways[2] = 2
        else:
            return ways[n]
        for index in range(3, n+1):
            ways[index] = ways[index-1] + ways[index-2]
        return ways[n]
        
# @lc code=end

